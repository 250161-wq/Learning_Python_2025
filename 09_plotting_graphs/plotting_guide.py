"""
Module: Plotting Graphs with Matplotlib
Description: Comprehensive guide to data visualization with Matplotlib

This module covers:
- Basic plotting
- Different plot types (line, bar, scatter, pie, histogram)
- Customization (colors, labels, legends, styles)
- Subplots and layouts
- Saving figures
- Integration with Pandas

Note: Run 'pip install matplotlib numpy pandas' before using this module
"""

try:
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from pathlib import Path
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    print("Warning: matplotlib, numpy, and/or pandas not installed.")
    print("Install with: pip install matplotlib numpy pandas")


def demonstrate_basic_plotting():
    """
    Demonstrates basic line plotting.
    """
    if not MATPLOTLIB_AVAILABLE:
        return
    
    print("=== Basic Line Plot ===")
    
    # Create data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title('Sine Wave')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.grid(True)
    
    # Save figure
    Path("../data/plots").mkdir(parents=True, exist_ok=True)
    plt.savefig('../data/plots/basic_line.png', dpi=300, bbox_inches='tight')
    print("  Saved: basic_line.png")
    plt.close()
    
    print()


def demonstrate_multiple_lines():
    """
    Demonstrates plotting multiple lines on the same graph.
    """
    if not MATPLOTLIB_AVAILABLE:
        return
    
    print("=== Multiple Lines ===")
    
    x = np.linspace(0, 10, 100)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, np.sin(x), label='sin(x)', linewidth=2)
    plt.plot(x, np.cos(x), label='cos(x)', linewidth=2, linestyle='--')
    plt.plot(x, np.sin(x) * np.cos(x), label='sin(x)*cos(x)', linewidth=2, linestyle=':')
    
    plt.title('Trigonometric Functions')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.savefig('../data/plots/multiple_lines.png', dpi=300, bbox_inches='tight')
    print("  Saved: multiple_lines.png")
    plt.close()
    
    print()


def demonstrate_bar_chart():
    """
    Demonstrates bar charts.
    """
    if not MATPLOTLIB_AVAILABLE:
        return
    
    print("=== Bar Chart ===")
    
    # Data
    categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    values = [23, 45, 56, 78, 32]
    
    # Create bar chart
    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8'])
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height}',
                ha='center', va='bottom')
    
    plt.title('Sales by Product', fontsize=16, fontweight='bold')
    plt.xlabel('Product', fontsize=12)
    plt.ylabel('Sales', fontsize=12)
    plt.ylim(0, max(values) * 1.1)
    
    plt.savefig('../data/plots/bar_chart.png', dpi=300, bbox_inches='tight')
    print("  Saved: bar_chart.png")
    plt.close()
    
    print()


def demonstrate_horizontal_bar():
    """
    Demonstrates horizontal bar charts.
    """
    if not MATPLOTLIB_AVAILABLE:
        return
    
    print("=== Horizontal Bar Chart ===")
    
    # Data
    languages = ['Python', 'JavaScript', 'Java', 'C++', 'Ruby']
    popularity = [85, 75, 70, 60, 45]
    
    plt.figure(figsize=(10, 6))
    plt.barh(languages, popularity, color='steelblue')
    plt.title('Programming Language Popularity')
    plt.xlabel('Popularity Score')
    plt.ylabel('Language')
    plt.xlim(0, 100)
    
    plt.savefig('../data/plots/horizontal_bar.png', dpi=300, bbox_inches='tight')
    print("  Saved: horizontal_bar.png")
    plt.close()
    
    print()


def demonstrate_scatter_plot():
    """
    Demonstrates scatter plots.
    """
    if not MATPLOTLIB_AVAILABLE:
        return
    
    print("=== Scatter Plot ===")
    
    # Generate random data
    np.random.seed(42)
    x = np.random.randn(100)
    y = 2 * x + np.random.randn(100)
    colors = np.random.rand(100)
    sizes = np.random.randint(20, 200, 100)
    
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
    plt.colorbar(scatter, label='Color Scale')
    
    plt.title('Scatter Plot with Varying Sizes and Colors')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.grid(True, alpha=0.3)
    
    plt.savefig('../data/plots/scatter_plot.png', dpi=300, bbox_inches='tight')
    print("  Saved: scatter_plot.png")
    plt.close()
    
    print()


