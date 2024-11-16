import pandas as pd
import os

# Directory containing the CSV files

# List to hold dataframes
dfs = []

# Read each CSV file into a dataframe and append to the list
for i in range(58):
    df = pd.read_csv(f'data_{i}.csv')
    dfs.append(df)

# Concatenate all dataframes into one
combined_df = pd.concat(dfs, ignore_index=True)

# Write the combined dataframe to a new CSV file
combined_df.to_csv("acled.csv", index=False)