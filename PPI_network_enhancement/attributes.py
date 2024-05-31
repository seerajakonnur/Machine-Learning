import re
import array
import sys
import os
import operator
import pandas as pd
import numpy as np
from pandas import read_csv
import csv
import statistics
import modlamp
from modlamp.descriptors import PeptideDescriptor, GlobalDescriptor
data=pd.read_csv("motifs.csv")
arr_motifs=data.values
#arr_motifs=arr[:,4]
#print(arr_motifs)
arr_len=[]
motif=[]
ch=[]
ch_den=[]
ip=[]
ii=[]
bi=[]
hr=[]
ar=[]
al=[]
for i in arr_motifs:
 print(i[0])
 motif.append(i[0])
 arr_len.append(len(i[0]))


# charge
for i,j in zip(arr_motifs, arr_len):
 desc = GlobalDescriptor(i[0])
 desc.calculate_charge(ph=7.4, amide=True)
 ch.append(desc.descriptor/j)


#hydrophobic ratio
for i,j in zip(arr_motifs, arr_len):
 desc = GlobalDescriptor(i[0])
 desc.hydrophobic_ratio()
 hr.append(desc.descriptor/j)

# aromaticity
for i,j in zip(arr_motifs, arr_len):
 desc = GlobalDescriptor(i[0])
 desc.aromaticity()
 ar.append(desc.descriptor/j)

# aliphatic index
for i,j in zip(arr_motifs, arr_len):
 desc = GlobalDescriptor(i[0])
 desc.aliphatic_index()
 al.append(desc.descriptor/j)



df = pd.DataFrame({"motif" : motif, "charge" : ch, "hr" : hr,  "aromaticity" : ar, "aliphatic_index" : al})
df.to_csv("attributes.csv", index=False)




 



