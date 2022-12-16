# Hello there!
This is a project involves in training machine learning models to predict the susceptibility of microbials against emperical antibiotics in the current anti-infectious guidelines.
## Training data
The training data was recorded from medical records of inpatients in a hospital in Ho Chi Minh City, Ethical approval was granted by the Research Ethics Committee at UMC HCMC (REC Approval Number: 34/GCN-HDDD).
The project is undergoing therefore the original dataset can not be published at the moment. I attached "Part of data.csv" for illustration purposes.
## Imbalanced dataset and processing strategies
In addition, due to high antimicrobial resistant rate (AMR), we anticipated imbalance of resistance data (samples with resistant pathogens outnumbered those with susceptible ones for tested antibiotics). Therefore, data resampling was conducted to address these issues. Two different data resampling techniques, undersampling and oversampling, were compared to identify which technique provided optimal results.
Five different ML algorithms:  were used to predict antibiotic susceptibility of five bacteria groups. The data set was randomly split into two sets: 80% for training and 20% for testing. Each ML algorithm was evaluated using the following metrics: accuracy from the training and test sets, and area under the receiver operating characteristic curve (AUROC) from the test sets. Ten-fold cross-validation (data were randomly partitioned into ten parts, with one part randomly held out for error evaluation) was also applied for the training sets to improve the prediction of the algorithms. We used the Scikit-Learn software package for data analysis (Scikit-learn version 1.0.2. https://scikit-learn.org/stable/).
1. Logistic Regression (LR)
2. Support Vector Machine (SVM)
3. Decision Tree (DT)
4. Random Forest (RF)
5. eXtreme Gradient Boosting (XGBoost),

Sampling methods to rebalance the data: Random oversampling and Random Undersampling was employed from https://imbalanced-learn.org/

## Variables
10 variables from the medical records were selected. These included age, gender, province of residence, diagnosis (type of infection), comorbidities, prior hospitalization, number of hospital admissions, sample type, pathogens, and antibiogram (including susceptibility results).

## Outcome
Resistant (R) or Sensitive (S)

