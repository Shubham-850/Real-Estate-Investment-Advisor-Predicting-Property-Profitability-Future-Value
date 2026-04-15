🏠 Real Estate Investment Advisor

A Machine Learning-based web application that predicts property prices and determines whether a property is a good investment based on user inputs like city, BHK, size, property type, and age.

🚀 Features
📊 Predicts property price (in Lakhs)
✅ Classifies property as Good / Bad investment
🏙️ Supports multiple cities and property types
⚙️ Uses feature engineering for better accuracy
🌐 Interactive UI built with Streamlit
🧠 Tech Stack
Python 🐍
Pandas & NumPy
Scikit-learn
Streamlit
Joblib
📁 Project Structure
real_estate_project/
│
├── models/
│   ├── classification_model.pkl
│   ├── regression_model.pkl
│   ├── city_encoder.pkl
│   ├── type_encoder.pkl
│
├── india_housing_prices.csv
├── app.py
├── training_script.py
└── README.md
⚙️ How It Works
Data preprocessing & feature engineering
Encode categorical features (City, Property Type)
Train:
RandomForestClassifier → Investment prediction
RandomForestRegressor → Price prediction
Deploy using Streamlit UI
▶️ How to Run
1. Install dependencies
pip install pandas numpy scikit-learn streamlit joblib
2. Train the model
python training_script.py
3. Run the app
streamlit run app.py
📌 Inputs
City
Property Type
BHK
Size (SqFt)
Year Built
📈 Output
💰 Estimated Price (Lakhs)
📊 Investment Decision (Good / Not Good)
🧠 Key Learnings
Handling real-world noisy data
Feature engineering for better predictions
Avoiding model bias & unrealistic outputs
Building end-to-end ML apps
🚀 Future Improvements
Add location-based pricing (latitude/longitude)
Improve accuracy with advanced models
Add price trend visualization
Deploy on cloud (Streamlit Cloud / Render)
👨‍💻 Author

Shubham Rathore
