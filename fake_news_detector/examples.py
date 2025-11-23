"""
Example usage of the Fake News Detection system
Demonstrates various features and API usage
"""

from model import FakeNewsDetector
from visualizer import VisualizationEngine
import os
import json

def example_single_prediction():
    """Example: Single article prediction"""
    print("\n" + "="*60)
    print("EXAMPLE 1: Single Article Prediction")
    print("="*60)
    
    detector = FakeNewsDetector()
    
    # Try to load existing model
    try:
        detector.load_model('models/fake_news_model.pkl')
    except:
        print("Model not found. Train first with: python train.py")
        return
    
    # Example texts
    articles = [
        "Scientists discover breakthrough cure for disease using advanced research methods",
        "Breaking: Secret government conspiracy revealed by anonymous sources online",
        "Tech company announces new sustainable energy solution",
        "Shocking video proves earth is flat according to social media claims"
    ]
    
    for article in articles:
        result = detector.predict(article)
        print(f"\nArticle: {article[:60]}...")
        print(f"  Classification: {'FAKE' if result['is_fake'] else 'REAL'}")
        print(f"  Confidence: {result['confidence']*100:.2f}%")
        print(f"  Probability: Fake={result['probability_fake']*100:.1f}%, Real={result['probability_real']*100:.1f}%")

def example_batch_analysis():
    """Example: Batch processing multiple articles"""
    print("\n" + "="*60)
    print("EXAMPLE 2: Batch Article Analysis")
    print("="*60)
    
    detector = FakeNewsDetector()
    
    try:
        detector.load_model('models/fake_news_model.pkl')
    except:
        print("Model not found. Train first with: python train.py")
        return
    
    articles = [
        "New study from MIT shows positive results",
        "Illuminati controls world through 5G towers",
        "Stock market hits new record high this quarter",
        "Aliens landed near Area 51 last night",
    ]
    
    fake_count = 0
    real_count = 0
    
    print("\nAnalyzing batch of 4 articles...")
    for i, article in enumerate(articles, 1):
        result = detector.predict(article)
        label = "FAKE ⚠️" if result['is_fake'] else "REAL ✓"
        
        if result['is_fake']:
            fake_count += 1
        else:
            real_count += 1
        
        print(f"\n  [{i}] {label} | Confidence: {result['confidence']*100:.1f}%")
        print(f"      {article[:50]}...")
    
    print(f"\n📊 Summary:")
    print(f"   Total: {len(articles)} articles")
    print(f"   Real: {real_count}")
    print(f"   Fake: {fake_count}")
    print(f"   Fake percentage: {(fake_count/len(articles)*100):.1f}%")

def example_metrics_display():
    """Example: Display model metrics"""
    print("\n" + "="*60)
    print("EXAMPLE 3: Model Performance Metrics")
    print("="*60)
    
    detector = FakeNewsDetector()
    
    try:
        detector.load_model('models/fake_news_model.pkl')
    except:
        print("Model not found. Train first with: python train.py")
        return
    
    metrics = detector.get_metrics()
    
    print("\n📊 Model Metrics:")
    print(f"  • Accuracy:  {metrics['accuracy']:.4f} ({metrics['accuracy']*100:.2f}%)")
    print(f"  • Precision: {metrics['precision']:.4f} ({metrics['precision']*100:.2f}%)")
    print(f"  • Recall:    {metrics['recall']:.4f} ({metrics['recall']*100:.2f}%)")
    print(f"  • F1-Score:  {metrics['f1']:.4f} ({metrics['f1']*100:.2f}%)")
    
    print(f"\n📚 Dataset Statistics:")
    print(f"  • Training samples: {metrics['training_samples']}")
    print(f"  • Test samples: {metrics['test_samples']}")
    print(f"  • Total samples: {metrics['training_samples'] + metrics['test_samples']}")
    
    # Confusion matrix
    cm = detector.get_confusion_matrix()
    if cm:
        print(f"\n📋 Confusion Matrix:")
        print(f"  True Negatives (Real predicted as Real):   {cm[0][0]}")
        print(f"  False Positives (Real predicted as Fake):  {cm[0][1]}")
        print(f"  False Negatives (Fake predicted as Real):  {cm[1][0]}")
        print(f"  True Positives (Fake predicted as Fake):   {cm[1][1]}")

