#library(devtools)
#install_github("dosorio/Peptides")
library(Peptides)
data=read.csv(file="motifs.csv", header=TRUE)
motifs=data$motifs
#print(motifs)
bi=array()
ii=array()
ip=array()
#
for(i in motifs){
 bi[i]=boman(i)
 #print(boman(i))
 #print("II")
 ii[i]=instaIndex(i)
 ip[i]=pI(i)
}
write.csv(bi, file = "bi.csv",row.names=FALSE)
write.csv(ii, file = "ii.csv",row.names=FALSE)
write.csv(ip, file = "ip.csv",row.names=FALSE)
