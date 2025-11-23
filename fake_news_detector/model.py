"""
Machine Learning model for fake news detection
Uses TfidfVectorizer and LogisticRegression
"""

import pickle
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import pandas as pd
import json
from datetime import datetime

class FakeNewsDetector:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
        self.model = LogisticRegression(max_iter=1000)
        self.metrics = {}
        self.confusion_mat = None
        self.training_history = []
        
    def train(self, csv_path):
        """Train the model on provided data"""
        print("Loading data...")
        df = pd.read_csv(csv_path)
        
        # Combine title and content for better feature extraction
        df['text'] = df['title'].fillna('') + ' ' + df['content'].fillna('')
        
        X = df['text'].values
        y = (df['label'] == 'fake').astype(int).values  # 1 for fake, 0 for real
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")
        print("Vectorizing text...")
        X_train_vec = self.vectorizer.fit_transform(X_train)
        X_test_vec = self.vectorizer.transform(X_test)
        
        print("Training model...")
        self.model.fit(X_train_vec, y_train)
        
        # Predictions
        y_pred = self.model.predict(X_test_vec)
        y_pred_proba = self.model.predict_proba(X_test_vec)
        
        # Calculate metrics
        self.metrics = {
            'accuracy': float(accuracy_score(y_test, y_pred)),
            'precision': float(precision_score(y_test, y_pred)),
            'recall': float(recall_score(y_test, y_pred)),
            'f1': float(f1_score(y_test, y_pred)),
            'training_samples': len(X_train),
            'test_samples': len(X_test),
        }
        
        self.confusion_mat = confusion_matrix(y_test, y_pred)
        
        # Store predictions for heatmap visualization
        self.last_predictions = {
            'y_true': y_test.tolist(),
            'y_pred': y_pred.tolist(),
            'y_proba': y_pred_proba.tolist(),
            'report': classification_report(y_test, y_pred, output_dict=True)
        }
        
        print(f"Model trained! Accuracy: {self.metrics['accuracy']:.4f}")
        return self.metrics
    
    def predict(self, text):
        """Predict if text is fake or real"""
        X_vec = self.vectorizer.transform([text])
        prediction = self.model.predict(X_vec)[0]
        probability = self.model.predict_proba(X_vec)[0]
        
        return {
            'is_fake': bool(prediction == 1),
            'confidence': float(probability[1]),
            'probability_fake': float(probability[1]),
            'probability_real': float(probability[0]),
        }
    
    def save_model(self, filepath='models/fake_news_model.pkl'):
        """Save the trained model"""
        joblib.dump({
            'vectorizer': self.vectorizer,
            'model': self.model,
            'metrics': self.metrics,
        }, filepath)
        print(f"Model saved to {filepath}")
    
    def load_model(self, filepath='models/fake_news_model.pkl'):
        """Load a trained model"""
        data = joblib.load(filepath)
        self.vectorizer = data['vectorizer']
        self.model = data['model']
        self.metrics = data['metrics']
        print(f"Model loaded from {filepath}")
    
    def get_metrics(self):
        """Return model metrics"""
        return self.metrics
    
    def get_confusion_matrix(self):
        """Return confusion matrix"""
        return self.confusion_mat.tolist() if self.confusion_mat is not None else None
    
    def get_last_predictions(self):
        """Return last predictions for analysis"""
        return self.last_predictions if hasattr(self, 'last_predictions') else None

# Global model instance
detector = FakeNewsDetector()

if __name__ == "__main__":
    detector.train('data/fake_news_data.csv')
    detector.save_model()
