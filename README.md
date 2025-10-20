# Heart Disease Prediction - Full Stack Application

A complete full-stack web application for predicting heart disease using Machine Learning, FastAPI backend, and React.js frontend with Tailwind CSS.

![Heart Disease Prediction](https://img.shields.io/badge/ML-Heart%20Disease%20Prediction-red)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![React](https://img.shields.io/badge/React-18.0+-61dafb)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green)

## 🎯 Features

- ✨ **Machine Learning Prediction**: Uses trained SVM model for accurate heart disease prediction
- 🚀 **FastAPI Backend**: High-performance Python backend with automatic API documentation
- ⚛️ **React.js Frontend**: Modern, responsive UI built with React and Tailwind CSS
- ✅ **Real-time Validation**: Input validation on both frontend and backend
- 📊 **Probability Scores**: Confidence levels for predictions
- 📱 **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- 🎨 **Beautiful UI**: Modern gradient design with intuitive user experience

## 📁 Project Structure

```
HEART-DISEASE-PREDICTION/
│
├── backend/
│   ├── data_validation/
│   │   └── response_data_validation.py    # Response validation schemas
|   |   |---input_data_validation.py       # Input Validation schemas
│   │
│   ├── model/
│   │   ├── __pycache__/                   # Python cache files
│   │   ├── heart_disease_svm_model.pkl    # Trained SVM model
│   │   └── prediction.py                  # Prediction logic
│   │
│   ├── Heart_Disease.ipynb                # Model training notebook
│   ├── main.py                            # FastAPI application
│   └── requirements.txt                   # Python dependencies
│
├── frontend/
│   ├── node_modules/                      # Node dependencies
│   ├── public/                            # Static files
│   │
│   ├── src/
│   │   ├── components/
│   │   │   └── Prediction1.js            # Main prediction component
│   │   ├── App.css                       # App styles
│   │   ├── App.js                        # Main App component
│   │   
│   └── tailwind.config.js                # Tailwind configuration
│
└── README.md                             # This file
```

## 🚀 Quick Start

### Prerequisites

- **Python**: 3.8 or higher
- **Node.js**: 16.0 or higher
- **npm**: 8.0 or higher
- **pip**: Latest version

### Installation

#### 1. Clone the Repository

```bash
git clone <repository-url>
cd HEART-DISEASE-PREDICTION
```

#### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the backend server
python main.py
```

The backend will start on `http://localhost:8000`

#### 3. Frontend Setup

```bash
# Open new terminal and navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

The frontend will start on `http://localhost:3000`

## 📚 API Documentation

Once the backend is running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Main Endpoints

#### 1. Root Endpoint
```http
GET /
```
Returns API information and status

#### 2. Health Check
```http
GET /health
```
Verify API and model status

#### 3. Predict Heart Disease
```http
POST /predict
```

**Request Body:**
```json
{
  "age": 55,
  "sex": 1,
  "cp": 2,
  "trestbps": 130,
  "chol": 250,
  "fbs": 1,
  "restecg": 0,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 2,
  "ca": 0,
  "thal": 3
}
```

**Response:**
```json
{
  "prediction": 1,
  "probability": 0.85,
  "risk_level": "High Risk",
  "message": "The model predicts a high risk of heart disease. Please consult a healthcare professional."
}
```

#### 4. Model Information
```http
GET /model-info
```
Get details about the loaded ML model

## 📊 Feature Descriptions

| Feature | Description | Type | Range | Required |
|---------|-------------|------|-------|----------|
| **age** | Age in years | Numeric | 1-120 | ✅ |
| **sex** | Sex (1=male, 0=female) | Categorical | 0-1 | ✅ |
| **cp** | Chest pain type | Categorical | 1-4 | ✅ |
| **trestbps** | Resting blood pressure (mm Hg) | Numeric | 80-200 | ✅ |
| **chol** | Serum cholesterol (mg/dl) | Numeric | 100-600 | ✅ |
| **fbs** | Fasting blood sugar > 120 mg/dl | Categorical | 0-1 | ✅ |
| **restecg** | Resting ECG results | Categorical | 0-2 | ✅ |
| **thalach** | Maximum heart rate achieved | Numeric | 60-220 | ✅ |
| **exang** | Exercise induced angina | Categorical | 0-1 | ✅ |
| **oldpeak** | ST depression induced by exercise | Numeric | 0-10 | ✅ |
| **slope** | Slope of peak exercise ST segment | Categorical | 1-3 | ✅ |
| **ca** | Number of major vessels (0-3) | Categorical | 0-3 | ✅ |
| **thal** | Thalassemia | Categorical | 3,6,7 | ✅ |

### Detailed Feature Explanations

**Chest Pain Type (cp):**
- 1: Typical Angina
- 2: Atypical Angina
- 3: Non-anginal Pain
- 4: Asymptomatic

**Resting ECG (restecg):**
- 0: Normal
- 1: ST-T Wave Abnormality
- 2: Left Ventricular Hypertrophy

**Slope:**
- 1: Upsloping
- 2: Flat
- 3: Downsloping

**Thalassemia (thal):**
- 3: Normal
- 6: Fixed Defect
- 7: Reversible Defect

## 🧪 Testing

### Test Backend API

**Using cURL:**
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "age": 55, "sex": 1, "cp": 2, "trestbps": 130,
       "chol": 250, "fbs": 1, "restecg": 0, "thalach": 150,
       "exang": 0, "oldpeak": 2.3, "slope": 2, "ca": 0, "thal": 3
     }'
