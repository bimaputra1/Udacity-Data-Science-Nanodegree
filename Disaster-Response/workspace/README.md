# Disaster Response Pipeline Project

## Project Overview

During a disater, informations can come from many source. One of the examples are millions of text communications that come from twitter. This massive amount of text generated are hard to filter and pull out to find the most important by a response organization.

To help this problems Figure Eight organization compose a dataset that include labelled twit messages related to disaster. Then here, I made a pipeline to process that data, build supervised learning model and then made a flask web app that can be used by emergencies response team to input a new message and get classification results in several categories. 

## Project Structure
    .
    ├── app     
    │   ├── run.py                           # Flask file that runs app
    │   └── templates   
    │       ├── go.html                      # Classification result page of web app
    │       └── master.html                  # Main page of web app    
    ├── data                   
    │   ├── disaster_categories.csv          # Dataset including all the categories  
    │   ├── disaster_messages.csv            # Dataset including all the messages
    │   ├── process_data.py                  # Data cleaning
    │   └── DisasterResponse.db              # Database as a results of preprocessed data
    ├── models
    │   ├── classifier.pkl                   # Model Generated
    │   └── train_classifier.py              # Train ML model           
    └── README.md

## Instructions
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

Note this project already have dabase and model on the data and models folder respectively. So you can skip step 1 if you're not have a new dataset.

## Web App Screenshot
Testing app with this messages 'Please help my area need food and water immediately!'
![Testing Apps](https://github.com/bimaputra1/Udacity-Data-Science-Nanodegree/blob/master/Disaster-Response/WebApp%20Snapshot.jpg)

![Main Page](https://github.com/bimaputra1/Udacity-Data-Science-Nanodegree/blob/master/Disaster-Response/Web%20Snapshot2.png)
