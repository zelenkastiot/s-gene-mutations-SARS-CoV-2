"""

 Created on 06-Jun-21
 @author: Kiril Zelenkovski
 @project: Predicting S-gene (glycoprotein) of Sars-Cov-2 virus

 phase1.py: Map all variants to their lineages

"""
import os
import glob
import pandas as pd


def lineage_mutations(lineage_list):
    for lineage in lineage_list:
        # Mutation counter
        i = 0

        # Opening JSON file
        f = open('./outbreakinfo/' + lineage + '.json', )

        # json.load: returns JSON object as a dictionary
        data = json.load(f)

        # Current lineage
        print(lineage)

        # Iterating through the json list
        for mutation in data:
            if mutation['gene'] == 'S':
                i += 1

                # if mutation['type'] == 'substitution':
                #     print(str(i) + " mutation is of type - " + mutation['type'], " :",
                #           mutation['ref_aa'],
                #           mutation['codon_num'],
                #           mutation['alt_aa'])
                #
                # else:
                #     print(str(i) + " mutation is of type - " + mutation['type'], " :",
                #           mutation['ref_aa'])

        # print("Total number of mutations in S-gene: " + str(i), "\n")
    print("Finished all")

# Read combined_csv_data from 0-phase
df = pd.read_csv("combined_data-2.csv")

# List all lineages
all_lineages = []
for index, row in df.iterrows():
    all_lineages.append(row['#Top Lineage'].split(" ")[1])
    # if row['#Top Lineage'].split(" ")[1] == "B.1.1.70":
    #     print(row['Variant'])


import collections

counter = collections.Counter(all_lineages)

print(counter)

# Get all unique values
all_lineages = list(set(all_lineages))
print("Total number of (unique) lineages: ", len(all_lineages), "\n")

# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ Create lineages dataset -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
from Bio import SeqIO

for seq_record in SeqIO.parse("./data-fasta/sars-cov-2-glycoprotein.fasta", "fasta"):
    print("ID: ", seq_record.id)
    print("Description: Surface glycoprotein [Sars-Cov-2]")
    print("Protein sequence: ", repr(seq_record.seq))
    print("Amino acid length: ", len(seq_record))
    S_region = seq_record.seq

# Save all unique lineages as text file
lineage_text_file = open("./outbreakinfo/LINEAGES.txt", "w")
for element in all_lineages:
    lineage_text_file.write(element + "\n")
lineage_text_file.close()

# Locate all Lineages on outbreak info, locate their mutations
import json

lineage_text_file = open("./outbreakinfo/LINEAGES.txt", "r")
my_lineages = lineage_text_file.read().splitlines()

# print("-_-_-_-_-_-_-_-_-_-_-_-_-_ LINEAGE ANALYSIS -_-_-_-_-_-_-_-_-_-_-_-_-_ ", "\n")

# B.1.608 is not considered to be a lineage: https://github.com/cov-lineages/pango-designation/issues/82
# print()
# print(my_lineages[113], " is not considered as lineage: so we will remove it!")
# my_lineages.remove('B.1.608')

lineage_mutations(my_lineages[:])
