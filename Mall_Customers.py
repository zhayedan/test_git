# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Step 1: Load dataset
data = pd.read_csv("Mall_Customers.csv")

# Step 2: Data Preprocessing
# Remove outliers using the IQR method for "Annual Income (k$)"
Q1 = data["Annual Income (k$)"].quantile(0.25)
Q3 = data["Annual Income (k$)"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
data_filtered = data[(data["Annual Income (k$)"] >= lower_bound) & (data["Annual Income (k$)"] <= upper_bound)]

# Convert "Gender" to numeric using One-Hot Encoding
data_prepared = pd.get_dummies(data_filtered, columns=["Gender"], drop_first=True)

# Select relevant features and target
features = ["Age", "Annual Income (k$)", "Spending Score (1-100)", "Gender_Male"]
target = "Spending Score (1-100)"
X = data_prepared[features]
y = data_prepared[target]

# Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Initialize models
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(random_state=42),
}

# Train and evaluate models
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)  # Train the model
    predictions = model.predict(X_test)  # Make predictions
    results[name] = {
        "MAE": mean_absolute_error(y_test, predictions),
        "MSE": mean_squared_error(y_test, predictions),
        "R2": r2_score(y_test, predictions),
    }

# Step 5: Display results as a DataFrame
results_df = pd.DataFrame(results).T
print("Model Performance Comparison:")
print(results_df)

# Step 6: Visualize results
results_df[["MAE", "MSE", "R2"]].plot(kind="bar", figsize=(10, 6), alpha=0.8)
plt.title("Model Performance Comparison", fontsize=16)
plt.ylabel("Scores", fontsize=12)
plt.xlabel("Models", fontsize=12)
plt.xticks(rotation=0)
plt.legend(title="Metrics", fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
