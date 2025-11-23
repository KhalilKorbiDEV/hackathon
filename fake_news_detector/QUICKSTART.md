# 🚀 QUICK START GUIDE

## Installation & Setup (3 Steps)

### ✅ Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**
- numpy - Numerical computing
- pandas - Data manipulation
- scikit-learn - Machine learning
- Flask - Web framework
- matplotlib - Visualization
- seaborn - Statistical graphics
- joblib - Model serialization

### ✅ Step 2: Train the Model

```bash
python train.py
```

This will:
- Generate 2000 sample articles (fake & real)
- Train the ML model (~95% accuracy)
- Save model to `models/fake_news_model.pkl`
- Display performance metrics

**Expected output:**
```
============================================================
🚀 FAKE NEWS DETECTION MODEL TRAINING
============================================================

📊 Step 1: Generating sample dataset...
Generated 2000 samples in data/fake_news_data.csv

🤖 Step 2: Training ML model...
Training samples: 1600, Test samples: 400
Vectorizing text...
Training model...
Model trained! Accuracy: 0.9525

💾 Step 3: Saving model...
Model saved to models/fake_news_model.pkl

============================================================
✅ TRAINING COMPLETE!
============================================================

📈 Model Performance Metrics:
   • Accuracy:  0.9525 (95.25%)
   • Precision: 0.9418 (94.18%)
   • Recall:    0.9625 (96.25%)
   • F1-Score:  0.9521 (95.21%)

📚 Training Samples: 1600
📚 Test Samples: 400

🚀 Next Step: Run the web app with:
   python app.py
```

### ✅ Step 3: Run the Web Application

```bash
python app.py
```

**Expected output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

Open your browser to: **http://localhost:5000**

---

## 🎯 Web Interface Features

### Tab 1: Single Prediction 📰
- Paste any news article or headline
- Get instant classification (Fake/Real)
- View confidence percentage (0-100%)
- See probability breakdown

**Example:**
```
Input: "Scientists discover miracle cure hidden by Big Pharma"
Output: FAKE NEWS ⚠️ (89% confidence)
        - Probability Fake: 89%
        - Probability Real: 11%
```

### Tab 2: Batch Analysis 📊
- Analyze multiple articles at once
- One article per line
- Get summary statistics
- View fake/real breakdown

**Example:**
```
Input:
Article 1
Article 2
Article 3

Output:
✓ Total Analyzed: 3
✓ Real News: 2
✓ Fake News: 1
✓ Fake %: 33.33%
```

### Tab 3: Analytics & Visualizations 📈

**Available Visualizations:**

1. **Confusion Matrix Heatmap** 🔥
   - True/False positives
   - True/False negatives
   - Shows model accuracy

2. **Performance Metrics Chart** 📊
   - Accuracy comparison
   - Precision & Recall
   - F1-Score
   - Training vs test distribution

3. **ROC Curve** 📉
   - Model discrimination ability
   - AUC score
   - Threshold analysis

4. **Prediction Distribution** 📊
   - How confident model is
   - Histogram of probabilities
   - Separates fake vs real patterns

5. **Feature Importance Heatmap** 🎯
   - Which words matter most
   - Fake news indicators
   - Real news indicators

6. **Training Progress** 📈
   - Accuracy over epochs
   - Convergence tracking
   - Mean accuracy line

7. **Performance Radar** 🎨
   - Multi-metric overview
   - All scores in one view
   - Easy comparison

---

## 📁 Project Structure

```
fake_news_detector/
│
├── 📄 Core Files
│   ├── app.py              Flask web application & API
│   ├── model.py            ML model & detector
│   ├── visualizer.py       Charts & heatmaps
│   ├── data_generator.py   Sample data generation
│   └── train.py            Training script
│
├── 📁 Web Interface
│   └── templates/
│       └── index.html      Full-featured web UI
│
├── 📁 Data & Models
│   ├── data/               Dataset folder
│   │   └── fake_news_data.csv
│   └── models/             Saved models
│       └── fake_news_model.pkl
│
├── 📁 Static Assets
│   └── static/             CSS, JS, images
│
├── 📖 Documentation
│   ├── requirements.txt    Python dependencies
│   ├── README.md          Full documentation
│   ├── QUICKSTART.md      This file
│   ├── test_setup.py      Component tests
│   └── examples.py        Usage examples
│
└── 🔧 Utilities
    ├── run.bat            Windows quick start
    └── run.sh             Linux/Mac quick start
```

