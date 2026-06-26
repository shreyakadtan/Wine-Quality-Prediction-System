import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


df = pd.read_csv(r"C:\Users\User\Desktop\wine_quality_prediction\WineQuality.csv")


df['quality_label'] = df['quality'].apply(lambda x: 1 if x >= 7 else 0)


X = df.drop(['quality', 'quality_label'], axis=1)
y = df['quality_label']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)


model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)


pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))

print("model.pkl and scaler.pkl created successfully")