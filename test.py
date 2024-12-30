import pandas as pd
import matplotlib.pyplot as plt

# Example data for visualization
results = {
    "Linear Regression": {"MAE": 2.17, "MSE": 7.81, "R2": 0.63},
    "Decision Tree": {"MAE": 2.07, "MSE": 7.41, "R2": 0.65},
    "Random Forest": {"MAE": 1.92, "MSE": 7.13, "R2": 0.66},
}

# Convert results to a DataFrame for visualization
results_df = pd.DataFrame(results).T  # Transpose for easier visualization

# Plotting the results
results_df[["MAE", "MSE", "R2"]].plot(kind="bar", figsize=(10, 6), alpha=0.8)
plt.title("Model Performance Comparison", fontsize=16)
plt.ylabel("Score", fontsize=12)
plt.xlabel("Model", fontsize=12)
plt.xticks(rotation=0)  # Keep model names horizontal
plt.legend(title="Metrics", fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()  # This is essential for rendering the plot in VS Code
