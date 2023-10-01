# Classification of tissue samples into cancerous and non-cancerous samples based on Multi-omics data using machine learning

These codes were developed to carry out a classification task (classifying tissues into cancerous and non-cancerous samples). The data used was multi-omics data. It includes mRNA, miRNA (micro RNA) and methylation data. During the project, analysis was carried out using all three types of omics data separately as well as using a multi-omics approach. The methodology followed was same for all. This folder all scripts developed for methylation data. As the dimensionality of multi-omics data is high, two dimensionality reduction techniques were used viz. ANOVA F-value and PCA. 
PCA-pipeline.ipynb :
• To differentiate between cancerous and non cancerous samples for head and neck cancer data from CPTAC using methylation data.
• The data consisting of cancerous and non cancerous samples is first split into training and test data in the ratio 80% training and 20% testing data using python sklearn’s test train split feature.
• Principal component analysis (PCA) from sklearn.decomposition is used to get the principal components, explained variance, explained variance ratio.
• The first ‘n’ principal components which contain around 85% of the information are taken for further analysis.
• Sklearn’s RandomizedsearchCV is performed on training data to get the best parameters and best estimator using Random forest classifier.
• The best random forest model is saved and used to predict the classification of test data samples.
