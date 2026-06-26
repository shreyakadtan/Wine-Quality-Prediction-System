# Wine-Quality-Prediction-System 🍷
Machine Learning-based web application that predicts wine quality using physicochemical properties.


Overview:
The Wine Quality Prediction System is a Machine Learning web application that predicts the quality of wine based on its physicochemical properties. The project demonstrates an end-to-end data science workflow including data preprocessing, model training, evaluation, and deployment using Flask.

Features:
Predicts wine quality based on input chemical properties
Data preprocessing and feature scaling
Machine Learning model training and comparison
Web-based user interface using Flask
Real-time prediction system
Technologies Used
Python
Flask
Pandas
NumPy
Scikit-learn
HTML
CSS

Dataset:
The dataset contains physicochemical tests of different wine samples, including features such as:

Acidity levels
Sugar content
Alcohol percentage
pH value
Sulphates
Machine Learning Models Used
Logistic Regression
Random Forest Classifier
Support Vector Machine (SVM)
K-Nearest Neighbors (KNN)

Random Forest performed the best based on accuracy and evaluation metrics.

Project Structure:
Wine-Quality-Prediction-System/
│── app.py
│── model.py
│── requirements.txt
│── dataset.csv
│── templates/
│── static/
│── model.pkl
│── scaler.pkl

Installation:
Clone the repository:
git clone https://github.com/your-username/Wine-Quality-Prediction-System.git
Navigate to the project directory:
cd Wine-Quality-Prediction-System
Install dependencies:
pip install -r requirements.txt
Run the application:
python app.py
Open in browser link
Results

The model predicts wine quality with good accuracy using ensemble learning techniques, making it suitable for educational and demonstration purposes.

Future Improvements:
Integration with deep learning models
Better hyperparameter tuning
Cloud deployment (AWS / Render / Heroku)
Improved UI/UX

Author:
Shreya Kadtan
Developed as a Machine Learning project for academic and portfolio purposes.
