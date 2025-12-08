"""
Module: Pandas and Data Analysis
Description: Comprehensive guide to data analysis with Pandas

This module covers:
- Pandas basics (Series and DataFrame)
- Reading and writing data files
- Data inspection and exploration
- Data selection and filtering
- Data manipulation and transformation
- Grouping and aggregation
- Handling missing data
- Data visualization basics

Note: Run 'pip install pandas numpy' before using this module
"""

try:
    import pandas as pd
    import numpy as np
    from pathlib import Path
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    print("Warning: pandas and/or numpy not installed.")
    print("Install with: pip install pandas numpy")


def demonstrate_series():
    """
    Demonstrates Pandas Series - one-dimensional labeled array.
    """
    if not PANDAS_AVAILABLE:
        return
    
    print("=== Pandas Series ===")
    
    # Create Series from list
    numbers = pd.Series([10, 20, 30, 40, 50])
    print("Series from list:")
    print(numbers)
    
    # Series with custom index
    prices = pd.Series([99.99, 149.99, 199.99], 
                      index=['Product A', 'Product B', 'Product C'])
    print("\nSeries with custom index:")
    print(prices)
    
    # Series from dictionary
    population = pd.Series({
        'New York': 8336817,
        'Los Angeles': 3979576,
        'Chicago': 2693976
    })
    print("\nSeries from dictionary:")
    print(population)
    
    # Series operations
    print("\nSeries operations:")
    print(f"  Mean: {numbers.mean()}")
    print(f"  Sum: {numbers.sum()}")
    print(f"  Max: {numbers.max()}")
    print(f"  Std: {numbers.std():.2f}")
    
    print()


def demonstrate_dataframe():
    """
    Demonstrates Pandas DataFrame - two-dimensional labeled data structure.
    """
    if not PANDAS_AVAILABLE:
        return
    
    print("=== Pandas DataFrame ===")
    
    # Create DataFrame from dictionary
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Boston'],
        'Salary': [70000, 80000, 75000, 85000]
    }
    df = pd.DataFrame(data)
    
    print("DataFrame from dictionary:")
    print(df)
    
    # DataFrame properties
    print("\nDataFrame properties:")
    print(f"  Shape: {df.shape}")
    print(f"  Columns: {list(df.columns)}")
    print(f"  Index: {list(df.index)}")
    print(f"  Data types:\n{df.dtypes}")
    
    print()


def demonstrate_data_inspection():
    """
    Demonstrates data inspection and exploration methods.
    """
    if not PANDAS_AVAILABLE:
        return
    
    print("=== Data Inspection ===")
    
    # Create sample DataFrame
    np.random.seed(42)
    df = pd.DataFrame({
        'A': np.random.randint(1, 100, 10),
        'B': np.random.randint(1, 100, 10),
        'C': np.random.randn(10),
        'D': ['X', 'Y', 'X', 'Z', 'Y', 'X', 'Z', 'Y', 'X', 'Z']
    })
    
    print("Sample data:")
    print(df)
    
    # Inspection methods
    print("\nFirst 3 rows:")
    print(df.head(3))
    
    print("\nLast 3 rows:")
    print(df.tail(3))
    
    print("\nInfo:")
    print(df.info())
    
    print("\nStatistical description:")
    print(df.describe())
    
    print("\nValue counts for column D:")
    print(df['D'].value_counts())
    
    print()


def demonstrate_data_selection():
    """
    Demonstrates data selection and indexing.
    """
    if not PANDAS_AVAILABLE:
        return
    
    print("=== Data Selection ===")
    
    # Create sample DataFrame
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'Age': [25, 30, 35, 28, 32],
        'Department': ['HR', 'IT', 'IT', 'Sales', 'HR'],
        'Salary': [70000, 80000, 75000, 85000, 72000]
    })
    
    print("Original DataFrame:")
    print(df)
    
    # Select single column
    print("\nSelect 'Name' column:")
    print(df['Name'])
    
    # Select multiple columns
    print("\nSelect multiple columns:")
    print(df[['Name', 'Salary']])
    
    # Select rows by index
    print("\nSelect row at index 1:")
    print(df.iloc[1])
    
    # Select rows by condition
    print("\nSelect IT department:")
    print(df[df['Department'] == 'IT'])
    
    # Multiple conditions
    print("\nAge > 28 AND Salary > 75000:")
    print(df[(df['Age'] > 28) & (df['Salary'] > 75000)])
    
    # Using loc and iloc
    print("\nUsing loc (label-based):")
    print(df.loc[0:2, ['Name', 'Age']])
    
    print("\nUsing iloc (position-based):")
    print(df.iloc[0:3, 0:2])
    
    print()


