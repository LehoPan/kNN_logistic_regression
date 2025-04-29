# kNN_logistic_regression

## Dependencies
Need Scikit Learn. Use command: ```pip install scikit-learn``` for windows.

## How to run
1. wdbc.data and wdbc.names are the original dataset files. We will be doing some preprocessing before training our models
2. Running ```MissingDataCheck.py``` will first check if there are any missing columns in the rows of data.
3. Running ```CleanData.py``` will remove the ID column as we will not be needing it, as well as one-hot encoding the Malignant/Benign data column in numerical 1's and 0's respecitvely. The data will be logged in ```cleaned.data``` and the labels into ```lables.data```.
4. Finally to properly scale the data for training we run ```FeatureScale.py``` which will scale all the data columns and output them to ```scaled.data```.
5. We have two models to run, ```kNN.py``` is the kNN model and ```LogisticRegression.py``` is the logistical regression model. Both split the data to 80/20 for training/testing set. 