from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

script_dir = Path(__file__).resolve().parent
csv_path = script_dir / "students.csv"
image_path = script_dir / "student_marks.png"

if not csv_path.exists():
    sample_data = pd.DataFrame(
        {
            "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"],
            "Marks": [85, 78, 92, 88, 76, 95],
        }
    )
    sample_data.to_csv(csv_path, index=False)

# Load the CSV file
data = pd.read_csv(csv_path)

# Display the dataset
print("Student Dataset")
print(data)

# Display Summary Statistics
print("\nSummary Statistics")
print("---------------------")
print("Mean Marks :", data["Marks"].mean())
print("Maximum Marks :", data["Marks"].max())
print("Minimum Marks :", data["Marks"].min())
print("Total Students :", data["Marks"].count())
print("Median Marks :", data["Marks"].median())
print("Standard Deviation :", data["Marks"].std())

# Create Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(data["Name"], data["Marks"], color="skyblue")
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig(image_path, dpi=300)
print(f"\nSaved chart to {image_path}")
