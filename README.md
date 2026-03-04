# 🔥 Calories Burnt Prediction

A machine learning-powered Streamlit application that predicts calories burnt during exercise based on personal fitness metrics and exercise parameters.

## 📋 Features

- **Single Prediction**: Enter personal metrics to get instant calorie predictions
- **Batch Prediction**: Upload CSV files with multiple records for bulk predictions
- **Model Insights**: View feature importance and understand what drives the predictions
- **Sample Data**: Quick test with pre-filled sample data
- **Visualizations**: Interactive charts showing feature importance and prediction distributions
- **Export Results**: Download batch predictions as CSV

## 🎯 Use Cases

- Fitness enthusiasts wanting to estimate calories burnt during workouts
- Personal trainers analyzing workout effectiveness
- Health researchers studying exercise impact
- Gym apps and fitness tracking applications

## 📊 Dataset Features

The model takes 7 input features:

| Feature | Type | Range | Description |
|---------|------|-------|-------------|
| Gender | Categorical | male/female | User's gender |
| Age | Numeric | 18-80+ years | User's age |
| Height | Numeric | 150-220 cm | User's height |
| Weight | Numeric | 40-150+ kg | User's body weight |
| Duration | Numeric | 5-200+ min | Exercise duration |
| Heart Rate | Numeric | 60-200 bpm | Exercise heart rate |
| Body Temperature | Numeric | 36.0-40.0°C | Body temperature during exercise |

**Target Variable**: Calories (continuous, kcal)

## 🤖 Model Information

- **Algorithm**: XGBoost Regressor
- **Feature Importance**: Duration (89.9%) > Heart Rate (4.6%) > Gender (2.7%) > Age (2.2%) > others
- **Training Data**: 15,000+ records from the Calories dataset

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip or conda

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Calories-Burnt-Prediction
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the App

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## 📖 Usage

### Single Prediction
1. Navigate to the **Home** tab
2. Fill in your personal and exercise metrics
3. Click **"Predict Calories"** button
4. View the prediction result and feature analysis

### Batch Prediction
1. Navigate to the **Batch Prediction** tab
2. Prepare a CSV file with columns: `Gender`, `Age`, `Height`, `Weight`, `Duration`, `Heart_Rate`, `Body_Temp`
3. Upload the file
4. Click **"Predict All Records"** to generate predictions
5. View statistics and download results

### Model Information
1. Navigate to the **Model Info** tab
2. View model details, feature importance ranking
3. Check recommended input ranges and tips

## 📁 Project Structure

```
Calories-Burnt-Prediction/
├── app.py                    # Main Streamlit application
├── model.pkl                 # Trained XGBoost model
├── calories.csv              # Dataset (15,000+ records)
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── .gitignore               # Git ignore rules
```

## 🔧 Dependencies

- **streamlit**: Web framework for ML apps
- **xgboost**: Gradient boosting library (model)
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **plotly**: Interactive visualizations

See `requirements.txt` for specific versions.

## 📊 Example CSV Format for Batch Prediction

```csv
Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp
male,30,175,75,30,110,37.5
female,25,165,60,45,120,37.8
male,45,180,85,20,95,37.2
```

## 💡 Tips for Better Predictions

- **Duration is key**: Exercise duration is the most important predictor (89.9% importance)
- **Heart rate matters**: Higher heart rates indicate more intense exercise
- **Accuracy**: Model works best with metrics within typical ranges
- **Data quality**: Ensure accurate measurements for best results

## 📈 Performance Insights

- Duration is the strongest predictor of calories burnt
- Heart rate provides secondary predictive power
- Gender and age have moderate influence
- Height and body temperature have minimal direct impact

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named..."
Install missing dependencies:
```bash
pip install -r requirements.txt
```

### "model.pkl not found"
Ensure the trained model file is in the same directory as `app.py`

### CSV upload errors
Verify your CSV has exactly these columns: `Gender`, `Age`, `Height`, `Weight`, `Duration`, `Heart_Rate`, `Body_Temp`

## 🔐 Model Limitations

- Model trained on specific demographic patterns
- Best predictions within observed data ranges
- Cannot account for unusual exercise conditions
- Individual variation in calorie burn is significant

## 📝 License

This project is provided as-is for educational and portfolio purposes.

## 👨‍💼 About

This application demonstrates:
- Machine Learning model deployment
- Streamlit web app development
- Data visualization with Plotly
- Professional Python development practices
- User-friendly ML interface design

## 🤝 Contributing

Suggestions for improvements:
- Add more features (fitness level, exercise type)
- Integrate with wearable APIs
- Add confidence intervals
- Implement model retraining pipeline
- Add user authentication

## 📧 Contact

For questions or feedback, feel free to reach out or open an issue.

---

**Happy Predicting! 🔥**
