# Fish market classification 
This application will predict the species of fishes based on the given dimensions such as Weight, Vertical Length, Diagonal Length, Cross length, Height and width. 

## Dataset Details 
The dataset used to train model is taken from Kaggle. It contains 7 common species of fishes in fish market sales. Dataset has 159 rows and 7 columns. It does not contain any nill values. 

## Approach
To perform classification of species, logistic regression model is used. It has 85.41% accuracy for this particular dataset. 

## Libraries required to install 
1) Numpy
2) Scikit learn
3) Pandas
4) Matplotlib

## Files: 
1) Fish_market_classification.ipynb 
- Importing, cleaning and preprocessing data followed by creation of logistic regression model and pickle file. 
2) Fish.csv 
- Dataset file. 
3) fish_classification.pkl
- Pickle file containing trained model.
4) flask_app.py
- Code to create flask application.
5) Procfile 
- To bind the project with Heroku app 
6) requirements.txt
- Containing required packages to run the application. 

## Running the application
1) Download the files including the dataset file. 
2) Use pickle file and run the trained model.

