#Imports numpy and pandas
import numpy as np
import pandas as pd

#Returns the listings dataframe
def getListings():
  return listings

#Classifies each listing as $, $$, $$$ based on their price
def expensive(price):
    if price < 20:
        return '$'  
    elif price >= 20 and price < 40:
        return '$$'
    else:
        return '$$$'

#Allows a user to create their own book listing
def createNewListing(title, authorPublisher, price, condition, course, name, email): 

  global listings
  
  newListing = pd.Series({"Title": title, "Author/Publisher":authorPublisher, "Price": int(price), "Condition": condition, "Course": course, "Name": name, "Email": email, "Expensive": expensive(int(price))})

  listings = pd.concat([listings, newListing.to_frame().T], ignore_index=True)

  listings.to_csv('input_data.csv',index=False)
    

#Allows a person to search for books used in a certain course
def searchCourse(df, key):
  filtered = df[df['Course'] == key]
  return filtered

#Allows a person to search for books by title
def searchTitle(df, key):
  filtered = df[df['Title'] == key]
  return filtered

#Allows a person to search for books based on the price range
def searchPrice(df, key):
  filtered = df[df['Expensive'] == key]
  return filtered

#Reads in the csv, casts the Price column to int, and applies the expensive method to the Price column
listings = pd.read_csv('input_data.csv')
listings['Price'] = listings['Price'].astype(int)
listings['Expensive'] = listings['Price'].apply(expensive)
