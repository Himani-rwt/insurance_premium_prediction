Insurance Premium Prediction API

A machine learning-powered REST API built with FastAPI that predicts a person's insurance premium category (Low / Medium / High) based on their age, BMI, income, smoking status, occupation, and city tier. The model is trained using scikit-learn and served through a validated, production-style API with Docker support.

Features
REST API built with FastAPI and served via Uvicorn
Request validation using Pydantic (rejects invalid input before it reaches the model)
ML model trained with scikit-learn (Random Forest Classifier)
Returns predicted category along with confidence score and class probabilities
Fully containerized with Docker for consistent, portable deployment
Organized codebase with separate config, model, and schema modules
Tech Stack
Category	Tools
Backend Framework	FastAPI
Server	Uvicorn
Validation	Pydantic
ML	scikit-learn, pandas
Containerization	Docker
Project Structure
insurance_premium_prediction/
├── app.py                      # FastAPI application entry point
├── config/
│   └── city_tier.py             # City tier mapping logic
├── model/
│   ├── model.pkl                 # Trained ML model
│   └── predict.py                # Prediction logic
├── schema/
│   ├── user_input.py             # Pydantic request schema
│   └── prediction_response.py    # Pydantic response schema
├── requirements.txt
├── Dockerfile
└── README.md
Model Details
Algorithm: Random Forest Classifier
Features used: age, BMI (derived from weight/height), income, smoker status, occupation, city tier
Target: insurance_premium_category (Low / Medium / High)
Preprocessing: Categorical features encoded, numeric features passed through
Getting Started
Option 1: Run with Docker (recommended)
bash
# Build the image
docker build -t insurance-premium-api .

# Run the container
docker run -p 8000:8000 insurance-premium-api
Option 2: Run locally without Docker
bash
# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn app:app --host 0.0.0.0 --port 8000
API Usage

Once running, open:

Interactive API docs (Swagger UI): http://localhost:8000/docs
Root endpoint: http://localhost:8000/
Example Request
json
POST /predict
{
  "age": 35,
  "height": 1.75,
  "weight": 70,
  "income_lpa": 12.5,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
Example Response
json
{
  "response": {
    "predicted_category": "Medium",
    "confidence": 0.74,
    "class_probabilities": {
      "High": 0.12,
      "Low": 0.14,
      "Medium": 0.74
    }
  }
}

Note: height must be provided in meters (e.g. 1.75, not 175).

Author

Himani Rawat