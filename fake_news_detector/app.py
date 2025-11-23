"""
Flask web application for fake news detection
Handles routing, predictions, and visualization
"""

from flask import Flask, render_template, request, jsonify, send_file
import os
import sys
from model import detector
from visualizer import visualizer
import json
from datetime import datetime

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

# Initialize model
model_path = 'models/fake_news_model.pkl'
model_trained = False

try:
    detector.load_model(model_path)
    model_trained = True
    print("✓ Model loaded successfully")
except:
    print("⚠ Model not found. Train model first: python train.py")

@app.route('/')
def index():
    """Serve main page"""
    return render_template('index.html', model_trained=model_trained)

@app.route('/api/predict', methods=['POST'])
def predict():
    """API endpoint for predictions"""
    if not model_trained:
        return jsonify({'error': 'Model not trained yet'}), 400
    
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({'error': 'Empty text provided'}), 400
        
        if len(text) < 10:
            return jsonify({'error': 'Text too short (minimum 10 characters)'}), 400
        
        result = detector.predict(text)
        
        return jsonify({
            'success': True,
            'is_fake': result['is_fake'],
            'confidence': round(result['confidence'] * 100, 2),
            'probability_fake': round(result['probability_fake'] * 100, 2),
            'probability_real': round(result['probability_real'] * 100, 2),
            'label': 'FAKE NEWS ⚠️' if result['is_fake'] else 'REAL NEWS ✓',
            'color': '#e74c3c' if result['is_fake'] else '#2ecc71'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/metrics')
def get_metrics():
    """Get model performance metrics"""
    if not model_trained:
        return jsonify({'error': 'Model not trained'}), 400
    
    metrics = detector.get_metrics()
    confusion_matrix = detector.get_confusion_matrix()
    
    return jsonify({
        'metrics': metrics,
        'confusion_matrix': confusion_matrix
    })

@app.route('/api/visualizations')
def get_visualizations():
    """Generate and return all visualizations"""
    if not model_trained:
        return jsonify({'error': 'Model not trained'}), 400
    
    try:
        metrics = detector.get_metrics()
        predictions = detector.get_last_predictions()
        
        if predictions is None:
            return jsonify({'error': 'No predictions available'}), 400
        
        y_true = predictions['y_true']
        y_proba = predictions['y_proba']
        y_pred = predictions['y_pred']
        
        visualizations = {
            'confusion_matrix': visualizer.create_confusion_matrix_heatmap(
                detector.get_confusion_matrix()
            ),
            'metrics_chart': visualizer.create_accuracy_chart(metrics),
            'roc_curve': visualizer.create_roc_curve(y_true, [p[1] for p in y_proba]),
            'prediction_dist': visualizer.create_prediction_distribution(y_true, y_proba),
            'feature_importance': visualizer.create_feature_importance_heatmap(),
            'training_progress': visualizer.create_accuracy_over_time(),
            'performance_radar': visualizer.create_performance_radar(metrics),
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify({'visualizations': visualizations})
    
    except Exception as e:
        print(f"Error generating visualizations: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/batch-predict', methods=['POST'])
def batch_predict():
    """Batch prediction endpoint"""
    if not model_trained:
        return jsonify({'error': 'Model not trained'}), 400
    
    try:
        data = request.get_json()
        texts = data.get('texts', [])
        
        if not texts or len(texts) == 0:
            return jsonify({'error': 'No texts provided'}), 400
        
        results = []
        for text in texts:
            if len(text.strip()) < 10:
                continue
            
            result = detector.predict(text)
            results.append({
                'text': text[:100],
                'is_fake': result['is_fake'],
                'confidence': round(result['confidence'] * 100, 2),
                'label': 'FAKE' if result['is_fake'] else 'REAL'
            })
        
        fake_count = sum(1 for r in results if r['is_fake'])
        real_count = len(results) - fake_count
        
        return jsonify({
            'success': True,
            'results': results,
            'summary': {
                'total': len(results),
                'fake': fake_count,
                'real': real_count,
                'fake_percentage': round((fake_count / len(results) * 100) if results else 0, 2)
            }
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats')
def get_stats():
    """Get application statistics"""
    metrics = detector.get_metrics() if model_trained else {}
    
    return jsonify({
        'model_trained': model_trained,
        'metrics': metrics,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model_trained,
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
