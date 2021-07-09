"""

 Created on 07-Jun-21
 @author: Kiril Zelenkovski
 @project: Predicting S-gene (glycoprotein) of Sars-Cov-2 virus

 phase2.py: Create protein sequences (aa chains) from maps

"""
import os
import glob
import pandas as pd
import json


def create_linage_peptides(S_protein, lineages):
    """

    :param S_protein:
    :param lineages:
    :return:
    """
    linage_aa = []
    for lineage in lineages:
        # Create copy for current linage
        S_copy = S_protein[:]

        # Opening JSON file
        f = open('./outbreakinfo/' + lineage + '.json', )

        # json.load: returns JSON object as a dictionary
        data = json.load(f)

        # Mutations in linage
        print(lineage)
        for mutation in data:
            if mutation['gene'] == 'S':

                if mutation['type'] == 'substitution':
                    ref_aa = mutation['ref_aa']
                    codon_num = mutation['codon_num'] - 1
                    alt_aa = mutation['alt_aa']

                    print("Mutation is of type - " + mutation['type'], " :",
                          mutation['ref_aa'],
                          mutation['codon_num'],
                          mutation['alt_aa'])

                    # Check if aa on codon is equal to aa on referent genome
                    if S_copy[codon_num] == ref_aa:
                        # Mutate to alternative amino acid
                        S_copy[codon_num] = alt_aa
                        print("Mutated " + ref_aa + " into " + alt_aa)



        S_aa = "".join(S_copy)
        print(S_aa, "\n")
        linage_aa.append(S_aa)


    return linage_aa

#
# from Bio import SeqIO
#
# for seq_record in SeqIO.parse("./data-fasta/sars-cov-2-glycoprotein.fasta", "fasta"):
#     print("ID: ", seq_record.id)
#     print("Description: Surface glycoprotein [Sars-Cov-2]")
#     print("Protein sequence: ", repr(seq_record.seq))
#     print("Amino acid length: ", len(seq_record), "\n")
#
# S_region = list(seq_record.seq)
#
# lineage_text_file = open("./outbreakinfo/LINEAGES.txt", "r")
# my_lineages = lineage_text_file.read().splitlines()
#
# # print()
# # print(my_lineages[113], " is not considered as lineage: so we will remove it!")
# # my_lineages.remove('B.1.608')
#
#
# # Create linage peptides
# lineage_peptides = create_linage_peptides(S_region, my_lineages[:])
# print("Total # of peptides:", len(lineage_peptides))
# print("Total # of lineages:", len(my_lineages))
#
# # Now take unique values
# unique_lineages = list(set(lineage_peptides))
# print("Total # of peptides after processing all duplicates:", len(unique_lineages))
#
# # Write all peptides into text file
# with open('train-1.txt', 'w') as f:
#     for item in unique_lineages:
#         f.write("%s\n" % item)
#
