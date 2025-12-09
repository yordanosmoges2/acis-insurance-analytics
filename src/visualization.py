import seaborn as sns
import matplotlib.pyplot as plt

def plot_histogram(df, column):
    plt.figure(figsize=(10,5))
    sns.histplot(df[column], kde=True, bins=30)
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

def plot_scatter(df, x, y):
    plt.figure(figsize=(10,5))
    sns.scatterplot(x=df[x], y=df[y])
    plt.title(f"{y} vs. {x}")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()

def plot_correlation_matrix(df):
    plt.figure(figsize=(12,8))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=False, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()

def plot_boxplot(df, column):
    plt.figure(figsize=(6,6))
    sns.boxplot(x=df[column])
    plt.title(f"Boxplot of {column}")
    plt.show()
