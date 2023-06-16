#Imports functions from flask and functions as well as imports numpy and pandas
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from functions import *

#Creates the app
app = Flask(__name__)

#Page that contains title as well as navigation buttons
@app.route("/")
def title():
    return render_template("welcome.html")

#Page where user creates their own listing
@app.route("/createListing")
def createListing():
    return render_template("createListing.html")

#Page where user can see all the listings as well as search for specific ones
@app.route("/searchListing")
def searchListing():
    listings = getListings()
    listings = listings.drop_duplicates()
    return render_template('searchListing.html', dataframe=listings)

#Page where the app displays the dataframe containing only the listings they want
@app.route('/filteredListing',methods = ['POST', 'GET'])
def filteredListing():
   category = request.args.get('category', '')
   title_course_price = request.args.get('title_course_price', '')
   
   listings = getListings()
  
   if category == 'Title':
     filtered = searchTitle(listings, title_course_price)
   elif category == 'Course':
     filtered = searchCourse(listings, title_course_price)
   else:
     filtered = searchPrice(listings, title_course_price)

   filtered = filtered.drop_duplicates()
     
   return render_template('filteredListing.html', dataframe=filtered, category=category, title_course_price=title_course_price)

#Page where the app confirms that the user has added a listing
@app.route('/listingConfirmed',methods = ['POST', 'GET'])
def listingConfirmed():
   title = request.args.get('title', '')
   authorPublisher = request.args.get('authorPublisher', '')
   price = request.args.get('price', '')
   condition = request.args.get('condition', '')
   course = request.args.get('course', '')
   name = request.args.get('name', '')
   email = request.args.get('email', '')

   global listings

   createNewListing(title, authorPublisher, price, condition, course, name, email)

   return render_template('listingConfirmed.html', title=title, authorPublisher=authorPublisher,  price=price, condition=condition, course=course, name=name, email=email)
   
#Runs the app
if __name__ == "__main__":
   # Launch the Flask dev server
  app.run('0.0.0.0', 8080)

