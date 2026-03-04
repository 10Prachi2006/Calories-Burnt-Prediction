import streamlit as st
import pickle
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import io

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Feature names and importance
feature_names = ['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']
feature_importances = [2.6829557e-02, 2.2189368e-02, 2.2731243e-04, 5.4935524e-03, 
                       8.9905035e-01, 4.6048563e-02, 1.6127460e-04]

# Set page config
st.set_page_config(page_title="Calories Burnt Prediction", layout="wide", initial_sidebar_state="expanded")

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["🏠 Home", "ℹ️ Model Info"])

# ==================== HOME PAGE ====================
if page == "🏠 Home":
    st.title("🔥 Calories Burnt Prediction")
    st.write("Enter your fitness data to predict calories burnt during exercise")
    
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        # Create two columns for input
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Personal Information")
            gender = st.selectbox("Gender", ["male", "female"])
            age = st.number_input("Age (years)", min_value=1, max_value=120, value=30, 
                                 help="Your age in years (typically 18-80)")
            height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170,
                                    help="Your height in centimeters")
            weight = st.number_input("Weight (kg)", min_value=20, max_value=200, value=70,
                                    help="Your body weight in kilograms")

        with col2:
            st.subheader("Exercise Information")
            duration = st.number_input("Duration (minutes)", min_value=0.1, max_value=200.0, value=30.0,
                                      help="Exercise duration in minutes")
            heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=220, value=100,
                                        help="Your heart rate during exercise (beats per minute)")
            body_temp = st.number_input("Body Temperature (°C)", min_value=36.0, max_value=42.0, value=37.0,
                                       help="Your body temperature in Celsius")

    with col_right:
        st.subheader("Quick Actions")
        if st.button("📋 Use Sample Data", key="sample", use_container_width=True):
            st.session_state.gender = "male"
            st.session_state.age = 35
            st.session_state.height = 175
            st.session_state.weight = 75
            st.session_state.duration = 45.0
            st.session_state.heart_rate = 115
            st.session_state.body_temp = 37.8
            st.info("✅ Sample data loaded! Click Predict below.", icon="ℹ️")

    st.divider()
    
    # Prediction
    col_pred1, col_pred2 = st.columns([1, 3])
    with col_pred1:
        predict_button = st.button("🎯 Predict Calories", type="primary", use_container_width=True, key="predict")
    
    if predict_button:
        # Convert gender to numeric (male=1, female=0)
        gender_encoded = 1 if gender == "male" else 0
        
        # Create feature array
        input_features = np.array([[gender_encoded, age, height, weight, duration, heart_rate, body_temp]])
        
        # Make prediction
        prediction = model.predict(input_features)[0]
        
        # Display result
        with col_pred2:
            st.success(f"✨ **Predicted Calories Burnt: {prediction:.2f} kcal**")
        
        # Create visualization showing input impact
        st.subheader("📈 Prediction Insights")
        
        viz_col1, viz_col2 = st.columns(2)
        
        with viz_col1:
            # Feature importance chart
            fig_importance = px.bar(
                x=feature_importances,
                y=feature_names,
                orientation='h',
                title='Feature Importance in Model',
                labels={'x': 'Importance Score', 'y': 'Feature'},
                color=feature_importances,
                color_continuous_scale='Viridis'
            )
            fig_importance.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig_importance, use_container_width=True)
        
        with viz_col2:
            # Summary of inputs
            summary_data = {
                "Feature": feature_names,
                "Value": [
                    gender.upper(),
                    f"{age} years",
                    f"{height} cm",
                    f"{weight} kg",
                    f"{duration} min",
                    f"{heart_rate} bpm",
                    f"{body_temp}°C"
                ]
            }
            df_summary = pd.DataFrame(summary_data)
            st.dataframe(df_summary, use_container_width=True, hide_index=True)
        
        # Show how each feature affects prediction
        st.subheader("🔍 Feature Impact Analysis")
        impact_data = []
        for i, (feat_name, feat_value) in enumerate(zip(feature_names, 
                                                          [gender_encoded, age, height, weight, duration, heart_rate, body_temp])):
            impact_score = (feature_importances[i] * 100)
            impact_data.append({
                "Feature": feat_name,
                "Your Value": str(feat_value),
                "Impact %": f"{impact_score:.2f}%"
            })
        
        df_impact = pd.DataFrame(impact_data)
        st.dataframe(df_impact, use_container_width=True, hide_index=True)


# ==================== MODEL INFO PAGE ====================
elif page == "ℹ️ Model Info":
    st.title("ℹ️ Model Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Model Details")
        st.info("""
        **Model Type:** XGBoost Regressor
        
        **Purpose:** Predict calories burnt during exercise based on personal and exercise metrics
        
        **Target Variable:** Calories (continuous)
        
        **Input Features:** 7
        - Gender (categorical)
        - Age (numeric)
        - Height (numeric)
        - Weight (numeric)
        - Exercise Duration (numeric)
        - Heart Rate (numeric)
        - Body Temperature (numeric)
        """)
    
    with col2:
        st.subheader("Feature Importance")
        importance_df = pd.DataFrame({
            'Feature': feature_names,
            'Importance': feature_importances,
            'Importance %': [f"{imp*100:.2f}%" for imp in feature_importances]
        }).sort_values('Importance', ascending=True)
        
        fig = px.bar(importance_df, x='Importance', y='Feature',orientation='h', 
                     color='Importance', color_continuous_scale='Blues',
                     title='Model Feature Importance Ranking')
        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    st.subheader("📝 Input Feature Ranges")
    ranges_info = {
        'Gender': 'male, female',
        'Age': '18-80 years (typical)',
        'Height': '150-220 cm',
        'Weight': '40-150 kg',
        'Duration': '5-200 minutes',
        'Heart Rate': '60-200 bpm',
        'Body Temperature': '36.0-40.0°C'
    }
    
    ranges_df = pd.DataFrame(list(ranges_info.items()), columns=['Feature', 'Recommended Range'])
    st.dataframe(ranges_df, use_container_width=True, hide_index=True)
    
    st.subheader("💡 Tips for Better Predictions")
    st.markdown("""
    - **Duration** is the most important feature (89.9% importance) - the model heavily weighs exercise duration
    - **Heart Rate** (4.6%) and **Gender** (2.7%) are also moderately important
    - Ensure all input values are within reasonable ranges for your body metrics
    - The model works best with data similar to the training dataset
    """)
