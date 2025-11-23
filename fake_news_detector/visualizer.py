"""
Visualization module for analytics and graphs
Creates heatmaps, confusion matrices, accuracy charts, etc.
"""

import json
import base64
from io import BytesIO
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

class VisualizationEngine:
    def __init__(self):
        self.figures = {}
        sns.set_style("darkgrid")
        plt.rcParams['figure.figsize'] = (10, 6)
    
    def create_confusion_matrix_heatmap(self, confusion_matrix):
        """Create confusion matrix heatmap"""
        plt.figure(figsize=(8, 6))
        sns.heatmap(confusion_matrix, annot=True, fmt='d', cmap='Blues', 
                   xticklabels=['Real', 'Fake'],
                   yticklabels=['Real', 'Fake'],
                   cbar_kws={'label': 'Count'})
        plt.title('Confusion Matrix - Fake News Detection', fontsize=14, fontweight='bold')
        plt.ylabel('Actual', fontsize=12)
        plt.xlabel('Predicted', fontsize=12)
        
        return self._fig_to_base64()
    
    def create_accuracy_chart(self, metrics):
        """Create accuracy and performance metrics bar chart"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
        
        # Metrics bar chart
        metric_names = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
        metric_values = [metrics.get('accuracy', 0), 
                        metrics.get('precision', 0),
                        metrics.get('recall', 0),
                        metrics.get('f1', 0)]
        
        colors = ['#2ecc71', '#3498db', '#e74c3c', '#f39c12']
        bars = ax1.bar(metric_names, metric_values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
        ax1.set_ylim([0, 1])
        ax1.set_ylabel('Score', fontsize=11, fontweight='bold')
        ax1.set_title('Model Performance Metrics', fontsize=12, fontweight='bold')
        ax1.grid(axis='y', alpha=0.3)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.3f}',
                    ha='center', va='bottom', fontweight='bold')
        
        # Training statistics
        training_samples = metrics.get('training_samples', 0)
        test_samples = metrics.get('test_samples', 0)
        
        stats_labels = [f'Training\n{training_samples}', f'Testing\n{test_samples}']
        stats_values = [training_samples, test_samples]
        
        bars2 = ax2.bar(stats_labels, stats_values, color=['#3498db', '#e74c3c'], alpha=0.8, edgecolor='black', linewidth=1.5)
        ax2.set_ylabel('Sample Count', fontsize=11, fontweight='bold')
        ax2.set_title('Dataset Distribution', fontsize=12, fontweight='bold')
        ax2.grid(axis='y', alpha=0.3)
        
        for bar in bars2:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}',
                    ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        return self._fig_to_base64()
    
    def create_roc_curve(self, y_true, y_proba):
        """Create ROC curve"""
        from sklearn.metrics import roc_curve, auc
        
        fpr, tpr, _ = roc_curve(y_true, y_proba)
        roc_auc = auc(fpr, tpr)
        
        plt.figure(figsize=(8, 6))
        plt.plot(fpr, tpr, color='#2ecc71', lw=2, label=f'ROC Curve (AUC = {roc_auc:.3f})')
        plt.plot([0, 1], [0, 1], color='#e74c3c', lw=2, linestyle='--', label='Random Classifier')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate', fontsize=11, fontweight='bold')
        plt.ylabel('True Positive Rate', fontsize=11, fontweight='bold')
        plt.title('ROC Curve - Model Performance', fontsize=12, fontweight='bold')
        plt.legend(loc="lower right", fontsize=10)
        plt.grid(alpha=0.3)
        
        return self._fig_to_base64()
    
    def create_prediction_distribution(self, y_true, y_proba):
        """Create probability distribution visualization"""
        fake_probs = [y_proba[i][1] for i in range(len(y_true)) if y_true[i] == 1]
        real_probs = [y_proba[i][1] for i in range(len(y_true)) if y_true[i] == 0]
        
        plt.figure(figsize=(10, 6))
        plt.hist(fake_probs, bins=30, alpha=0.6, label='Fake News', color='#e74c3c', edgecolor='black')
        plt.hist(real_probs, bins=30, alpha=0.6, label='Real News', color='#2ecc71', edgecolor='black')
        plt.xlabel('Confidence Score (Fake)', fontsize=11, fontweight='bold')
        plt.ylabel('Frequency', fontsize=11, fontweight='bold')
        plt.title('Prediction Confidence Distribution', fontsize=12, fontweight='bold')
        plt.legend(fontsize=10)
        plt.grid(alpha=0.3)
        
        return self._fig_to_base64()
    
    def create_feature_importance_heatmap(self, top_features=20):
        """Create mock feature importance heatmap"""
        # Generate synthetic important features
        features = ['government', 'truth', 'secret', 'study', 'research',
                   'official', 'confirmed', 'alleged', 'claims', 'sources',
                   'leaked', 'proven', 'evidence', 'data', 'verified',
                   'anonymous', 'unconfirmed', 'theory', 'fake', 'real'][:top_features]
        
        # Importance scores
        importance = np.random.rand(top_features, 2)
        importance = importance / importance.sum(axis=1, keepdims=True)
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(importance, annot=True, fmt='.3f', cmap='RdYlGn',
                   xticklabels=['Real News Weight', 'Fake News Weight'],
                   yticklabels=features,
                   cbar_kws={'label': 'Feature Weight'})
        plt.title('Top Feature Importance Heatmap', fontsize=12, fontweight='bold')
        plt.ylabel('Features', fontsize=11, fontweight='bold')
        
        return self._fig_to_base64()
    
    def create_accuracy_over_time(self):
        """Create mock accuracy improvement over time"""
        epochs = list(range(1, 21))
        accuracy = [0.5 + 0.45 * (1 - np.exp(-i/5)) + np.random.normal(0, 0.02) for i in epochs]
        accuracy = [min(max(x, 0.5), 0.99) for x in accuracy]
        
        plt.figure(figsize=(10, 6))
        plt.plot(epochs, accuracy, marker='o', linewidth=2, markersize=8, color='#3498db', label='Training Accuracy')
        plt.axhline(y=np.mean(accuracy), color='#e74c3c', linestyle='--', label=f'Mean: {np.mean(accuracy):.3f}')
        plt.xlabel('Epoch', fontsize=11, fontweight='bold')
        plt.ylabel('Accuracy', fontsize=11, fontweight='bold')
        plt.title('Model Training Progress', fontsize=12, fontweight='bold')
        plt.ylim([0.45, 1.0])
        plt.grid(alpha=0.3)
        plt.legend(fontsize=10)
        
        return self._fig_to_base64()
    
    def create_performance_radar(self, metrics):
        """Create radar chart for model performance"""
        from math import pi
        
        categories = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
        values = [
            metrics.get('accuracy', 0),
            metrics.get('precision', 0),
            metrics.get('recall', 0),
            metrics.get('f1', 0)
        ]
        
        # Add first value at end to complete the circle
        values += values[:1]
        angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
        angles += angles[:1]
        
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
        ax.plot(angles, values, 'o-', linewidth=2, color='#3498db', label='Performance')
        ax.fill(angles, values, alpha=0.25, color='#3498db')
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, fontsize=10)
        ax.set_ylim(0, 1)
        ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
        ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], fontsize=8)
        ax.grid(True)
        ax.set_title('Model Performance Radar', fontsize=12, fontweight='bold', pad=20)
        
        return self._fig_to_base64()
    
    def _fig_to_base64(self):
        """Convert matplotlib figure to base64 string"""
        buffer = BytesIO()
        plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode()
        plt.close()
        return image_base64

# Global visualization engine
visualizer = VisualizationEngine()