def demonstrate_histogram():
    """
    Demonstrates histograms.
    """
    if not MATPLOTLIB_AVAILABLE:
        return
    
    print("=== Histogram ===")
    
    # Generate random data
    np.random.seed(42)
    data = np.random.normal(100, 15, 1000)
    
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    plt.axvline(data.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {data.mean():.2f}')
    
    plt.title('Distribution of Test Scores', fontsize=16)
    plt.xlabel('Score')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.savefig('../data/plots/histogram.png', dpi=300, bbox_inches='tight')
    print("  Saved: histogram.png")
    plt.close()
    
    print()


def demonstrate_pie_chart():
    """
    Demonstrates pie charts.
    """
    if not MATPLOTLIB_AVAILABLE:
        return
    
    print("=== Pie Chart ===")
    
    # Data
    categories = ['Category A', 'Category B', 'Category C', 'Category D']
    sizes = [30, 25, 20, 25]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    explode = (0.1, 0, 0, 0)  # Explode first slice
    
    plt.figure(figsize=(10, 8))
    plt.pie(sizes, explode=explode, labels=categories, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('Distribution by Category', fontsize=16)
    plt.axis('equal')
    
    plt.savefig('../data/plots/pie_chart.png', dpi=300, bbox_inches='tight')
    print("  Saved: pie_chart.png")
    plt.close()
    
    print()


def demonstrate_subplots():
    """
    Demonstrates creating multiple subplots.
    """
    if not MATPLOTLIB_AVAILABLE:
        return
    
    print("=== Subplots ===")
    
    x = np.linspace(0, 10, 100)
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Subplot 1: Line plot
    axes[0, 0].plot(x, np.sin(x), 'b-')
    axes[0, 0].set_title('Sine Wave')
    axes[0, 0].grid(True)
    
    # Subplot 2: Cosine plot
    axes[0, 1].plot(x, np.cos(x), 'r-')
    axes[0, 1].set_title('Cosine Wave')
    axes[0, 1].grid(True)
    
    # Subplot 3: Bar chart
    categories = ['A', 'B', 'C', 'D']
    values = [4, 7, 2, 9]
    axes[1, 0].bar(categories, values, color='green')
    axes[1, 0].set_title('Bar Chart')
    
    # Subplot 4: Scatter plot
    axes[1, 1].scatter(np.random.randn(50), np.random.randn(50), alpha=0.5)
    axes[1, 1].set_title('Scatter Plot')
    axes[1, 1].grid(True)
    
    plt.tight_layout()
    plt.savefig('../data/plots/subplots.png', dpi=300, bbox_inches='tight')
    print("  Saved: subplots.png")
    plt.close()
    
    print()


def demonstrate_customization():
    """
    Demonstrates plot customization.
    """
    if not MATPLOTLIB_AVAILABLE:
        return
    
    print("=== Plot Customization ===")
    
    x = np.linspace(0, 10, 100)
    y = np.exp(-x/10) * np.sin(x)
    
    plt.figure(figsize=(12, 6))
    
    # Plot with custom style
    plt.plot(x, y, color='#FF6B6B', linewidth=3, linestyle='-', 
             marker='o', markevery=10, markersize=8, markerfacecolor='white',
             markeredgecolor='#FF6B6B', markeredgewidth=2, label='Damped Sine')
    
    # Customization
    plt.title('Highly Customized Plot', fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('Time (s)', fontsize=14, fontweight='bold')
    plt.ylabel('Amplitude', fontsize=14, fontweight='bold')
    
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='upper right', fontsize=12, framealpha=0.9)
    
    # Add annotations
    max_idx = np.argmax(y)
    plt.annotate('Maximum', xy=(x[max_idx], y[max_idx]), 
                xytext=(x[max_idx]+1, y[max_idx]+0.1),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=12, color='red')
    
    plt.tight_layout()
    plt.savefig('../data/plots/customized.png', dpi=300, bbox_inches='tight')
    print("  Saved: customized.png")
    plt.close()
    
    print()


def demonstrate_pandas_integration():
    """
    Demonstrates plotting directly from Pandas DataFrames.
    """
    if not MATPLOTLIB_AVAILABLE:
        return
    
    print("=== Pandas Integration ===")
    
    # Create sample DataFrame
    df = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Sales': [1200, 1500, 1800, 1600, 2000, 2200],
        'Expenses': [800, 900, 1000, 950, 1100, 1150]
    })
    
    # Plot directly from DataFrame
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Line plot
    df.plot(x='Month', y=['Sales', 'Expenses'], ax=axes[0], marker='o')
    axes[0].set_title('Sales vs Expenses Over Time')
    axes[0].set_ylabel('Amount ($)')
    axes[0].grid(True, alpha=0.3)
    
    # Bar plot
    df.plot(x='Month', y=['Sales', 'Expenses'], kind='bar', ax=axes[1])
    axes[1].set_title('Monthly Sales and Expenses')
    axes[1].set_ylabel('Amount ($)')
    axes[1].set_xlabel('Month')
    axes[1].legend(['Sales', 'Expenses'])
    
    plt.tight_layout()
    plt.savefig('../data/plots/pandas_plot.png', dpi=300, bbox_inches='tight')
    print("  Saved: pandas_plot.png")
    plt.close()
    
    print()


