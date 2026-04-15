import streamlit as st
import pandas as pd
import joblib

# ===============================
# LOAD MODELS + ENCODERS
# ===============================
@st.cache_resource
def load_all():
    clf = joblib.load("models/classification_model.pkl")
    reg = joblib.load("models/regression_model.pkl")
    le_city = joblib.load("models/city_encoder.pkl")
    le_type = joblib.load("models/type_encoder.pkl")
    return clf, reg, le_city, le_type

clf, reg, le_city, le_type = load_all()

# ===============================
# UI
# ===============================
st.set_page_config(page_title="Real Estate Advisor")
st.title("🏠 Real Estate Investment Advisor")

st.sidebar.header("Property Inputs")

# ✅ Inputs

city = st.sidebar.selectbox("City", le_city.classes_)
ptype = st.sidebar.selectbox("Property Type", le_type.classes_)

bhk = st.sidebar.slider("BHK", 1, 5, 2)

size = st.sidebar.number_input("Size (SqFt)", 300, 5000, 1000)

price_sqft = st.sidebar.number_input(
    "Price per SqFt", min_value=1000, max_value=20000, value=5000
)

year = st.sidebar.number_input("Year Built", 1990, 2026, 2015)

# ===============================
# TRANSFORM INPUTS
# ===============================
city_encoded = le_city.transform([city])[0]
type_encoded = le_type.transform([ptype])[0]

age = 2026 - year

# ===============================
# CREATE INPUT DATA
# ===============================
input_data = pd.DataFrame({
    "City": [city_encoded],
    "Property_Type": [type_encoded],
    "BHK": [bhk],
    "Size_in_SqFt": [size],
    "Price_per_SqFt": [price_sqft],
    "Age_of_Property": [age]
})

st.write("### 📥 Input Data")
st.write(input_data)

# ===============================
# PREDICTION
# ===============================
if st.button("Predict"):

    try:
        investment = clf.predict(input_data)[0]
        price = reg.predict(input_data)[0]

        st.write("### 📊 Results")

        if investment == 1:
            st.success("✅ Good Investment")
        else:
            st.error("❌ Not a Good Investment")

        st.metric("💰 Estimated Price (Lakhs)", f"{round(price,2)}")

    except Exception as e:
        st.error(f"Error: {e}")