```

**Using Python:**
```python
import requests

url = "http://localhost:8000/predict"
data = {
    "age": 55, "sex": 1, "cp": 2, "trestbps": 130,
    "chol": 250, "fbs": 1, "restecg": 0, "thalach": 150,
    "exang": 0, "oldpeak": 2.3, "slope": 2, "ca": 0, "thal": 3
}

response = requests.post(url, json=data)
print(response.json())
```

### Test Frontend

1. Open http://localhost:3000
2. Fill in all required fields
3. Click "Predict Risk" button
4. View prediction results in the right panel
5. Click "Reset" to clear the form

## 🛠️ Technologies Used

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for FastAPI
- **Pydantic**: Data validation using Python type annotations
- **scikit-learn**: Machine learning library
- **NumPy**: Numerical computing library

### Frontend
- **React.js**: JavaScript library for building user interfaces
- **Tailwind CSS**: Utility-first CSS framework
- **Lucide React**: Beautiful icon library
- **Fetch API**: HTTP requests to backend

### Machine Learning
- **Algorithm**: Support Vector Machine (SVM)
- **Dataset**: UCI Heart Disease Dataset
- **Features**: 13 clinical features
- **Task**: Binary classification (Disease/No Disease)

## 🚨 Troubleshooting

### Common Backend Issues

**❌ Error: `No module named 'numpy._core'`**
```bash
pip uninstall numpy scikit-learn -y
pip install numpy==1.26.4 scikit-learn==1.4.2
```

**❌ Error: `Model not loaded`**
- Ensure `heart_disease_svm_model.pkl` exists in `backend/model/` directory
- Check file permissions
- Verify model was trained and saved correctly

**❌ Error: `Port 8000 already in use`**
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:8000 | xargs kill -9
```

**❌ Error: `CORS policy blocked`**
- Check `allow_origins` in `main.py` includes your frontend URL
- Default should be `["*"]` for development

### Common Frontend Issues

**❌ Error: `Cannot connect to backend`**
- Verify backend is running on http://localhost:8000
- Check API URL in `Prediction1.js`
- Check browser console for detailed errors

**❌ Error: `Tailwind styles not working`**
```bash
# Rebuild Tailwind
npm run build:css

# Or restart dev server
npm start
```

## 📈 Model Performance

The SVM model achieves the following metrics on the test set:

- **Accuracy**: ~90%
- **Precision**: ~87%
- **Recall**: ~87%
- **F1-Score**: ~87%

*Note: Actual performance may vary based on the specific dataset and training parameters*

## ⚠️ Important Disclaimer

**This application is for educational and demonstration purposes only.**

- ❌ **NOT a medical diagnosis tool**
- ❌ **NOT a substitute for professional medical advice**
- ❌ **NOT intended for clinical use**

✅ **Always consult qualified healthcare professionals** for proper medical evaluation and diagnosis.

## 🔒 Security Considerations

For production deployment:

1. **Environment Variables**: Use `.env` files for sensitive data
2. **CORS**: Restrict `allow_origins` to specific domains
3. **HTTPS**: Always use HTTPS in production
4. **API Keys**: Implement authentication for API endpoints
5. **Rate Limiting**: Add rate limiting to prevent abuse
6. **Input Sanitization**: Already implemented via Pydantic validation


## 🤝 Contributing

Contributions are welcome!

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Md Al Mahbub Hossain

## 🙏 Acknowledgments

- UCI Machine Learning Repository for the Heart Disease Dataset
- FastAPI team for the excellent framework
- React and Tailwind CSS communities
- All contributors to the scikit-learn library

## 📞 Support

For support, please:
- Open an issue in the repository
- Contact: mmdmahbub292@gmail.com
- Documentation: Check `/docs` for detailed API documentation

## 🔄 Version History

- **v1.0.0** (Current)
  - Initial release
  - SVM model implementation
  - Full-stack integration
  - Responsive UI with Tailwind CSS

---

**Made with ❤️ for healthcare and machine learning enthusiasts**

*Last Updated: October 2025*