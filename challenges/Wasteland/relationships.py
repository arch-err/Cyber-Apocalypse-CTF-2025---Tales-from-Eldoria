#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the data
df = pd.read_csv("./ml_wasteland/Ashen_Outpost_Records.csv")

# Look at basic statistics
print(df.describe())

# Plot the correlations
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlations")
plt.savefig("correlations.png")
plt.close()

# Analyze relationship between features and reputation
features = ['Dragonfire_Resistance', 'Shadow_Crimes', 'Corruption_Mutations']
X = df[features]
y = df['Reputation']

# Train a simple linear model to understand feature importance
model = LinearRegression()
model.fit(X, y)

# Print coefficients
for feature, coef in zip(features, model.coef_):
    print(f"{feature}: {coef}")