---

## 🧪 Testing Your Installation

Run the test script:
```bash
python test_setup.py
```

Expected output:
```
============================================================
🧪 FAKE NEWS DETECTION SYSTEM - COMPONENT TEST
============================================================

🧪 Testing imports...
  ✓ NumPy
  ✓ Pandas
  ✓ Scikit-learn
  ✓ Flask
  ✓ Matplotlib
  ✓ Seaborn
  ✓ Joblib
✅ All imports successful!

🧪 Testing model components...
  ✓ Model class imported
  ✓ Data generator imported
  ✓ Visualizer imported
✅ All components imported successfully!

🧪 Testing Flask application...
  ✓ Flask app imported
  ✓ Routes initialized
✅ Flask application ready!

============================================================
📊 TEST SUMMARY
============================================================
Imports: ✅ PASSED
Model Components: ✅ PASSED
Flask App: ✅ PASSED

✅ All tests passed! System is ready to use.
```

---

## 🔧 Quick Troubleshooting

### Python Not Found
```bash
# Check Python installation
python --version

# Install Python 3.8+ from: https://www.python.org/
```

### Module Not Found
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Or individually:
pip install numpy pandas scikit-learn flask matplotlib seaborn joblib
```

### Port Already in Use
Edit `app.py`:
```python
if __name__ == '__main__':
    app.run(port=5001)  # Change from 5000 to 5001
```

### Model File Not Found
```bash
# Train the model first
python train.py
```

---

## 📊 API Examples

### Python Requests
```python
import requests

# Single prediction
response = requests.post('http://localhost:5000/api/predict', 
    json={'text': 'Your article here'})
print(response.json())

# Batch analysis
response = requests.post('http://localhost:5000/api/batch-predict',
    json={'texts': ['Article 1', 'Article 2']})
print(response.json())

# Get metrics
response = requests.get('http://localhost:5000/api/metrics')
print(response.json())
```

### cURL
```bash
# Single prediction
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Your news article"}'

# Batch analysis
curl -X POST http://localhost:5000/api/batch-predict \
  -H "Content-Type: application/json" \
  -d '{"texts": ["Article 1", "Article 2"]}'

# Get metrics
curl http://localhost:5000/api/metrics
```

---

## 🎓 Usage Examples

### Run Examples
```bash
python examples.py
```

This provides:
1. Single article prediction
2. Batch article analysis
3. Model performance metrics display
4. API request/response formats
5. System data flow explanation

---

## 🚀 Advanced Usage

### Using with Custom Data
```python
from model import FakeNewsDetector

# Create and train detector
detector = FakeNewsDetector()
detector.train('your_data.csv')  # CSV with columns: title, content, label
detector.save_model('custom_model.pkl')

# Use the model
result = detector.predict("Your text here")
print(f"Is Fake: {result['is_fake']}")
print(f"Confidence: {result['confidence']}")
```

### Batch Processing
```python
texts = [
    "Article 1",
    "Article 2",
    "Article 3"
]

for text in texts:
    result = detector.predict(text)
    print(f"{text[:50]}... → {'FAKE' if result['is_fake'] else 'REAL'}")
```

### Generate Visualizations
```python
from visualizer import visualizer

# Generate individual visualizations
heatmap_b64 = visualizer.create_confusion_matrix_heatmap(cm)
chart_b64 = visualizer.create_accuracy_chart(metrics)
roc_b64 = visualizer.create_roc_curve(y_true, y_proba)
```

---

## 📞 Support & Help

**Common Issues:**

1. **"Model not found"**
   - Run: `python train.py`

2. **"Port 5000 already in use"**
   - Edit app.py and change port to 5001

3. **"Import error"**
   - Run: `pip install -r requirements.txt`

4. **"Flask not responding"**
   - Check if app.py is running
   - Ensure port is not blocked

---

## 📈 Next Steps

1. ✅ Installation complete
2. ✅ Model trained
3. ✅ Web server running
4. 📊 Explore the analytics dashboard
5. 🔗 Integrate with your application
6. 🚀 Deploy to production

---

**Build with ❤️ using Python | AI-Powered Fake News Detection**
