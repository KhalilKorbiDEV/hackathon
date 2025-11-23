# ba7ath.tn - Fact-Checking & Image Authentication Platform

A powerful, dual-engine verification system combining AI-powered fact-checking with forensic image analysis. ba7ath.tn helps you identify misinformation and expose image manipulation in real-time.

## 🎯 Features

### Text Verification
- **Dual-Engine Analysis**: Combines Perplexity API LLM with local NLP model
- **Verdict Classification**: TRUE, FALSE, MIXED, or UNVERIFIABLE
- **Confidence Scoring**: Detailed confidence metrics with meta-analysis
- **Historical Context**: Investigates claims dating back to the 1800s-1900s
- **Source Attribution**: Provides authoritative sources and references

### Image Analysis
- **Metadata Forensics**: EXIF data extraction and analysis
- **ELA Detection**: Error Level Analysis for compression anomalies
- **Tampering Detection**: Identifies edited or composited images
- **Authenticity Scoring**: 0-100 scale with forensic flags

### User Experience
- **Modern UI**: Red/brown theme with bold, accessible design
- **Session History**: Track all verification sessions
- **Real-time Processing**: Live results with progress indicators
- **Responsive Design**: Works on desktop and mobile

## 🏗️ Project Structure

```
hackathon/
├── back_end/              # Flask API server
│   ├── app.py            # Main Flask application
│   ├── model.pkl         # Trained scikit-learn model
│   ├── vectorizer.pkl    # TF-IDF vectorizer
│   ├── requirements.txt  # Python dependencies
│   └── train.py          # Model training script
├── front_end/             # React + Vite frontend
│   ├── src/
│   │   ├── App.jsx       # Main React component
│   │   ├── main.jsx      # Entry point
│   │   └── assets/       # Static assets
│   ├── package.json      # npm dependencies
│   └── vite.config.js    # Vite configuration
└── README.md             # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- Perplexity API Key (get one at [perplexity.ai](https://www.perplexity.ai))

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/KhalilKorbiDEV/hackathon.git
   cd hackathon
   ```

2. **Backend Setup**
   ```bash
   cd back_end
   pip install -r requirements.txt
   ```
   
   Create a `.env` file with your API key:
   ```
   PERPLEXITY_API_KEY=your_api_key_here
   ```

3. **Frontend Setup**
   ```bash
   cd ../front_end
   npm install
   ```

### Running the Application

**Terminal 1 - Backend Server:**
```bash
cd back_end
python app.py
```
Backend runs on: `http://localhost:5000`

**Terminal 2 - Frontend Server:**
```bash
cd front_end
npm run dev
```
Frontend runs on: `http://localhost:5173`

### Access the Application
Open your browser and navigate to: **`http://localhost:5173`**

## 🔧 Technology Stack

### Backend
- **Framework**: Flask + Flask-CORS
- **ML Models**: scikit-learn (Logistic Regression, TF-IDF Vectorizer)
- **AI Integration**: Perplexity API (sonar-pro model)
- **Image Processing**: Pillow, ELA (Error Level Analysis)
- **Data Handling**: pandas, joblib

### Frontend
- **Framework**: React 18
- **Build Tool**: Vite
- **Styling**: Tailwind CSS
- **Icons**: Lucide React
- **HTTP**: Fetch API

## 📊 How It Works

### Text Verification Flow
1. User submits a claim
2. Backend processes with:
   - **LLM Engine**: Perplexity API analyzes historical records
   - **Local NLP**: Pre-trained scikit-learn model for quick classification
   - **Heuristics**: Sensationalism detection, URL analysis, text patterns
3. Engines vote on verdict with confidence scores
4. Meta-analysis combines signals into final confidence
5. Results displayed with sources and historical context

### Image Analysis Flow
1. User uploads image
2. Backend extracts:
   - EXIF metadata (camera, software, datetime)
   - Error Level Analysis (ELA score)
   - Resolution and aspect ratio info
3. Forensic analysis detects:
   - Editing software signatures
   - Compression artifacts
   - Metadata anomalies
4. Authenticity score generated (0-100)
5. Tampering verdict issued with forensic flags

## 🎨 Branding

**Color Palette:**
- Primary Brown-Red: `#A22829`
- Dark Brown-Red: `#9C2A2B`
- Lobster Pink: `#C05E5A`
- Black: `#000000`
- White: `#FFFFFF`

## 📝 Environment Variables

**Backend (.env file)**
```
PERPLEXITY_API_KEY=your_api_key_here
```

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## 📄 License

This project is part of the hackathon initiative.

## 🔗 API Endpoints

### POST /api/verify
Verify a text claim
```json
{
  "text": "Claim to verify"
}
```

### POST /api/analyze-image
Analyze image for tampering
```
multipart/form-data
image: <image-file>
```

### GET /
Access the HTML interface (backend)

## 🐛 Troubleshooting

### Backend Issues
- **Missing Dependencies**: Run `pip install -r requirements.txt`
- **API Key Error**: Check `.env` file has valid Perplexity key
- **Model Loading**: Ensure `model.pkl` and `vectorizer.pkl` exist in `back_end/`

### Frontend Issues
- **npm install fails**: Delete `node_modules` and `package-lock.json`, then retry
- **Port conflicts**: Change port in `vite.config.js` if 5173 is in use
- **CORS errors**: Verify backend is running and accessible

## 📧 Support

For issues or questions, create an issue on the GitHub repository.

---

**Made with ⚙️ for truth verification**
