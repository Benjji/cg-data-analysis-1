
import math
import matplotlib.pyplot as plt

wildlines = open("wildtype.sorted.coverage.filtered", "r").readlines()
tumorlines = open("tumor.sorted.coverage.filtered", "r").readlines()

wp = 0
tp = 0

x, y = [], []

while wp < len(wildlines) or tp < len(tumorlines):
    wildpos, wildcov = [int(x) for x in wildlines[wp].strip().split('\t')]
    tumorpos, tumorcov = [int(x) for x in tumorlines[tp].strip().split('\t')]
    
    if wildpos < tumorpos:
        wp += 1
        continue
    if tumorpos < wildpos:
        tp += 1
        continue

    wp += 1
    tp += 1
    
    if wildcov == 0 or tumorcov == 0:
        continue

    score = math.log2(tumorcov/wildcov)
    x.append(tumorpos)
    y.append(score)


plt.rcParams['figure.figsize'] = (12, 2)
plt.scatter(x, y, s=0.1)
plt.savefig('coverage_plot.png')
    