def example_api_format():
    """Example: Show API request/response formats"""
    print("\n" + "="*60)
    print("EXAMPLE 4: API Request/Response Formats")
    print("="*60)
    
    print("\n📝 Single Prediction API:")
    print("  Request (POST /api/predict):")
    print("  {")
    print('    "text": "Your news article here..."')
    print("  }")
    print("\n  Response:")
    print("  {")
    print('    "success": true,')
    print('    "is_fake": false,')
    print('    "confidence": 87.5,')
    print('    "probability_fake": 12.5,')
    print('    "probability_real": 87.5,')
    print('    "label": "REAL NEWS ✓",')
    print('    "color": "#2ecc71"')
    print("  }")
    
    print("\n📊 Batch Prediction API:")
    print("  Request (POST /api/batch-predict):")
    print("  {")
    print('    "texts": ["Article 1", "Article 2", ...]')
    print("  }")
    print("\n  Response:")
    print("  {")
    print('    "success": true,')
    print('    "results": [')
    print("      {")
    print('        "text": "Article 1...",')
    print('        "is_fake": true,')
    print('        "confidence": 92.3,')
    print('        "label": "FAKE"')
    print("      },")
    print("      ...")
    print("    ],")
    print('    "summary": {')
    print('      "total": 10,')
    print('      "fake": 3,')
    print('      "real": 7,')
    print('      "fake_percentage": 30.0')
    print("    }")
    print("  }")

def example_data_flow():
    """Example: Explain the data flow"""
    print("\n" + "="*60)
    print("EXAMPLE 5: System Data Flow")
    print("="*60)
    
    print("""
1️⃣  INPUT LAYER
    └─ User enters article text
    └─ Text validation (min 10 chars)

2️⃣  PREPROCESSING
    └─ Combine title + content
    └─ Lowercase conversion
    └─ Remove special characters (optional)

3️⃣  VECTORIZATION
    └─ TF-IDF transformation
    └─ Convert text to numerical features
    └─ Max 5000 features selected

4️⃣  CLASSIFICATION
    └─ Logistic Regression model
    └─ Predict probability (0.0 to 1.0)
    └─ 1.0 = Likely fake, 0.0 = Likely real

5️⃣  OUTPUT LAYER
    └─ Generate confidence score
    └─ Create visualizations
    └─ Return results to user

6️⃣  VISUALIZATION
    └─ Confusion matrix heatmap
    └─ Performance metrics chart
    └─ ROC curve
    └─ Prediction distribution
    └─ Feature importance heatmap
    """)

def main():
    print("\n" + "="*60)
    print("🔍 FAKE NEWS DETECTION - USAGE EXAMPLES")
    print("="*60)
    
    print("\nAvailable examples:")
    print("  1. Single article prediction")
    print("  2. Batch article analysis")
    print("  3. Model performance metrics")
    print("  4. API request/response formats")
    print("  5. System data flow")
    print("  6. Run all examples")
    
    choice = input("\nSelect example (1-6) or press Enter to run all: ").strip()
    
    if choice == '1':
        example_single_prediction()
    elif choice == '2':
        example_batch_analysis()
    elif choice == '3':
        example_metrics_display()
    elif choice == '4':
        example_api_format()
    elif choice == '5':
        example_data_flow()
    elif choice == '6' or choice == '':
        example_single_prediction()
        example_batch_analysis()
        example_metrics_display()
        example_api_format()
        example_data_flow()
    else:
        print("Invalid selection")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