def demonstrate_data_manipulation():
    """
    Demonstrates data manipulation and transformation.
    """
    if not PANDAS_AVAILABLE:
        return
    
    print("=== Data Manipulation ===")
    
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Score1': [85, 90, 78],
        'Score2': [88, 92, 82]
    })
    
    print("Original DataFrame:")
    print(df)
    
    # Add new column
    df['Average'] = (df['Score1'] + df['Score2']) / 2
    print("\nAfter adding Average column:")
    print(df)
    
    # Apply function
    df['Grade'] = df['Average'].apply(lambda x: 'A' if x >= 90 else 'B' if x >= 80 else 'C')
    print("\nAfter adding Grade column:")
    print(df)
    
    # Rename columns
    df_renamed = df.rename(columns={'Score1': 'Test1', 'Score2': 'Test2'})
    print("\nAfter renaming columns:")
    print(df_renamed)
    
    # Drop columns
    df_dropped = df.drop(['Score1', 'Score2'], axis=1)
    print("\nAfter dropping score columns:")
    print(df_dropped)
    
    # Sort values
    df_sorted = df.sort_values('Average', ascending=False)
    print("\nSorted by Average (descending):")
    print(df_sorted)
    
    print()


def demonstrate_grouping_aggregation():
    """
    Demonstrates grouping and aggregation operations.
    """
    if not PANDAS_AVAILABLE:
        return
    
    print("=== Grouping and Aggregation ===")
    
    # Create sample data
    df = pd.DataFrame({
        'Department': ['IT', 'IT', 'HR', 'HR', 'Sales', 'Sales', 'IT'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'George'],
        'Salary': [80000, 85000, 70000, 72000, 75000, 78000, 82000],
        'Years': [3, 5, 2, 4, 3, 6, 4]
    })
    
    print("Original DataFrame:")
    print(df)
    
    # Group by single column
    print("\nAverage salary by department:")
    print(df.groupby('Department')['Salary'].mean())
    
    # Multiple aggregations
    print("\nMultiple aggregations:")
    print(df.groupby('Department').agg({
        'Salary': ['mean', 'min', 'max'],
        'Years': 'mean'
    }))
    
    # Count by group
    print("\nEmployee count by department:")
    print(df.groupby('Department').size())
    
    # Custom aggregation
    print("\nSalary range by department:")
    print(df.groupby('Department')['Salary'].agg(lambda x: x.max() - x.min()))
    
    print()


def demonstrate_missing_data():
    """
    Demonstrates handling missing data.
    """
    if not PANDAS_AVAILABLE:
        return
    
    print("=== Handling Missing Data ===")
    
    # Create DataFrame with missing values
    df = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 2, 3, np.nan, 5],
        'C': [1, 2, 3, 4, 5]
    })
    
    print("DataFrame with missing values:")
    print(df)
    
    # Check for missing values
    print("\nMissing values per column:")
    print(df.isnull().sum())
    
    # Drop rows with any missing values
    print("\nDrop rows with any NaN:")
    print(df.dropna())
    
    # Drop columns with any missing values
    print("\nDrop columns with any NaN:")
    print(df.dropna(axis=1))
    
    # Fill missing values
    print("\nFill NaN with 0:")
    print(df.fillna(0))
    
    # Fill with mean
    print("\nFill NaN with column mean:")
    print(df.fillna(df.mean()))
    
    # Forward fill
    print("\nForward fill:")
    print(df.fillna(method='ffill'))
    
    print()


def demonstrate_reading_writing():
    """
    Demonstrates reading and writing data files.
    """
    if not PANDAS_AVAILABLE:
        return
    
    print("=== Reading and Writing Files ===")
    
    # Ensure data directory exists
    Path("../data").mkdir(exist_ok=True)
    
    # Create sample DataFrame
    df = pd.DataFrame({
        'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
        'Price': [999.99, 29.99, 79.99, 349.99],
        'Stock': [15, 50, 30, 20],
        'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics']
    })
    
    # Write to CSV
    df.to_csv('../data/products_pandas.csv', index=False)
    print("Written to CSV: products_pandas.csv")
    
    # Read from CSV
    df_read = pd.read_csv('../data/products_pandas.csv')
    print("\nRead from CSV:")
    print(df_read)
    
    # Write to Excel (requires openpyxl)
    try:
        df.to_excel('../data/products_pandas.xlsx', index=False)
        print("\nWritten to Excel: products_pandas.xlsx")
    except ImportError:
        print("\nExcel support requires: pip install openpyxl")
    
    # Write to JSON
    df.to_json('../data/products_pandas.json', orient='records', indent=2)
    print("Written to JSON: products_pandas.json")
    
    # Read from JSON
    df_json = pd.read_json('../data/products_pandas.json')
    print("\nRead from JSON:")
    print(df_json)
    
    print()


