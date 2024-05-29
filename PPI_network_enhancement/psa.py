import os,sys,argparse,operator
import pandas as pd
import numpy as np
from pandas import read_csv
def GetRecommendations(df,user):
	#this will show up as 1 only for those users which are 
	#being currently examined everyone else will be set to 0
	UniqueUsers = list(df['users'].unique())
	df['usersinitweight']=np.where(df['users']==user, 1, 0)
	
	#store the resources that are connected to the current selected
	#users
	resourcesusedbyuser = list(df.query('usersinitweight==1')['resources'])
	#print resourcesusedbyuser
	##countresources = df.groupby('resources').count()
	#this will make a subset of dataframe based on the resourceslist
	dfx = df.loc[df['resources'].isin(resourcesusedbyuser)]
	#print dfx
	countresources = df['resources'].value_counts().to_dict()
	#print countresources
	#this holds the value of how much resources the particular resource can contribute
	#to anyone connected to it
	propogate_first_random = {k: (1.0/float(v)) for k, v in countresources.items()}
	#print propogate_first_random
	dfx['firstrandomwalk']= dfx['resources'].map(propogate_first_random)
	#df2 = df.groupby('users').aggregate('firstrandomwalk')
	firstrandomwalkout = dfx.groupby('users')['firstrandomwalk'].aggregate('sum').to_dict()
	for j in range(len(UniqueUsers)):
		try:
			firstrandomwalkout[UniqueUsers[j]]
		except KeyError:
			firstrandomwalkout[UniqueUsers[j]]=0.0
	#print df.groupby('users').filter(lambda x: (x.initweight>0).all())
	#firstrandomwalkoutdict = {k:list(firstrandomwalkout.ix[k].index) for k in firstrandomwalkout.index.levels[0]}
	#print firstrandomwalkout
	df['FinalUserValsAfterFirstRandomWalk'] = df['users'].map(firstrandomwalkout)
	#print df
	countusers = df['users'].value_counts().to_dict()
	#print countusers
	df['usercounts'] = df['users'].map(countusers)
	df['secondrandomwalkvalues'] =  df['FinalUserValsAfterFirstRandomWalk']/df['usercounts']
	secondrandomwalkout = df.groupby('resources')['secondrandomwalkvalues'].aggregate('sum').to_dict()
	#print secondrandomwalkout
	df['FinalUserValsAfterSecondRandomWalk'] = df['resources'].map(secondrandomwalkout)
	finaldict = {}
	secondkeys = secondrandomwalkout.keys()
	for k in range(len(secondkeys)):
		if secondkeys[k] in resourcesusedbyuser:
			finaldict[secondkeys[k]] = 0.0
		else:
			finaldict[secondkeys[k]] = secondrandomwalkout[secondkeys[k]]
	df['FinalResults'] = df['resources'].map(finaldict)
	dfxF = df.loc[df['FinalResults']>0.0]
	#print dfxF[['users','resources', 'FinalResults']]
	Finaldict = area_dict = dict(zip(dfxF.resources, dfxF.FinalResults))
	#SortedDict =  sorted(Finaldict.items(), key=operator.itemgetter(1), reverse=True) 
	sorteddict = sorted(Finaldict.items(), key=lambda kv: kv[1], reverse=True)
	return sorteddict
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='This code will implement the probabilistic spreading algorithm for a bipartite host-pathogen network. The first column is the pathogen the second the host interaction. The pathogen will be treated as the user and the host will be treated as the item')
	parser.add_argument('HPppin', type= str, help='Please provide the tab-separated PPI host-pathogen interaction with the first column being the pathogen and second being the host')
	parser.add_argument('outfilename',type=str,help='Give a name for the output results file')
	args = parser.parse_args()
	df = read_csv(args.HPppin, sep='\t')
	df.rename(columns={df.columns[0]: 'users', df.columns[1]:'resources'}, inplace=True)
	#print(df)
	#df.columns=['users','resources']
	uniqueusers = df['users'].unique()
	uniqueresources = df['resources'].unique()
	fout = open(args.outfilename,'w')
	fout.write('Genes\tRecommended_Interactors\n')
	#calculate the final resources allocated for each user by a random walk
	for i in range(len(uniqueusers)):
		recommendation = GetRecommendations(df,uniqueusers[i])
		recomlist = []
		for p in range(len(recommendation)):
			recomlist.append('%s:%s'%(str(recommendation[p][0]),str(recommendation[p][1])))
		recomstring = '|'.join(recomlist)
		fout.write(uniqueusers[i]+"\t%s\n"%(recomstring))
	fout.close()
