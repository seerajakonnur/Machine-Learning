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

# getting human proteins interacting with pathogen (ex. matrix protein) positive interactions group 
data=pd.read_csv("binding_interaction_filename.csv")
arr=data.values
arr2=arr[:,2]
a1=[]
b1=[]
c1=[]
d1=[]
e1=[]
f1=[]
# example pathogen protein 'matrix'
print(arr[2][2])
for i in arr:
 if i[2]=="matrix":
  a1.append(i[2])
  b1.append(i[3])
  c1.append(i[4])
  d1.append(i[5])
  e1.append(i[6])
  f1.append(i[7])

df = pd.DataFrame({"Hiv_protein" : a1, "Keyword" : b1, "human_gene_id" : c1, "human_gene_symbol" : d1, "human_prot_accession" : e1, "human_prot_name" : f1})
df.to_csv("only_mat_binds.csv", index=False)

# getting human proteins not interacting with pathogen (ex. matrix protein) negative interactions group 

data3=pd.read_csv("all_interactions.csv")
arr3=data3.values
a1=[]
b1=[]
c1=[]
d1=[]
e1=[]
f1=[]
for i in arr3:
 if i[2]=="matrix":
  a1.append(i[2])
  b1.append(i[3])
  c1.append(i[4])
  d1.append(i[5])
  e1.append(i[6])
  f1.append(i[7])

df = pd.DataFrame({"Hiv_protein" : a1, "Keyword" : b1, "human_gene_id" : c1, "human_gene_symbol" : d1, "human_prot_accession" : e1, "human_prot_name" : f1})
df.to_csv("only_mat_all_interactions.csv", index=False)

#
data4=pd.read_csv("all_interactions.csv")
arr4=data4.values
a1=[]
b1=[]
c1=[]
d1=[]
e1=[]
f1=[]
for i in arr4:
 if i[2]!="matrix":
  a1.append(i[2])
  b1.append(i[3])
  c1.append(i[4])
  d1.append(i[5])
  e1.append(i[6])
  f1.append(i[7])

df = pd.DataFrame({"Hiv_protein" : a1, "Keyword" : b1, "human_gene_id" : c1, "human_gene_symbol" : d1, "human_prot_accession" : e1, "human_prot_name" : f1})
df.to_csv("not_mat_all_interactions.csv", index=False)
#
data5=pd.read_csv("only_mat_all_interactions.csv")
arr5=data5.values
data6=pd.read_csv("not_mat_all_interactions.csv")
arr6=data6.values
a1=[]
b1=[]
c1=[]
d1=[]
e1=[]
f1=[]
a_new=[]
for i in arr6:
 t=0
 for j in arr5:
  if i[3]==j[3]:
   t=t+1
 if t==0:
  a1.append(i[0])
  b1.append(i[1])
  c1.append(i[2])
  d1.append(i[3])
  e1.append(i[4])
  f1.append(i[5])
df = pd.DataFrame({"Hiv_prot" : a1,"keyword" : b1,"human_gene_id" : c1,"human_gene_symbol" : d1, "human_prot_acc" : e1, "human_prot_des" : f1})
df.to_csv("mat_not_interacting.csv", index=False)

   
