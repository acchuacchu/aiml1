import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the "mpg" dataset from Seaborn
mpg_data = pd.read_csv("C:/Users/SPTINT-13/Desktop/dataset/auto-mpg.csv")

# Create a box plot and whisker plot
sns.boxplot(x=mpg_data["mpg"])

# Set plot title and labels
plt.title("Box Plot of MPG")
plt.xlabel("Miles per Gallon")

# Show the plot
plt.show()

# Calculate the five-number summary
five_num_summary = mpg_data["mpg"].describe()

# Print the five-number summary
print("Five-Number Summary:")
print(five_num_summary)
