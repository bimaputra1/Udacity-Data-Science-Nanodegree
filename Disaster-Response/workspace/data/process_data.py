import sys
import pandas as pd
import numpy as n
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    '''
    Functions: 
        Load data from the csv
    
    Args:
        messages_filepath: the path of the messages.csv files that will be processed
        categories_filepath: the path of the categories.csv files that will be processed
        
    Returns: 
        merged_df (DataFrame): merged messages and categories DataFrame
    '''
    # load messages and categories
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    
    # merge two dataframes into one
    df = pd.merge(messages, categories, on = 'id')
    
    return df

def clean_data(df):
    '''
    Functions: 
        Cleaning and Preparing data by:
        - Renaming column
        - Replace categories column value into number
        - Remove Duplicate
    
    Args:
        df: DataFrame after preprocessed
        
    Returns: 
        cleaned_df (DataFrame): cleaned data frame
    '''
    
    # split the categories columns into multiple columns
    categories = df['categories'].str.split(';', expand=True)

    # rename columns
    row = categories.iloc[1]
    category_colnames = row.apply(lambda x: x.split('-')[0])
    categories.columns = category_colnames

    # replace original values into 1 and 0
    for column in categories:
        categories[column] = categories[column].apply(lambda x: int(x.split('-')[1]))

    # replace the old categories column
    df.drop('categories', axis = 1, inplace = True)
    df = df.join(categories)
    
    # drop duplicates
    df = df.drop_duplicates()
    
    return df


def save_data(df, database_filepath):
    '''
    Functions: 
       Save processed data to sqlite database
       
    Args:
        df: DataFrame after preprocessed
        database_filepath: database location
        
    Returns: 
        None
    '''
    engine = create_engine('sqlite:///' + database_filepath)
    df.to_sql('DisasterResponse', engine, index=False)
    


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()