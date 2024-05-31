library(Peptides)
data=read.csv(file="nef_top_only_motifs.csv", header=TRUE)
motifs=data$motifs
ki=array()
#
for(i in motifs){
 ki[i]=kideraFactors(i)
}
print(ki)
write.csv(ki, file = "kidera.csv",row.names=FALSE) # save it in csv file

# transpose the file
data2=read.csv(file="kidera.csv", header=TRUE)
final_df= as.data.frame(t(data2))
print(final_df)
write.csv(final_df, file = "kidera_trans.csv")
