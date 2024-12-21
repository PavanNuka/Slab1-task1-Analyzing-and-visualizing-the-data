import pandas as pd

# Create the dataset
data = {
    "column_name": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    "x_column": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "y_column": [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
    "category": ["A", "B", "A", "C", "B", "C", "A", "B", "C", "A"],
    "value": [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
}

# Save to a CSV file
df = pd.DataFrame(data)
df.to_csv("example_dataset.csv", index=False)
print(df)

print("Dataset saved as 'example_dataset.csv'.")
