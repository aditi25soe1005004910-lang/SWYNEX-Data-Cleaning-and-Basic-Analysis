# Task 2: Data Cleaning and Basic Analysis

## Overview
This repository contains data cleaning routines and basic statistical profiling for simulated gene expression metrics modeled after NCBI GEO dataset GSE20685.

## Steps Executed
1. **Data Inspection**: Identified missing values and structure across 10 genomic features over 50 samples.
2. **Data Cleaning**: Handled missing values using median expression imputation to maintain distribution integrity without introducing extreme bias.
3. **Statistical Summary**: Calculated key distribution metrics including mean, standard deviation, median, minimum, and maximum expression values.
4. **Output**: Generated exportable statistical summary table (`summary_statistics.csv`).

## Execution
Run the analysis script via Python:
```bash
python analysis.py
