"""
Training script for the fake news detection model
Generates data, trains the model, and saves it
"""

import os
import sys
from data_generator import generate_sample_data
from model import detector

def main():
    print("=" * 60)
    print("🚀 FAKE NEWS DETECTION MODEL TRAINING")
    print("=" * 60)
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    os.makedirs('models', exist_ok=True)
    
    # Generate dataset
    print("\n📊 Step 1: Generating sample dataset...")
    data_path = generate_sample_data('data/fake_news_data.csv', num_samples=2000)
    
    # Train model
    print("\n🤖 Step 2: Training ML model...")
    metrics = detector.train(data_path)
    
    # Save model
    print("\n💾 Step 3: Saving model...")
    detector.save_model('models/fake_news_model.pkl')
    
    # Display results
    print("\n" + "=" * 60)
    print("✅ TRAINING COMPLETE!")
    print("=" * 60)
    print(f"\n📈 Model Performance Metrics:")
    print(f"   • Accuracy:  {metrics['accuracy']:.4f} ({metrics['accuracy']*100:.2f}%)")
    print(f"   • Precision: {metrics['precision']:.4f} ({metrics['precision']*100:.2f}%)")
    print(f"   • Recall:    {metrics['recall']:.4f} ({metrics['recall']*100:.2f}%)")
    print(f"   • F1-Score:  {metrics['f1']:.4f} ({metrics['f1']*100:.2f}%)")
    print(f"\n📚 Training Samples: {metrics['training_samples']}")
    print(f"📚 Test Samples: {metrics['test_samples']}")
    
    print("\n🚀 Next Step: Run the web app with:")
    print("   python app.py")
    print("\nThen open your browser to: http://localhost:5000")
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
