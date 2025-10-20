import pickle
from data_validation.response_data_validation import PredictionResponse

try:
    with open('model/heart_disease_svm_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("✅ Model loaded successfully!")
except FileNotFoundError:
    print("❌ Error: model.pkl not found. Please place your trained model in the same directory.")
    model = None
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

def predict_output(user_input):

    # df = pd.DataFrame([user_input])
    # print(df.shape)
    prediction = int(model.predict(user_input))
        
    # Get probability if available
    probability = None
    if hasattr(model, 'predict_proba'):
        proba = model.predict_proba(user_input)
        probability = float(proba[1])  # Probability of disease (class 1)
        
    # Determine risk level
    risk_level = "High Risk" if prediction == 1 else "Low Risk"
    
    # Create response message
    if prediction == 1:
        message = "The model predicts a high risk of heart disease. Please consult a healthcare professional for proper medical evaluation."
    else:
        message = "The model predicts a low risk of heart disease. However, regular check-ups are still recommended."
    
    return PredictionResponse(
        prediction=prediction,
        probability=probability,
        risk_level=risk_level,
        message=message
    )
 
