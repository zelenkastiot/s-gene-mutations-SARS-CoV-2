"""

 Created on 06-Jun-21
 @author: Kiril Zelenkovski
 @project: Predicting S-gene (glycoprotein) of Sars-Cov-2 virus

 phase0.py: Manipulating with data from GISAID (Jul-2020:Apr-2021)

"""
import os
import glob
import pandas as pd

# Read all files in data directory
os.chdir("./data-updated")
file_extension = '.csv'
all_filenames = [i for i in glob.glob(f'*{file_extension}')]


# Insert timestamp for datasets before concatenation
all_files_modified = []
for file in all_filenames:
    df = pd.read_csv(file)
    timestamp = file.split('-')[1].split(".")[0]
    # print(timestamp)
    df.insert(8, "Timestamp", timestamp)
    all_files_modified.append(df)

# pd.concat: command by default stacks dataframes vertically
combined_csv_data = pd.concat(all_files_modified)

# Saving our combined csv data as a new file; index=False to lose "index" column
os.chdir('..')
combined_csv_data = combined_csv_data.drop(['#Genomes',
                                            '#Top Location',
                                            '#Top Clade',
                                            'Δ#Loc(S)',
                                            '#aachanges(C)'], axis=1)

# Print dataset info
print("Shape (rows/columns) of new data: ", combined_csv_data.shape)
print("Column names in our new data: ", combined_csv_data.columns.values)
print("Preview of first 5 rows: ")
print(combined_csv_data.head(5))
combined_csv_data.to_csv('combined_data-3.csv', index=False)
