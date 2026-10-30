# Week 1 Assessment: Employee Data Analysis 

## Overview

This project analyzes employee data using Python, Pandas, NumPy, and Matplotlib. It demonstrates data exploration, department-level aggregation, filtering, and performance measurement using a Jupyter Notebook.

## Project Structure

```text
week1-assessment/
├── data/
│   └── employees.csv
├── notebooks/
│   └── employee_analysis.ipynb
├── reports/
├── src/
│   └── employee_analysis.py
├── README.md
└── .gitignore
```

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   cd week1-assessment
   ```
2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```
3. Activate it on Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
4. Install the dependencies:

   ```bash
   pip install pandas numpy matplotlib jupyter nbconvert
   ```
5. Launch Jupyter Notebook:

   ```bash
   jupyter notebook
   ```
6. Open `notebooks/employee_analysis.ipynb` and run the cells.

## Terminal Commands

Search for employees located in Chennai:

```bash
grep "Chennai" data/employees.csv
```

Export the notebook to Python:

```bash
jupyter nbconvert --to script notebooks/employee_analysis.ipynb --output employee_analysis --output-dir src
```

## Five-Line Summary of Findings

1. The dataset contains eight employees across four departments.
2. The IT department has the highest headcount, with three employees.
3. Sales and HR each have two employees, while Finance has one.
4. Four employees are located in Chennai.
5. The analysis uses Pandas to explore employee data and calculate department-level statistics.

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Git and GitHub
