"""

 Created on 07-Jun-21
 @author: Kiril Zelenkovski
 @project: Predicting S-gene (glycoprotein) of Sars-Cov-2 virus

 phase3.py: Create protein sequences for emerging variants

"""
import os
import glob
import pandas as pd
import re

def get_mutations(S_protein, variants):
    var_aa = []
    for name in variants:
        print(name)
        mutations = name.split("_")
        S_copy = S_protein[:]
        for m in range(0, len(mutations)):
            mutations_list = re.split('(\d+)', mutations[m])
            if mutations_list[2] == 'del':
                continue
            else:
                codon_num = int(mutations_list[1]) - 1
                print("Mutating ", S_copy[codon_num], "into", mutations_list[2])
                S_copy[codon_num] = mutations_list[2]

        S_aa = "".join(S_copy)
        print(S_aa[:15] + "..."+S_aa[-1], "\n")
        var_aa.append(S_aa)
    return var_aa


# from Bio import SeqIO
#
# df = pd.read_csv("combined_data.csv")
# emerging_variants = df['Variant'].tolist()
#
# for seq_record in SeqIO.parse("./data-fasta/sars-cov-2-glycoprotein.fasta", "fasta"):
#     print("ID: ", seq_record.id)
#     print("Description: Surface glycoprotein [Sars-Cov-2]")
#     print("Protein sequence: ", repr(seq_record.seq))
#     print("Amino acid length: ", len(seq_record), "\n")
#
# S_region = list(seq_record.seq)
# variants_peptides = get_mutations(S_region, emerging_variants[:])
# print(variants_peptides[0])
# unique_peptides = set(variants_peptides)
#
# print("Total # of peptides:", len(variants_peptides))
# print("Total # of unique peptides:", len(unique_peptides))
#
# # Write all peptides into text file
# with open('train-2.txt', 'w') as f:
#     for item in unique_peptides:
#         f.write("%s\n" % item)
