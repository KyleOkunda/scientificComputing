
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris


# Task 1: Load and Explore the Dataset

try:
    # Load iris dataset from sklearn
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)
    
    print("✅ Dataset successfully loaded!\n")
    
    # Display first few rows
    print("First 5 rows of the dataset:")
    print(df.head(), "\n")
    
    # Check data types and missing values
    print("Dataset Info:")
    print(df.info(), "\n")
    
    print("Missing Values per column:")
    print(df.isnull().sum(), "\n")
    
    # Clean dataset: drop or fill missing values
    df = df.dropna()  
    
except FileNotFoundError:
    print("❌ Error: Dataset file not found.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")


# Task 2: Basic Data Analysis

print("Descriptive Statistics for Numerical Columns:")
print(df.describe(), "\n")

# Grouping by species and computing mean
species_means = df.groupby("species").mean(numeric_only=True)
print("Mean values per species:")
print(species_means, "\n")

# Observations
print("Observations:")
print("- Setosa flowers tend to have the smallest petal and sepal sizes.")
print("- Virginica has the largest petal length and width.")
print("- Versicolor lies in between Setosa and Virginica in most dimensions.\n")


# Task 3: Data Visualization


sns.set(style="whitegrid", palette="muted", font_scale=1.1)

# 1. Line chart (simulate a time trend using index as time for petal length)
plt.figure(figsize=(8, 5))
plt.plot(df.index, df["petal length (cm)"], label="Petal Length", color="blue")
plt.title("Line Chart of Petal Length over Index (simulated time)")
plt.xlabel("Index (as time)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart: Average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(x="species", y="petal length (cm)", data=df, estimator=np.mean)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram of sepal length
plt.figure(figsize=(8, 5))
plt.hist(df["sepal length (cm)"], bins=20, color="green", alpha=0.7)
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot: Sepal length vs Petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, s=70)
plt.title("Scatter Plot of Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
