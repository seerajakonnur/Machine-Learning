• The data was obtained from the UK Biobank.

• The code 'undersampling_for_cvd.ipynb' shows the imbalance in the data, also carries out descriptive statistics and performs random undersampling as the data was imbalanced for the 'cardiovascular disease death' outcome. The data had extreme imbalance as the proportion of the  minority class was less than 1 % .

• The codes starting with 'cvd_death_nested' contains the ML model for 'cardiovascular disease death' outcome (each code containing different combinations of features).

• The different feature combinations considered were: only classical risk factors, classical risk factors omitting blood pressure, classical risk factors plus pulse wave features, only pulse wave features, classical risk factors omitting blood pressure plus pulse wave features.