# EXERCISES
def exercise_1():
    """
    Exercise 1: Create a multi-line time series plot
    
    TODO: Plot temperature data over time for multiple cities
    """
    if not MATPLOTLIB_AVAILABLE:
        return
    
    print("=== Exercise 1: Temperature Time Series ===")
    
    # Create data
    days = np.arange(1, 31)
    np.random.seed(42)
    ny_temp = 20 + 5 * np.sin(days / 5) + np.random.randn(30)
    la_temp = 25 + 3 * np.sin(days / 5) + np.random.randn(30)
    chicago_temp = 15 + 6 * np.sin(days / 5) + np.random.randn(30)
    
    plt.figure(figsize=(12, 6))
    plt.plot(days, ny_temp, marker='o', label='New York', linewidth=2)
    plt.plot(days, la_temp, marker='s', label='Los Angeles', linewidth=2)
    plt.plot(days, chicago_temp, marker='^', label='Chicago', linewidth=2)
    
    plt.title('Daily Average Temperature - January 2025', fontsize=16, fontweight='bold')
    plt.xlabel('Day of Month', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    plt.legend(loc='best', fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    plt.savefig('../data/plots/exercise1_temperature.png', dpi=300, bbox_inches='tight')
    print("  Saved: exercise1_temperature.png")
    plt.close()
    
    print()


def exercise_2():
    """
    Exercise 2: Create a grouped bar chart
    
    TODO: Compare quarterly sales across different products
    """
    if not MATPLOTLIB_AVAILABLE:
        return
    
    print("=== Exercise 2: Quarterly Sales Comparison ===")
    
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    product_a = [150, 175, 200, 225]
    product_b = [180, 190, 185, 210]
    product_c = [120, 145, 170, 195]
    
    x = np.arange(len(quarters))
    width = 0.25
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    bars1 = ax.bar(x - width, product_a, width, label='Product A', color='#FF6B6B')
    bars2 = ax.bar(x, product_b, width, label='Product B', color='#4ECDC4')
    bars3 = ax.bar(x + width, product_c, width, label='Product C', color='#45B7D1')
    
    ax.set_xlabel('Quarter', fontsize=12, fontweight='bold')
    ax.set_ylabel('Sales (thousands)', fontsize=12, fontweight='bold')
    ax.set_title('Quarterly Sales by Product - 2025', fontsize=16, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(quarters)
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('../data/plots/exercise2_quarterly_sales.png', dpi=300, bbox_inches='tight')
    print("  Saved: exercise2_quarterly_sales.png")
    plt.close()
    
    print()


def exercise_3():
    """
    Exercise 3: Create a comprehensive dashboard
    
    TODO: Create a 2x2 subplot dashboard with different visualizations
    """
    if not MATPLOTLIB_AVAILABLE:
        return
    
    print("=== Exercise 3: Sales Dashboard ===")
    
    # Generate data
    np.random.seed(42)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales = [12000, 15000, 14500, 18000, 19500, 21000]
    categories = ['Electronics', 'Clothing', 'Food', 'Books', 'Sports']
    category_sales = [35, 25, 20, 10, 10]
    
    fig = plt.figure(figsize=(14, 10))
    
    # Subplot 1: Line chart - Monthly sales trend
    ax1 = plt.subplot(2, 2, 1)
    ax1.plot(months, sales, marker='o', linewidth=2, color='#FF6B6B')
    ax1.set_title('Monthly Sales Trend', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Sales ($)')
    ax1.grid(True, alpha=0.3)
    
    # Subplot 2: Bar chart - Top products
    ax2 = plt.subplot(2, 2, 2)
    products = ['Laptop', 'Phone', 'Tablet', 'Watch', 'Headphones']
    product_sales = [450, 380, 290, 210, 180]
    ax2.barh(products, product_sales, color='#4ECDC4')
    ax2.set_title('Top 5 Products', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Sales (units)')
    
    # Subplot 3: Pie chart - Category distribution
    ax3 = plt.subplot(2, 2, 3)
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    ax3.pie(category_sales, labels=categories, colors=colors, autopct='%1.1f%%', startangle=90)
    ax3.set_title('Sales by Category (%)', fontsize=14, fontweight='bold')
    
    # Subplot 4: Histogram - Order distribution
    ax4 = plt.subplot(2, 2, 4)
    order_values = np.random.normal(150, 40, 500)
    ax4.hist(order_values, bins=30, color='#98D8C8', edgecolor='black', alpha=0.7)
    ax4.set_title('Order Value Distribution', fontsize=14, fontweight='bold')
    ax4.set_xlabel('Order Value ($)')
    ax4.set_ylabel('Frequency')
    ax4.axvline(order_values.mean(), color='red', linestyle='--', label=f'Mean: ${order_values.mean():.2f}')
    ax4.legend()
    
    plt.suptitle('Sales Dashboard - Q1 2025', fontsize=18, fontweight='bold', y=0.995)
    plt.tight_layout()
    
    plt.savefig('../data/plots/exercise3_dashboard.png', dpi=300, bbox_inches='tight')
    print("  Saved: exercise3_dashboard.png")
    plt.close()
    
    print()


def exercise_4():
    """
    Exercise 4: Scatter plot with regression line
    
    TODO: Create a scatter plot showing correlation and add a trend line
    """
    if not MATPLOTLIB_AVAILABLE:
        return
    
    print("=== Exercise 4: Correlation Analysis ===")
    
    # Generate correlated data
    np.random.seed(42)
    study_hours = np.random.uniform(1, 10, 50)
    exam_scores = 40 + 5 * study_hours + np.random.normal(0, 5, 50)
    exam_scores = np.clip(exam_scores, 0, 100)
    
    # Calculate regression line
    z = np.polyfit(study_hours, exam_scores, 1)
    p = np.poly1d(z)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(study_hours, exam_scores, alpha=0.6, s=100, color='#4ECDC4', edgecolors='black')
    plt.plot(study_hours, p(study_hours), "r--", linewidth=2, label=f'Trend: y={z[0]:.2f}x+{z[1]:.2f}')
    
    plt.title('Study Hours vs Exam Scores', fontsize=16, fontweight='bold')
    plt.xlabel('Study Hours per Day', fontsize=12)
    plt.ylabel('Exam Score (%)', fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    
    # Calculate and display correlation
    correlation = np.corrcoef(study_hours, exam_scores)[0, 1]
    plt.text(0.05, 0.95, f'Correlation: {correlation:.3f}', 
             transform=plt.gca().transAxes, fontsize=12,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.savefig('../data/plots/exercise4_correlation.png', dpi=300, bbox_inches='tight')
    print("  Saved: exercise4_correlation.png")
    plt.close()
    
    print()


def exercise_5():
    """
    Exercise 5: Box plot for statistical analysis
    
    TODO: Create box plots to compare distributions
    """
    if not MATPLOTLIB_AVAILABLE:
        return
    
    print("=== Exercise 5: Statistical Comparison ===")
    
    # Generate data for different groups
    np.random.seed(42)
    group_a = np.random.normal(100, 15, 100)
    group_b = np.random.normal(110, 12, 100)
    group_c = np.random.normal(95, 18, 100)
    group_d = np.random.normal(105, 10, 100)
    
    data = [group_a, group_b, group_c, group_d]
    labels = ['Group A', 'Group B', 'Group C', 'Group D']
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Box plot
    bp = axes[0].boxplot(data, labels=labels, patch_artist=True)
    for patch, color in zip(bp['boxes'], ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']):
        patch.set_facecolor(color)
    axes[0].set_title('Performance Comparison (Box Plot)', fontsize=14, fontweight='bold')
    axes[0].set_ylabel('Score')
    axes[0].grid(True, alpha=0.3, axis='y')
    
    # Violin plot
    parts = axes[1].violinplot(data, positions=range(1, 5), showmeans=True, showmedians=True)
    axes[1].set_xticks(range(1, 5))
    axes[1].set_xticklabels(labels)
    axes[1].set_title('Performance Comparison (Violin Plot)', fontsize=14, fontweight='bold')
    axes[1].set_ylabel('Score')
    axes[1].grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('../data/plots/exercise5_statistical.png', dpi=300, bbox_inches='tight')
    print("  Saved: exercise5_statistical.png")
    plt.close()
    
    print()


if __name__ == "__main__":
    """
    Main execution block - runs all demonstrations and exercises.
    """
    if not MATPLOTLIB_AVAILABLE:
        print("=" * 60)
        print("ERROR: matplotlib, numpy, and/or pandas not installed")
        print("=" * 60)
        print("\nPlease install required packages:")
        print("  pip install matplotlib numpy pandas")
        print("\nThen run this module again.")
        exit(1)
    
    # Ensure output directory exists
    Path("../data/plots").mkdir(parents=True, exist_ok=True)
    
    print("=" * 60)
    print("PLOTTING GRAPHS WITH MATPLOTLIB - COMPLETE GUIDE")
    print("=" * 60)
    print()
    
    # Run all demonstrations
    demonstrate_basic_plotting()
    demonstrate_multiple_lines()
    demonstrate_bar_chart()
    demonstrate_horizontal_bar()
    demonstrate_scatter_plot()
    demonstrate_histogram()
    demonstrate_pie_chart()
    demonstrate_subplots()
    demonstrate_customization()
    demonstrate_pandas_integration()
    
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
    print("All plots saved in: ../data/plots/")
    print("END OF PLOTTING MODULE")
    print("=" * 60)
