# INFO-B-211-Assignment---3
# Iris Data Analysis Project – ReadMe

## Purpose of the Project

The purpose of this project is to analyze the physical measurements of three iris species—setosa, versicolor, and virginica—using Fisher’s Iris dataset. The project combines separate sepal and petal datasets into a single DataFrame and performs statistical analysis to understand relationships between variables and similarities among species.

The analysis includes:

* Correlation between variables
* Mean (average) measurements per species
* Median measurements per species
* Standard deviation per species
* Species similarity analysis using Euclidean distance

---

## Data Description

The combined dataset contains the following attributes:

* **sample_id**: Unique identifier for each iris sample
* **species**: Iris species (setosa, versicolor, virginica)
* **sepal_length**: Length of the sepal (numeric)
* **sepal_width**: Width of the sepal (numeric)
* **petal_length**: Length of the petal (numeric)
* **petal_width**: Width of the petal (numeric)

The data was originally provided in two separate files:

* `sepal_data.csv` (sepal measurements)
* `petal_data.csv` (petal measurements)

These were merged using the common attributes **sample_id** and **species**.

---

## Class Design and Implementation

This project uses the **pandas DataFrame** as the primary data structure instead of creating custom classes. The DataFrame acts as the main container for storing and manipulating the iris measurements.

### Attributes (DataFrame Columns)

* `sample_id`: Unique sample identifier
* `species`: Iris species label
* `sepal_length`: Sepal length measurement
* `sepal_width`: Sepal width measurement
* `petal_length`: Petal length measurement
* `petal_width`: Petal width measurement

### Methods Used

The following pandas and numpy methods were used:

* **pd.read_csv()**

  * Loads the sepal and petal datasets.

* **pd.merge()**

  * Combines the sepal and petal datasets into one DataFrame using `sample_id` and `species`.

* **DataFrame.corr()**

  * Calculates the correlation between numerical variables.

* **DataFrame.groupby().mean()**

  * Calculates the average measurements per species.

* **DataFrame.groupby().median()**

  * Calculates the median measurements per species.

* **DataFrame.groupby().std()**

  * Calculates the standard deviation per species.

* **NumPy operations**

  * Used to manually compute Euclidean distances between species based on their average measurements.

---

## Program Workflow

1. Load the sepal and petal datasets.
2. Merge the datasets into a single DataFrame.
3. Compute the correlation matrix.
4. Calculate average, median, and standard deviation per species.
5. Compute Euclidean distances between species using average measurements.
6. Identify the most similar and least similar species.

---

## Key Findings

* **Versicolor and virginica** are the most similar species, with the smallest Euclidean distance (1.429).
* **Setosa and virginica** are the least similar species, with the largest Euclidean distance (4.581).
* The main difference comes from **petal length and width**, which vary significantly between setosa and the other species.

---

## Limitations

* The analysis is based only on four physical measurements.
* No visualization or advanced statistical modeling was included.
* Euclidean distance uses only average values, which may hide variation within species.
* External libraries such as SciPy were not used, as per assignment requirements.

---

## Requirements

This project uses only:

* Standard Python modules
* pandas
* numpy

Install required packages if needed:

```
pip install pandas numpy
```

---

## How to Run the Program

1. Place the following files in the same folder:

   * `sepal_data.csv`
   * `petal_data.csv`
   * `iris_analysis.py` (your script)
2. Run the script:

```
python iris_analysis.py
```

The program will display all statistical results and species similarity analysis in the terminal.
