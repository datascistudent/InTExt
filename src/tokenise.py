__author__ = 'gkannappan'

from nltk.corpus import stopwords
#from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import PorterStemmer, WordNetLemmatizer

import nltk
import re



from collections import Counter


#Function for converting Dictionary to File

def write_report(r, filename):
    with open(filename, "wb") as input_file:
        for k, v in r.items():
            line = '{}, {}, \n'.format(k, v)
            input_file.write(line)
        input_file.close()

#
#doc = "Service road opposite to manyata tech park is at a horrible condition. in the name of maintenance work and drainage work thiBs ate stalled ad it is from past few months. at least if the service road is fixed the traffic can move easily. People just dump their garbage into this open drain without even thinking about the drainage getting blocked. because of this mosquitoes can breed in this and create health issues. I request the concerned authorities to take necessary action in this matter. Signal jump - Violating lane discipline at K. Kamaraj Road, Bengaluru, Karnataka 560042, IndiaTraffic @tinfactory is so much find sum solution No roads are laid in Kunnappa road Street light are not working in tippasandra road.... I am one of the resident of Mahatma Gandhi Nagar Slum (Ward no 75) where we as a group of 250 to 300 families residing from Past 40 to 50 years but now recently there was an Apartment got established &amp; they are asking us to let out the entire area as they feel that Slum wont look good near Apartment itseems but through this i request Our Honourable  MLA sir Mr Gopalaiah Honorable Corporator Mr. Shivaraju to help us out in this regards. Every month the garbage Incharge lady collects Rs.20/- illegally, When I ask them why we need to give are u not getting salary for the service done, and more she is not a poura karmica and she says everybody is giving if u not give garbage will not be collected from your house and secondly the road of 7th cross is littered with tree leaves and even after requesting the pourakarmika lady to clean it, she refuses, request to take note of this and illegal monthly garbage money collection (ie.,tax paid includes annual garbage cess) to take suitable action.Hi Sir/Madam, We are residents of keerthi heights,belthur which is near HDFC Bank Kadugodi Branch. Our main road(40 ft main road) is in bad shape and which needs to be tared . Because of the bad road kids and elderly people are facing so many issues starting from back pain to breathe issues. Kindly help us in fixing this issue. Sign boards that give the location information to non-residents have been defaced with posters."

file_content = open("/Users/gkannappan/Desktop/In24Hrs/root/Processed_File_Desc.txt").read()
#

file_content = file_content.lower()

#tokenize
#
#words = nltk.word_tokenize(doc)
words = nltk.word_tokenize(file_content)


#Define and Remove Stop words in English
stop = set(stopwords.words('english'))
stopwordsfree_words = [word for word in words if word not in stop]

#Stemming


#stmr = LancasterStemmer()

#file_content = stmr.stem(file_content)

#porterstmr = PorterStemmer()

#stemmed = " ".join([porterstmr.stem(i) for i in file_content.split()])

#print stemmed


#words = nltk.word_tokenize(stemmed)

#Implement word count
counts = Counter(stopwordsfree_words)
file = '/Users/gkannappan/Desktop/In24Hrs/root/dicttofile.txt'

#print counts

write_report(counts, file)







