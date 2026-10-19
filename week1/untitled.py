# 1. IMPORT ALL THE TOOLS WE LEARNED TODAY
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# ==========================================
# STEP 1: NUMPY - Generate the Raw Data
# ==========================================
np.random.seed(42) # Keeps random numbers consistent
# Generate 100 random study hours between 1 and 10
study_hours = np.random.uniform(1, 10, 100)
# Generate scores based on hours, adding a little random noise
scores = (study_hours * 8.5) + 15 + np.random.normal(0, 5, 100)

# ==========================================
# STEP 2: PANDAS - Organize and Clean Data
# ==========================================
# Turn the raw NumPy arrays into a beautiful, labeled table (DataFrame)
df = pd.DataFrame({
    'Study_Hours': study_hours,
    'Exam_Score': scores
})

print("--- Pandas DataFrame Preview ---")
print(df.head()) # Shows the first 5 rows
print("\n--- Pandas Quick Statistics ---")
print(df.describe()) # Automatically calculates mean, median, min, max!

# ==========================================
# STEP 3: SCIKIT-LEARN - Train a Machine Learning Model
# ==========================================
# Format the data for Machine Learning (X must be a 2D grid/DataFrame, y is a 1D target)
X = df[['Study_Hours']]
y = df['Exam_Score']

# Split data: 80% for training the model, 20% to test if it's accurate
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train our Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Use our trained model to predict scores for the test set
predictions = model.predict(X_test)
print(f"\nModel Trained! Accuracy (R2 Score): {model.score(X_test, y_test):.2f}")

# ==========================================
# STEP 4: SEABORN & MATPLOTLIB - Visualization
# ==========================================
# Set a beautiful visual style using Seaborn
sns.set_theme(style="darkgrid")

# Create a figure outline using Matplotlib (Width: 8 inches, Height: 5 inches)
plt.figure(figsize=(8, 5))

# Use Seaborn to plot the raw data points as a scatter plot
sns.scatterplot(data=df, x='Study_Hours', y='Exam_Score', color='blue', label='Actual Student Data')

# Use Matplotlib to overlay our Scikit-learn machine learning prediction line
plt.plot(X_test, predictions, color='red', linewidth=2.5, label='Machine Learning Prediction')

# Fine-tune layout details using Matplotlib
plt.title('How Study Hours Predict Exam Scores', fontsize=14, fontweight='bold')
plt.xlabel('Hours Spent Studying', fontsize=12)
plt.ylabel('Final Exam Score', fontsize=12)
plt.legend() # Displays the labels we defined above

# Render the final chart
plt.show()
