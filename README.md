# Statistical-analysis-and-Machine-Learning
This code carries out classification of Head and neck cancer samples as cancerous (tumor) and non cancerous (normal) based on methylation data using 
machine learning (random forest). Most biological data sets like multi omics data sets (gene expression, miRNA expression, methylation) contain a large number of features (gene expression data contains 25000 to 35000 features). However, there is a lot of redundancy involved in such data. Moreover, the sample number is usually very low (around 100 to 500). Training a machine learning model on this type of data can create problems. Therefore, we use data reduction methods which reduce the dimensions (features) of the data while retaining most of the information from the original data. There are several data reduction methods such as Principal component analysis, statistical methods, feature elimination methods, etc. Here, we are going to use PCA and one of the statistical methods F anova value.
PCA based pipeline (PCA-pipeline.ipynb):
    • To differentiate between cancerous and non cancerous samples for head and neck cancer data from CPTAC using methylation data.
    • The data consisting of cancerous and non cancerous samples is first split into training and test data in the ratio 80% training and 20% testing data using python sklearn’s test train split feature.
    • Principal component analysis (PCA) from sklearn.decomposition is used to get the principal components, explained variance, explained variance ratio.
    • The first ‘n’ principal components which contain around 85% of the information are taken for further analysis. 
    • Sklearn’s RandomizedsearchCV is performed on training data to get the best parameters and best estimator using Random forest.
    • The best random forest model is saved and used to predict samples from test data.
    
 ANOVA F - value based approch:   
 Code 
    