def demonstrate_merging_joining():
    """
    Demonstrates merging and joining DataFrames.
    """
    if not PANDAS_AVAILABLE:
        return
    
    print("=== Merging and Joining ===")
    
    # Create sample DataFrames
    employees = pd.DataFrame({
        'emp_id': [1, 2, 3, 4],
        'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'dept_id': [10, 20, 10, 30]
    })
    
    departments = pd.DataFrame({
        'dept_id': [10, 20, 30],
        'dept_name': ['Engineering', 'Sales', 'HR']
    })
    
    print("Employees:")
    print(employees)
    print("\nDepartments:")
    print(departments)
    
    # Inner join
    print("\nInner join:")
    merged = pd.merge(employees, departments, on='dept_id')
    print(merged)
    
    # Left join
    print("\nLeft join:")
    all_employees = pd.merge(employees, departments, on='dept_id', how='left')
    print(all_employees)
    
    # Concatenate vertically
    print("\nConcatenate DataFrames:")
    df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
    concatenated = pd.concat([df1, df2], ignore_index=True)
    print(concatenated)
    
    print()


# EXERCISES
def exercise_1():
    """
    Exercise 1: Sales Data Analysis
    
    TODO: Analyze sales data:
    - Create DataFrame with sales data
    - Calculate total sales per product
    - Find best and worst performing products
    - Calculate average sale amount
    """
    if not PANDAS_AVAILABLE:
        return
    
    print("=== Exercise 1: Sales Analysis ===")
    
    # Create sales data
    sales_data = {
        'Date': pd.date_range('2025-01-01', periods=10),
        'Product': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Mouse', 
                   'Monitor', 'Laptop', 'Keyboard', 'Monitor', 'Mouse'],
        'Quantity': [2, 5, 1, 3, 8, 1, 2, 4, 2, 6],
        'Price': [999.99, 29.99, 999.99, 79.99, 29.99, 
                 349.99, 999.99, 79.99, 349.99, 29.99]
    }
    
    df = pd.DataFrame(sales_data)
    df['Total'] = df['Quantity'] * df['Price']
    
    print("Sales data:")
    print(df)
    
    # Total sales per product
    print("\nTotal sales by product:")
    product_sales = df.groupby('Product')['Total'].sum().sort_values(ascending=False)
    print(product_sales)
    
    # Best and worst
    print(f"\nBest seller: {product_sales.idxmax()} (${product_sales.max():.2f})")
    print(f"Worst seller: {product_sales.idxmin()} (${product_sales.min():.2f})")
    
    # Average sale
    print(f"\nAverage sale amount: ${df['Total'].mean():.2f}")
    
    print()


def exercise_2():
    """
    Exercise 2: Student Grade Analysis
    
    TODO: Analyze student grades:
    - Load or create student data
    - Calculate average grades
    - Identify top performers
    - Calculate grade distribution
    """
    if not PANDAS_AVAILABLE:
        return
    
    print("=== Exercise 2: Grade Analysis ===")
    
    # Create student data
    students = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
        'Math': [85, 92, 78, 95, 88, 82],
        'Science': [88, 89, 82, 93, 90, 85],
        'English': [92, 87, 88, 91, 85, 89]
    })
    
    print("Student grades:")
    print(students)
    
    # Calculate average
    students['Average'] = students[['Math', 'Science', 'English']].mean(axis=1)
    print("\nWith averages:")
    print(students[['Name', 'Average']])
    
    # Top 3 students
    print("\nTop 3 students:")
    top_3 = students.nlargest(3, 'Average')[['Name', 'Average']]
    print(top_3)
    
    # Grade distribution
    def get_grade(avg):
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        else:
            return 'D'
    
    students['Grade'] = students['Average'].apply(get_grade)
    print("\nGrade distribution:")
    print(students['Grade'].value_counts().sort_index())
    
    print()


