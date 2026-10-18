import numpy as np
import pandas as pd


np.random.seed(42)
n_samples = 50
genes = [f"Gene_{i}" for i in range(1, 11)]

data = {gene: np.random.normal(loc=8.0, scale=1.5, size=n_samples) for gene in genes}
df = pd.DataFrame(data)


df.iloc[2, 0] = np.nan
df.iloc[7, 3] = np.nan
df.iloc[14, 5] = np.nan

print("=== RAW DATA PREVIEW ===")
print(df.head())
print("\nMissing values per feature before cleaning:")
print(df.isnull().sum())


df_cleaned = df.fillna(df.median())
print("\nMissing values after median imputation:")
print(df_cleaned.isnull().sum().sum())


summary_stats = df_cleaned.describe().T[['mean', 'std', 'min', '50%', 'max']]
summary_stats.rename(columns={'50%': 'median'}, inplace=True)

print("\n=== SUMMARY STATISTICS ===")h
print(summary_stats)


summary_stats.to_csv("summary_statistics.csv")
print("\nCleaned summary statistics successfully saved to 'summary_statistics.csv'.")
