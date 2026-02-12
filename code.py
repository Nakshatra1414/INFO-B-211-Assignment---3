import pandas as pd
import numpy as np

# A
sepal_df = pd.read_csv('Sepal_Data.csv')
petal_df = pd.read_csv('Petal_Data.csv')


# Merge on sample_id and species
iris_df = pd.merge(sepal_df, petal_df, on=['sample_id', 'species'])

# Keep only required columns
iris_df = iris_df[['sample_id', 'species',
                   'sepal_length', 'sepal_width',
                   'petal_length', 'petal_width']]

print("Combined Iris DataFrame:\n")
print(iris_df.head(), "\n")

# B

numerical_vars = ['sepal_length', 'sepal_width',
                  'petal_length', 'petal_width']

correlations = iris_df[numerical_vars].corr()
print("Correlation matrix:\n")
print(correlations, "\n")

# C 
averages = iris_df.groupby('species')[numerical_vars].mean()
print("Average measurements per species:\n")
print(averages, "\n")

#D

medians = iris_df.groupby('species')[numerical_vars].median()
print("Median measurements per species:\n")
print(medians, "\n")

#E

std_devs = iris_df.groupby('species')[numerical_vars].std()
print("Standard deviation per species:\n")
print(std_devs, "\n")

# -----------------------------
# Step 7: Species similarity (using averages)
# -----------------------------
print("Species similarity analysis:\n")

species_names = averages.index.tolist()

# Convert averages to numpy array
means_array = averages.to_numpy()

# Compute Euclidean distances manually (no scipy)
distance_matrix = np.zeros((len(species_names), len(species_names)))

for i in range(len(species_names)):
    for j in range(len(species_names)):
        distance = np.sqrt(np.sum((means_array[i] - means_array[j])**2))
        distance_matrix[i][j] = distance

# Convert to DataFrame for readability
distance_df = pd.DataFrame(distance_matrix,
                           index=species_names,
                           columns=species_names)

print("Euclidean distance between species (lower = more similar):\n")
print(distance_df, "\n")

# Identify most and least similar species
# Ignore diagonal (distance to itself = 0)
min_dist = float('inf')
max_dist = 0
most_similar = None
least_similar = None

for i in range(len(species_names)):
    for j in range(i + 1, len(species_names)):
        d = distance_matrix[i][j]
        pair = (species_names[i], species_names[j])

        if d < min_dist:
            min_dist = d
            most_similar = pair

        if d > max_dist:
            max_dist = d
            least_similar = pair

print("Most similar species:", most_similar, "Distance:", min_dist)
print("Least similar species:", least_similar, "Distance:", max_dist)