def exercise_3():
    """
    Exercise 3: Data Cleaning
    
    TODO: Clean messy data:
    - Handle missing values
    - Remove duplicates
    - Fix data types
    - Standardize values
    """
    if not PANDAS_AVAILABLE:
        return
    
    print("=== Exercise 3: Data Cleaning ===")
    
    # Create messy data
    messy_data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Bob', 'Diana', None, 'Eve'],
        'Age': [25, 30, '35', 30, 28, 32, 27],
        'City': ['New York', 'LA', 'chicago', 'LA', 'BOSTON', 'Seattle', 'Miami'],
        'Salary': [70000, 80000, None, 80000, 85000, 72000, 75000]
    }
    
    df = pd.DataFrame(messy_data)
    print("Messy data:")
    print(df)
    print(f"Shape: {df.shape}")
    
    # Remove duplicates
    df = df.drop_duplicates()
    print(f"\nAfter removing duplicates: {df.shape}")
    
    # Handle missing values
    df = df.dropna(subset=['Name'])
    df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
    print(f"After handling missing values: {df.shape}")
    
    # Fix data types
    df['Age'] = pd.to_numeric(df['Age'])
    
    # Standardize cities
    df['City'] = df['City'].str.title()
    
    print("\nCleaned data:")
    print(df)
    
    print()


def exercise_4():
    """
    Exercise 4: Time Series Analysis
    
    TODO: Analyze time series data:
    - Create date-indexed DataFrame
    - Calculate rolling averages
    - Find trends
    - Resample data
    """
    if not PANDAS_AVAILABLE:
        return
    
    print("=== Exercise 4: Time Series Analysis ===")
    
    # Create time series data
    dates = pd.date_range('2025-01-01', periods=30, freq='D')
    np.random.seed(42)
    values = np.random.randint(100, 200, size=30) + np.arange(30) * 2
    
    df = pd.DataFrame({
        'Date': dates,
        'Sales': values
    })
    df.set_index('Date', inplace=True)
    
    print("Sales data (first 10 days):")
    print(df.head(10))
    
    # Rolling average
    df['Rolling_Avg_7'] = df['Sales'].rolling(window=7).mean()
    print("\nWith 7-day rolling average (last 10 days):")
    print(df.tail(10))
    
    # Weekly resampling
    weekly = df.resample('W').sum()
    print("\nWeekly totals:")
    print(weekly)
    
    # Trend
    trend = df['Sales'].iloc[-7:].mean() - df['Sales'].iloc[:7].mean()
    print(f"\nTrend (last week vs first week): {'+' if trend > 0 else ''}{trend:.2f}")
    
    print()


def exercise_5():
    """
    Exercise 5: Data Pivot and Reshape
    
    TODO: Reshape data:
    - Create pivot tables
    - Melt wide data to long format
    - Cross-tabulations
    - Multi-level indexing
    """
    if not PANDAS_AVAILABLE:
        return
    
    print("=== Exercise 5: Pivot and Reshape ===")
    
    # Create sample data
    data = {
        'Date': ['2025-01-01', '2025-01-01', '2025-01-02', '2025-01-02'],
        'Product': ['A', 'B', 'A', 'B'],
        'Region': ['East', 'East', 'West', 'West'],
        'Sales': [100, 150, 120, 180]
    }
    
    df = pd.DataFrame(data)
    print("Original data:")
    print(df)
    
    # Pivot table
    print("\nPivot table (Product vs Region):")
    pivot = df.pivot_table(values='Sales', index='Product', columns='Region', aggfunc='sum')
    print(pivot)
    
    # Melt (wide to long)
    print("\nMelted pivot table:")
    melted = pivot.reset_index().melt(id_vars='Product', var_name='Region', value_name='Sales')
    print(melted)
    
    # Cross-tabulation
    print("\nCross-tabulation:")
    df['High_Sales'] = df['Sales'] > 140
    crosstab = pd.crosstab(df['Product'], df['High_Sales'])
    print(crosstab)
    
    print()


if __name__ == "__main__":
    """
    Main execution block - runs all demonstrations and exercises.
    """
    if not PANDAS_AVAILABLE:
        print("=" * 60)
        print("ERROR: pandas and/or numpy not installed")
        print("=" * 60)
        print("\nPlease install required packages:")
        print("  pip install pandas numpy")
        print("\nThen run this module again.")
        exit(1)
    
    print("=" * 60)
    print("PANDAS AND DATA ANALYSIS - COMPLETE GUIDE")
    print("=" * 60)
    print()
    
    # Run all demonstrations
    demonstrate_series()
    demonstrate_dataframe()
    demonstrate_data_inspection()
    demonstrate_data_selection()
    demonstrate_data_manipulation()
    demonstrate_grouping_aggregation()
    demonstrate_missing_data()
    demonstrate_reading_writing()
    demonstrate_merging_joining()
    
    # Run all exercises
    print("=" * 60)
    print("EXERCISES")
    print("=" * 60)
    print()
    
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    
    print("=" * 60)
    print("END OF PANDAS MODULE")
    print("=" * 60)
