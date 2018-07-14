""""""""""""""""""""""""""""""""""
03/04/18 TFabianac modified from:
02/28/18 TFabianac modified from:

#Matt Ardolino
#Indiana University
#D590 Topics in Data Science
#PubMed Project
#02/27/2018
"""""""""""""""""""""""""""""""""

#import packages

import pandas as pd
from pandas import DataFrame
import xml.etree.ElementTree as xml
from sklearn.feature_extraction.text import CountVectorizer
import glob
import re
import time
from nltk.corpus import stopwords

stop = stopwords.words("english")

def generateArray(root):
    # generate array
    csvarticles = []
    print ("Getting artices from XML files...")
    for article in root.iter("PubmedArticle"):

        titletest = article.find("MedlineCitation/Article/ArticleTitle")
        if titletest is not None:
            title = article.find("MedlineCitation/Article/ArticleTitle").text
        else:
            title = ''

        csvarticles.append(title)

    return csvarticles

def main():

#input xml file
    print ("Reading XML...")
    attributeList = []
    csvarticles = []

    # Pull the names of all the XML files in the directory that this python code is saved
    # If the XML files are saved in a different directory, replace the * with the directory location
    filenames = glob.glob('*.xml')  # pull all the xml files from one directory
    for filename in filenames:
        with open(filename, 'r', encoding='utf8') as content:
            tree = xml.parse(content)
            root = tree.getroot()
            xmlArticles = generateArray(root)
            for l in xmlArticles:
                csvarticles.append(l)

    print ("Our full articles look like this: {0}".format(csvarticles[0]))
    print("Vectorizing...")

# One step at a time
    cali = 0
    for i in range(100):
        t0 = time.clock()
        shortArticles = [word.lower() for word in csvarticles]
        shortArticles = ' '.join([word for word in csvarticles if word not in stop])
        shortArticles = [re.sub(r'\b\w{1,2} ', '', item) for item in csvarticles]
        shortArticles = [re.sub("[^ '\w]|[\d_]", ' ', item).strip()for item in csvarticles]
        vect = CountVectorizer(analyzer="word", max_features=5000)
        bag_of_words = vect.fit_transform(shortArticles)
        t1 = time.clock()
        cali += (t1 - t0)
    print("One Step at a Time: {0}".format(cali/100))
    print("The Features: {0}".format(vect.get_feature_names()))

# One Regex
    cali = 0
    for i in range(100):
        t0 = time.clock()
        shortArticles = [re.sub(r'\b\w{1,2} ', '', re.sub("[^ '\w]|[\d_]", ' ', item)).strip().lower()
                         for item in csvarticles if item not in stop]
        vect = CountVectorizer(analyzer="word", max_features=5000)
        bag_of_words = vect.fit_transform(shortArticles)
        t1 = time.clock()
        cali += (t1 - t0)
    print("One Regex: {0}".format(cali/100))
    print("The Features: {0}".format(vect.get_feature_names()))

# All in countvector
    cali = 0
    for i in range(100):
        t0 = time.clock()
        vect = CountVectorizer(analyzer="word", lowercase=True,
                                max_features=5000, stop_words='english', token_pattern=r'\b[a-zA-Z]{2,}\b')
        bag_of_words = vect.fit_transform(csvarticles)
        t1 = time.clock()
        cali += (t1 - t0)
    print("All in CountVector: {0}".format(cali/100))
    print("The Features: {0}".format(vect.get_feature_names()))

main()