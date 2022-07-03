# Statistical-analysis-and-Machine-Learning

Description of codes: PCA-pipeline.ipynb, Fanova_pipeline_methyl_fanova_ranking.ipynb, Fanova_pipeline_methyl_fanova_model.ipynb, Fnaova_pipeline_methyl_fanova_prediction.ipynb

These codes carry out classification of Head and neck cancer samples as cancerous (tumor) and non cancerous (normal) based on methylation data using 
machine learning (random forest). Most biological data sets like multi omics data sets (gene expression, miRNA expression, methylation) contain a large number of features (gene expression data contains 25000 to 35000 features). However, there is a lot of redundancy involved in such data. Moreover, the sample number is usually very low (around 100 to 500). Training a machine learning model on this type of data can create problems. Therefore, we use data reduction methods which reduce the dimensions (features) of the data while retaining most of the information from the original data. There are several data reduction methods such as Principal component analysis, statistical methods, feature elimination methods, etc. Here, I have used PCA and one of the statistical methods ANOVA F - value value.

PCA based pipeline (PCA-pipeline.ipynb):
    • To differentiate between cancerous and non cancerous samples for head and neck cancer data from CPTAC using methylation data.
    • The data consisting of cancerous and non cancerous samples is first split into training and test data in the ratio 80% training and 20% testing data using python sklearn’s test train split feature.
    • Principal component analysis (PCA) from sklearn.decomposition is used to get the principal components, explained variance, explained variance ratio.
    • The first ‘n’ principal components which contain around 85% of the information are taken for further analysis. 
    • Sklearn’s RandomizedsearchCV is performed on training data to get the best parameters and best estimator using Random forest classifier.
    • The best random forest model is saved and used to predict the classification of test data samples.
    
 ANOVA F - value based approch:   
 Code Fanova_pipeline_methyl_fanova_ranking.ipynb : 
     • The data consisting of cancerous and non cancerous samples is first split into training and test data in the ratio 80% training and 20% testing data using python sklearn’s test train split feature.
    • Removing features having zero variance from training data using sklearn variance threshold.
    • Applying f_classif from sklearn.feature_selection to the training data to rank the features.
    • This calculates the anova F value and ranks the features accordingly. Save the rankings for further analysis
    
 Code Fanova_pipeline_methyl_fanova_model.ipynb :
    • Training the Random forest model on top 100 features and then on only top 50 features using RandomizedsearchCV. Best models are saved from both top 100 features and top 50 features.
    
  Code Fnaova_pipeline_methyl_fanova_prediction.ipynb :
    • The best model from both (top 100 features and top 50 features ) is used to predict the classification of test data samples.
    

Description of code SVM_deep_learning_on_speech_data.ipynb
This code carries out classification of speech data samples into 'Cold' i.e. presence of cold or flu and 'Not Cold' i.e. absence of cold and flu using support vector machines and deep learning. 
