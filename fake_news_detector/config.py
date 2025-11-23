"""
Configuration and utilities for the Fake News Detection system
"""

import os
import json
from datetime import datetime

class Config:
    """Application configuration"""
    
    # Flask
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 5000
    SECRET_KEY = 'fake-news-detector-secret-key-2024'
    
    # Model
    MODEL_PATH = 'models/fake_news_model.pkl'
    DATA_PATH = 'data/fake_news_data.csv'
    
    # Training
    TRAINING_SAMPLES = 2000
    TEST_SIZE = 0.2
    MAX_FEATURES = 5000
    
    # Visualization
    FIGURE_DPI = 100
    FIGURE_SIZE = (10, 6)
    STYLE = 'darkgrid'
    
    # Thresholds
    MIN_TEXT_LENGTH = 10
    CONFIDENCE_THRESHOLD = 0.5
    
    # Directories
    DIRS = {
        'data': 'data',
        'models': 'models',
        'templates': 'templates',
        'static': 'static',
    }
    
    @classmethod
    def init_directories(cls):
        """Create necessary directories"""
        for dir_path in cls.DIRS.values():
            os.makedirs(dir_path, exist_ok=True)
    
    @classmethod
    def to_dict(cls):
        """Convert config to dictionary"""
        return {
            'debug': cls.DEBUG,
            'host': cls.HOST,
            'port': cls.PORT,
            'model_path': cls.MODEL_PATH,
            'training_samples': cls.TRAINING_SAMPLES,
            'test_size': cls.TEST_SIZE,
            'max_features': cls.MAX_FEATURES,
        }

class Logger:
    """Simple logging utility"""
    
    def __init__(self, name='FakeNewsDetector'):
        self.name = name
        self.log_file = f'logs/{name}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
        os.makedirs('logs', exist_ok=True)
    
    def _format_message(self, level, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] [{level}] {message}"
    
    def info(self, message):
        """Log info message"""
        msg = self._format_message("INFO", message)
        print(f"ℹ️  {msg}")
        self._write_to_file(msg)
    
    def success(self, message):
        """Log success message"""
        msg = self._format_message("SUCCESS", message)
        print(f"✅ {msg}")
        self._write_to_file(msg)
    
    def warning(self, message):
        """Log warning message"""
        msg = self._format_message("WARNING", message)
        print(f"⚠️  {msg}")
        self._write_to_file(msg)
    
    def error(self, message):
        """Log error message"""
        msg = self._format_message("ERROR", message)
        print(f"❌ {msg}")
        self._write_to_file(msg)
    
    def _write_to_file(self, message):
        """Write message to log file"""
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(message + '\n')
        except:
            pass

class Stats:
    """Statistics tracking"""
    
    def __init__(self):
        self.predictions = 0
        self.predictions_fake = 0
        self.predictions_real = 0
        self.avg_confidence = 0
        self.start_time = datetime.now()
    
    def add_prediction(self, is_fake, confidence):
        """Add prediction to statistics"""
        self.predictions += 1
        if is_fake:
            self.predictions_fake += 1
        else:
            self.predictions_real += 1
        
        # Update average confidence
        self.avg_confidence = (
            (self.avg_confidence * (self.predictions - 1) + confidence) / self.predictions
        )
    
    def get_summary(self):
        """Get statistics summary"""
        uptime = datetime.now() - self.start_time
        
        return {
            'total_predictions': self.predictions,
            'fake_predictions': self.predictions_fake,
            'real_predictions': self.predictions_real,
            'fake_percentage': (self.predictions_fake / self.predictions * 100) 
                              if self.predictions > 0 else 0,
            'average_confidence': self.avg_confidence,
            'uptime_seconds': uptime.total_seconds(),
            'uptime_formatted': self._format_uptime(uptime),
        }
    
    @staticmethod
    def _format_uptime(uptime):
        """Format uptime as human readable string"""
        total_seconds = int(uptime.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours}h {minutes}m {seconds}s"

class DataValidator:
    """Data validation utilities"""
    
    @staticmethod
    def validate_text(text):
        """Validate input text"""
        if not text:
            return False, "Text cannot be empty"
        
        if len(text.strip()) < 10:
            return False, "Text must be at least 10 characters"
        
        if len(text) > 50000:
            return False, "Text exceeds maximum length (50000 chars)"
        
        return True, "Valid"
    
    @staticmethod
    def validate_csv(filepath):
        """Validate CSV data format"""
        try:
            import pandas as pd
            df = pd.read_csv(filepath)
            
            required_cols = ['title', 'content', 'label']
            missing = [col for col in required_cols if col not in df.columns]
            
            if missing:
                return False, f"Missing columns: {missing}"
            
            if len(df) == 0:
                return False, "CSV is empty"
            
            return True, f"Valid CSV with {len(df)} rows"
        
        except Exception as e:
            return False, f"Error reading CSV: {str(e)}"

# Global instances
config = Config()
logger = Logger()
stats = Stats()
validator = DataValidator()

# Initialize on import
config.init_directories()

if __name__ == "__main__":
    print("Configuration and Utilities Module")
    print("\nLoaded Modules:")
    print("  • Config - Application configuration")
    print("  • Logger - Logging utility")
    print("  • Stats - Statistics tracking")
    print("  • DataValidator - Input validation")
    print("\nConfig Summary:")
    for key, value in config.to_dict().items():
        print(f"  {key}: {value}")
