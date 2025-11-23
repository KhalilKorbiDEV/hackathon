"""
Test script to verify all components work correctly
Run this after installation to test the system
"""

import sys
import os

def test_imports():
    """Test if all required packages are installed"""
    print("🧪 Testing imports...")
    
    packages = [
        ('numpy', 'NumPy'),
        ('pandas', 'Pandas'),
        ('sklearn', 'Scikit-learn'),
        ('flask', 'Flask'),
        ('matplotlib', 'Matplotlib'),
        ('seaborn', 'Seaborn'),
        ('joblib', 'Joblib'),
    ]
    
    failed = []
    for package, name in packages:
        try:
            __import__(package)
            print(f"  ✓ {name}")
        except ImportError:
            print(f"  ✗ {name} - NOT INSTALLED")
            failed.append(package)
    
    if failed:
        print(f"\n❌ Missing packages: {', '.join(failed)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("✅ All imports successful!\n")
    return True

def test_model_structure():
    """Test if model components can be imported"""
    print("🧪 Testing model components...")
    
    try:
        from model import FakeNewsDetector
        print("  ✓ Model class imported")
        
        from data_generator import generate_sample_data
        print("  ✓ Data generator imported")
        
        from visualizer import VisualizationEngine
        print("  ✓ Visualizer imported")
        
        print("✅ All components imported successfully!\n")
        return True
    except Exception as e:
        print(f"✗ Error importing components: {e}\n")
        return False

def test_app_structure():
    """Test if Flask app can be imported"""
    print("🧪 Testing Flask application...")
    
    try:
        from app import app
        print("  ✓ Flask app imported")
        print("  ✓ Routes initialized")
        print("✅ Flask application ready!\n")
        return True
    except Exception as e:
        print(f"✗ Error: {e}\n")
        return False

def main():
    print("=" * 60)
    print("🧪 FAKE NEWS DETECTION SYSTEM - COMPONENT TEST")
    print("=" * 60)
    print()
    
    results = []
    
    results.append(("Imports", test_imports()))
    results.append(("Model Components", test_model_structure()))
    results.append(("Flask App", test_app_structure()))
    
    print("=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    for name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{name}: {status}")
    
    if all(r[1] for r in results):
        print("\n✅ All tests passed! System is ready to use.")
        print("\n📖 Next steps:")
        print("   1. Run: python train.py    (to train the model)")
        print("   2. Run: python app.py      (to start the web server)")
        print("   3. Open: http://localhost:5000")
        return 0
    else:
        print("\n❌ Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
