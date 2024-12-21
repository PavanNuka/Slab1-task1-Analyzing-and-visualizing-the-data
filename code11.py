import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a Pandas DataFrame
# Replace 'your_file.csv' with the path to your CSV file
data = pd.read_csv('example_dataset.csv')

# Display the first few rows of the DataFrame
print("\nFirst 5 rows of the data:")
print(data.head())

# Perform basic data analysis
# Example: Calculate the average of a selected column (replace 'column_name' with an actual column name)
column_name = 'column_name'
if column_name in data.columns:
    average_value = data[column_name].mean()
    print(f"\nAverage of {column_name}: {average_value}")
else:
    print(f"\nColumn '{column_name}' not found in the dataset.")

# Generate visualizations
# 1. Bar chart
if column_name in data.columns:
    plt.figure(figsize=(10, 6))
    data[column_name].value_counts().plot(kind='bar')
    plt.title(f"Bar Chart of {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Count")
    plt.show()

# 2. Scatter plot (replace 'x_column' and 'y_column' with actual column names)
x_column = 'x_column'
y_column = 'y_column'
if x_column in data.columns and y_column in data.columns:
    plt.figure(figsize=(10, 6))
    plt.scatter(data[x_column], data[y_column], alpha=0.5)
    plt.title(f"Scatter Plot of {x_column} vs {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()
else:
    print(f"\nColumns '{x_column}' or '{y_column}' not found in the dataset.")

# 3. Heatmap (correlation matrix)
plt.figure(figsize=(10, 6))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Heatmap of Correlation Matrix")
plt.show()

# Insights and observations (Replace this section with analysis based on the generated outputs)
# Example:
# 1. Identify patterns in the bar chart: e.g., which category is most/least frequent?
# 2. Analyze relationships in the scatter plot: e.g., is there a positive or negative correlation?
# 3. Insights from the heatmap: e.g., which columns have strong correlations?
