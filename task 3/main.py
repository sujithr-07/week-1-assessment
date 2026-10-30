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

print("median salary used:", median_salary)
print("\ncleaned dataframe:\n", len(df))
print("\nMissing salaries after cleaning:", df['Salary'].isna().sum())

print("\ncleaned employee data:")
print(df)



print("\n---------- DEPARTMENT AGGREGATION ----------")

department_summary = (
    df.groupby("department")
      .agg(
          headcount=("id", "count"),
          average_salary=("salary", "mean"),
          maximum_salary=("salary", "max")
      )
      .reset_index()
)

print(department_summary)

print("\nHeadcount:")
for _, row in department_summary.iterrows():
    print(f"{row['department']}: {row['headcount']}")


print("\n---------- DATA MERGING ----------")

departments = pd.read_csv("departments.csv")

# Correct department text
departments["department"] = (
    departments["department"].str.strip().str.title()
)

# INNER JOIN
inner_join = pd.merge(
    df,
    departments,
    on="department",
    how="inner"
)

print("\nINNER JOIN:")
print(inner_join[["name", "department", "head", "budget"]])

# LEFT JOIN
left_join = pd.merge(
    df,
    departments,
    on="department",
    how="left"
)

print("\nLEFT JOIN:")
print(left_join[["name", "department", "head", "budget"]])

# OUTER JOIN
outer_join = pd.merge(
    department_summary,
    departments,
    on="department",
    how="outer",
    indicator=True
)

print("\nOUTER JOIN:")
print(outer_join)

# Departments without employees
departments_without_employees = outer_join.loc[
    outer_join["_merge"] == "right_only",
    "department"
].tolist()

print("\nDepartments with no employees:",
      departments_without_employees)


print("\n========== CHARTS AND INSIGHTS ==========")

# BAR CHART
# Average salary by department
plt.figure(figsize=(8, 5))

plt.bar(
    department_summary["department"],
    department_summary["average_salary"],
    label="Average Salary"
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/bar_chart.png")
plt.close()

print("Bar chart insight: The chart compares average salaries "
      "across departments.")

# HISTOGRAM
# Salary distribution
plt.figure(figsize=(8, 5))

plt.hist(
    df["salary"],
    bins=5,
    edgecolor="black",
    label="Employee Salaries"
)

plt.title("Distribution of Employee Salaries")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/histogram.png")
plt.close()

print("Histogram insight: The chart shows how employee salaries "
      "are distributed across salary ranges.")

# SCATTER PLOT
# Salary vs Employee ID

plt.figure(figsize=(8, 5))

plt.scatter(
    df["id"],
    df["salary"], 
    label="Employees"
)

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/scatter_plot.png")
plt.close()

print("Scatter plot insight: The chart compares individual "
      "employee salaries without assuming that employee ID "
      "causes salary differences.")


plt.figure(figsize=(8, 5))

plt.plot(
    department_summary["department"],
    department_summary["average_salary"],
    marker="o",
    label="Average Salary"
)


#LINE CHART
# Average salary by department
plt.title("Average Salary Trend Across Departments")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/line_chart.png")
plt.close()

print("Line chart insight: The line connects department average "
      "salaries to make differences between departments visible.")


print("\nAll tasks completed successfully!")
print("Charts saved in the outputs folder.")