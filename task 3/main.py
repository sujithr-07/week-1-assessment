import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("outputs", exist_ok=True)


print("\n--------- NUMPY ARRAY OPERATIONS ---------")

#marks of 4 students in 3 subjects
marks = np.array([[85, 90, 78],
                  [92, 88, 95],
                  [76, 85, 80],
                  [89, 92, 84]
                ])

print("marks array:\n", marks)

print("\nShape", marks.shape)

#average marks of each student
student_avg = np.mean(marks, axis=1)
print("\nStudent Average marks:\n", student_avg)

#average marks of each subject
subject_avg = np.mean(marks, axis=0)
print("\nSubject Average marks:\n", subject_avg)

#add 5 grace marks using broadcasting
marks_with_bonus = marks + 5
print("\nMarks with bonus:\n", marks_with_bonus)

#weighted scores using np.dot
weights = np.array([0.3, 0.4, 0.3])
weighted_scores = np.dot(marks_with_bonus, weights)
print("\nWeighted scores:\n", weighted_scores)


print("\n--------- PANDAS DATAFRAME OPERATIONS ---------")

df=pd.read_csv("employees.csv")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataframe Info:")
print(df.info())

print("\nDataframe Description:")
print(df.describe())

#loc
print("\nusing loc:")
print(df.loc[0:2, ['Name', 'Department', 'Salary']])

#iloc
print("\nusing iloc:")
print(df.iloc[0:3, [0, 1, 2]])

#filtering
print("\nEmployees with Salary > 50000:")
print(df[df['Salary'] > 50000])


print("\n--------- DATA CLEANING ---------")

print("original dataframe:\n", len(df))

#count missing salaries
print("\nMissing salaries:", df['Salary'].isna().sum())

#count duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

#remove duplicates
df=df.drop_duplicates().copy()

#corrrect data types
df["id"] = pd.to_numeric(df["id"], errors="raise").astype(int)
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

#fill missing salaries with median
median_salary = df['Salary'].median()
df['Salary'] = df['Salary'].fillna(median_salary)

#standardize text columns
df['Name'] = df['Name'].str.strip().str.title()
df['Department'] = df['Department'].str.strip().str.title()
df["city"] = df["city"].str.strip().str.title()

#ensure salary is numeric
df["salary"] = df["Salary"].astype(float)

print("median salary used:", median_salary)\
print("\ncleaned dataframe:\n", len(df))
print("\nMissing salaries after cleaning:", df['Salary'].isna().sum())

print("\ncleaned employee data:")
print(df)



