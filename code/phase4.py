"""

 Created on 07-Jun-21
 @author: Kiril Zelenkovski

 phase4.py: Frequency analysis

"""


def percentage(part, whole):
    return 100 * float(part) / float(whole)


lineages = open("train-1.txt", "r")
my_lineages = lineages.read().splitlines()

variants = open("train-2.txt", "r")
my_variants = variants.read().splitlines()

print(len(my_variants[0]))
print(len(my_lineages[1]))

all_variants = my_variants + my_lineages
print("Total # of variants + lineages:", len(all_variants))
unique_variants = list(set(all_variants))
print("Total # of unique variants + lineages:", len(unique_variants))

# Write all peptides into text file
with open('train.txt', 'w') as f:
    for item in unique_variants:
        f.write("%s\n" % item)

print("\n\n-=-=-=-=-=-=-=-=-=-=-=- Frequency analysis -=-=-=-=-=-=-=-=-=-=-=-")

count_N = 0
count_Y = 0

for lineage in unique_variants:
    if lineage[500] == "N":
        count_N += 1
    elif lineage[500] == 'Y':
        count_Y += 1

print()
print("Count N for codon 501 is: " + str(count_N),
      f'[{percentage(count_N, count_N + count_Y):.2f}%]')

print("Count Y for codon 501 is: " + str(count_Y),
      f'[{percentage(count_Y, count_N + count_Y):.2f}%]')

count_D = 0
count_G = 0

for lineage in unique_variants:
    if lineage[613] == "D":
        count_D += 1
    elif lineage[613] == 'G':
        count_G += 1

print()
print("Count D for codon 614 is: " + str(count_D),
      f'[{percentage(count_D, count_D + count_G):.2f}%]')

print("Count G for codon 614 is: " + str(count_G),
      f'[{percentage(count_G, count_D + count_G):.2f}%]')

count_Q = 0
count_H = 0

for lineage in unique_variants:
    if lineage[676] == "Q":
        count_D += 1
    elif lineage[676] == 'H':
        count_G += 1

print()
print("Count Q for codon 677 is: " + str(count_D),
      f'[{percentage(count_D, count_D + count_G):.2f}%]')

print("Count H for codon 677 is: " + str(count_G),
      f'[{percentage(count_G, count_D + count_G):.2f}%]')
