__author__ = 'gkannappan'

'''
Consolidating the scripts developed for hackathon

Carving out the code to scrap "web-crawler.py" the website outside of this master code
'''

import urllib
import re
from bs4 import BeautifulSoup
import unicodedata
import csv


#paragraphs = []

'''
This block of code is used to read the html file and pick the tags (excluding timer) and create a file out of it
'''

###The input file to be modified at the runtime
html_doc = '/Users/gkannappan/Documents/Intuit/Analytics Playground/In24Hrs/Test.html'


soup = BeautifulSoup(open(html_doc))

for chunks in soup.findAll(True,{"class":["modern-pictograms-add-photo", "label-agency", "ward-name", "address", "header-title3", "brief-complaint-description","modern-pictograms-add-photo"]} ):
#for chunks in soup.findAll(True,{"class":["modern-pictograms-add-photo","timer"]}):

# get text
    lines1 = chunks.get_text()
    lines = re.sub(r'[^\x00-\x7F]+',' ', lines1)
    lines = re.sub("[^a-zA-Z0-9\s]","", lines)
    lines = lines.rstrip('\n')

 # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in lines.splitlines())

# break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

# drop blank lines
    text = '|'.join(chunk for chunk in chunks if chunk).encode('utf-8')

###Output file location to be modified during the runtime
    target = open('/Users/gkannappan/Documents/Intuit/Analytics Playground/In24Hrs/DeleteTags.txt', 'a')
    target.truncate()
    if text == 'A':
        target.writelines('\n')

    target.write(text)
    target.write('|')
    target.close()


#for chunks in soup.findAll(True,{"class":["modern-pictograms-add-photo", "label-agency", "ward-name", "address", "header-title3", "brief-complaint-description","modern-pictograms-add-photo"]} ):
for chunks in soup.findAll(True,{"class":["modern-pictograms-add-photo","timer"]}):

# get text
    lines1 = chunks.get_text()
    lines = re.sub(r'[^\x00-\x7F]+',' ', lines1)
    lines = re.sub("[^a-zA-Z0-9\s]","", lines)
    lines = lines.rstrip('\n')

 # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in lines.splitlines())

# break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

# drop blank lines
    text = '|'.join(chunk for chunk in chunks if chunk).encode('utf-8')

###Output file location to be modified during the runtime
    target = open('/Users/gkannappan/Documents/Intuit/Analytics Playground/In24Hrs/DeleteTimer.txt', 'a')
    target.truncate()
    if text == 'A':
        target.writelines('\n')

    target.write(text)
    target.write('|')
    target.close()


#ConcatenateColumns.py
###The input file to be modified at the runtime
fp =  open('/Users/gkannappan/Documents/Intuit/Analytics Playground/In24Hrs/DeleteTags.txt')

###Output file location to be modified during the runtime
target = open('/Users/gkannappan/Documents/Intuit/Analytics Playground/In24Hrs/Delete1.txt', 'w+')
target.truncate()

###The input file to be modified at the runtime
with open('/Users/gkannappan/Documents/Intuit/Analytics Playground/In24Hrs/DeleteTags.txt', mode = 'r', buffering = -1) as f:
    reader = csv.reader(f, delimiter='|', skipinitialspace=False)
    for k in fp:

        k=k.strip('\t')
        k=k.strip('\n')
        first_row = next(reader)
        num_cols = len(first_row)
        line = k.split('|')
        line1 = [' '.join(map(str,line[6:num_cols]))]
        new_line = line[1:6]+line1
        print >> target, new_line

fp.close()
f.close()
target.close()


fp =  open('/Users/gkannappan/Documents/Intuit/Analytics Playground/In24Hrs/DeleteTimer.txt')

###Output file location to be modified during the runtime
target = open('/Users/gkannappan/Documents/Intuit/Analytics Playground/In24Hrs/Delete2.txt', 'w+')
target.truncate()

###The input file to be modified at the runtime
with open('/Users/gkannappan/Documents/Intuit/Analytics Playground/In24Hrs/DeleteTimer.txt', mode = 'r', buffering = -1) as f:
    reader = csv.reader(f, delimiter='|', skipinitialspace=False)


    for k in f:
        k=k.strip('\t')
        k=k.strip('\n')

        #print first_row
        num_cols = len(k)
        line = k.split('|')
        line1 = [' '.join(map(str,line[1:num_cols]))]
        #new_line = line[1]+line1
        #new_line = line[1]
        new_line = line1
        print >> target, new_line

fp.close()
f.close()
target.close()

with open('/Users/gkannappan/Documents/Intuit/Analytics Playground/In24Hrs/Delete2.txt', mode = 'r') as f1, open('/Users/gkannappan/Documents/Intuit/Analytics Playground/In24Hrs/Delete1.txt', 'r') as f2, open('/Users/gkannappan/Documents/Intuit/Analytics Playground/In24Hrs/DeleteFinal.txt', 'a') as f3:
    writer = csv.writer(f3)
    r1, r2 = csv.reader(f1),csv.reader(f2)
    while True:
        try:
            writer.writerow(next(r1)+next(r2))
            print 'write'
        except StopIteration:
            break


with open('/Users/gkannappan/Documents/Intuit/Analytics Playground/In24Hrs/DeleteFinal.txt', 'r') as f4, open('/Users/gkannappan/Documents/Intuit/Analytics Playground/In24Hrs/DeleteFinal2.txt', 'w') as f5:
    data = f4.read()
    data = data.replace("[", "")
    data = data.replace("]", "")
    data = data.replace(",", "|")
    data = data.replace("'", "")
    #data = data.replace("\\", " ")
    f5.write(data)


'''
One more step here (similar) to merge Lat Long
To create Lat Long file is a standalone step
'''


'''
Classification Step

'''

Stray_Dogs = ["steet dogs", "dogs", "stray"]
Garbage = ["dumping garbage"]

Road_PotHoles = ["potholes", "bad stretch"]
Road_Encroach = ["narrow", "narrow road"]
Road_Bad = ["lay good road", "pain to drive", "pain to ride"]

Traffic_Parking = ["parking", "parked"]

Street_Lights = ["street light", "dark", "badly lit", "lit"]
Power_Cut = ["cut power", "power cut", "power outage", "powercut"]

Drainage = ["no drainage", "overflowing drainage", "sewage", "overflowing sewage"]
Water = ["facing serious water problem", "water shortage", "water supply"]

BBMP_Road_Damage = ["damaged road", "Roads are completely damaged", "roads are damaged", "damaged roads", "Roads are so so horrible ", "roads are horrible", "horrible roads", "road damaged", "repair road", "road repair", "repair roads", "pathetic road", "road is becoming bad", "road was digup", "road is in bad condition", "damaged the road", "roads here were never", "maintain basic road infra", "roads are so so horrible", "worst road"]
BBMP_Road_Pothole = ["Big Potholes", "Potholes", "Pothole", "Potholed", "pot hole", "pot holes", "pot holed", "poteholes", "potehole", "pathole", "manhole", "man hole", "man holes", "manholes", "potholes", "pothole", "crater", "pathholes", "big hole"]
BBMP_Road_Encroachment = ["encroachment", "road encroachment", "encroachment of road", "encroachment of roads"]
BBMP_Road_RoadMaintenance = ["not having any road", "no road", "no access", "no roads", "dangerous road", "road maintenance", "muddy roads", "muddy road", "damaged footpath", "terrible road", "bad road", "bad roads", "Road is Very Pathetic", "cutting the Road", "bad job of patching", "road work", "no proper road", "Roads are in very poor condition", "bumpy ride", "Pathetic Dangerous", "no tar roads", "cement road", "roads were dug", "road is not good", "road is in very bad condition", "due to roads", "roads and gutter are dug up", "new roads", "road had neen cut", "roads are maintained", "asphalted", "road is cut", "road dug for some work", "road maintainance", "dug the whole road", "no tar in the road"]
BBMP_Animals_StrayAnimals = ["stray dogs", "dog bite", "stray dog", "cow", "buffalo", "pig menace", "rats", "pigs", "mosquito", "street dogs", "dogs", "dog"]
BBMP_Cleanliness_Garbage = [ "Garbage Clean", "Garbage", "cleaned", "posters on traffic poles", "posters", "No collect garbage", "garbage collection", "garbages collect", "garbages collection", "throw waste", "put waste", "no single Garbage Collector", "no garbage Collector", "garbages and wastes", "dumping garbage", "garbage pickup", "Uncleared debris", "debris", "urination", "urine", "rubble", "garbage disposal", "plastic", "garbage", "garbage collection", "garbage dump", "Garbage not collected", "DUSTBINS", "dustbins", "garbage dump area", "throw wastage"]

BTP_Traffic_TrafficJam = ["road blocked", "traffic jam", "control the traffic", "control traffic", "traffic control", "traffic", "Traffic Control Room", "heavy traffic", "huge traffic", "chaotic junction", "speed barrier", "humps", "hump", "speed barriers", "barriers", "lane discipline", "traffic congestion", "traffic junction"]
BTP_Violation_Traffic = ["driving on footpath", "wrong direction", "one way", "one-way", "wrong side", "no entry", "no-entry", "without helmet", "no helmet", "helmetless", "helmet Less", "jumping signal", "signal jump", "footpath riding", "traffic violation", "wrong side", "breaking the law", "breaking signal", "breaking law", "traffic offence", "not wearing helmet", "Riding Without A Helmet", "wrong way", "overspeeding", "Over speeding", "Speeding", "Over Speeding" "OverSpeeding", "Helmet", "Riding Without"]
BTP_Violation_Parking = ["Parking On Footpath", "parked on foot path", "Footpath Parking", "parking", "obstructive parking", "no parking", "stopping", "illegal parking", "stopped"]

BESCOM_Electricity_PowerOutage = ["no power", "power cut", "power outage", "power supply issue", "voltage", "power goes down", "huge power failure", "power problem"]
BESCOM_Lights_Streelight = ["street light", "no streetlight", "streetlight","no street light","no streetlights", "every lights are working"]
BESCOM_Infrastructure_Maintenance = ["electric cable", "electrical poles"]

BMTC_Experience_RudeBehavior = ["Rude conductor", "rude driver", "rude behavior", "misbehavior", "rashy", "rash drive", "rashily", "driven rashily", "fare", "improper fare", "abusive language", "abuse", "harrased", "conductors"]
BMTC_Infrastructure_BusShelter = ["Bus shelter", "waiting shelter", "bus stop", "busstops", "busstop", "bus shelter"]
BMTC_Buses_MoreBuses = ["Need more Bmtc buses", "Need more buses", "more buses", "more bus", "irregular buses", "irregular bus", "increase frequency", "more frequency", "less buses", "less bus", "limited buses", "few buses", "limited bus", "few bus", "increase in bus", "no bus", "no buses", "introduce buses", "need more bmtc buses", "no proper bus service", "need extra buses", "need buses", "no direct bus", "crowded buses"]
BMTC_Others_Other = ["bmtc"]

BWSSB_Water_Problem =["inlet pipes", "water problem", "drinking water", "water connection", "waterman", "water supply", "ground water level", "wastage of water", "overflow of fresh water", "water logging", "heavy water clogging"]
BWSSB_Sewage_Problem=["sanitary problem", "sewage", "drain", "sewage lines", "water get accumulated", "drainage", "proper drainage system", "sanitary wastage"]


KSPCB_Pollution_Air = ["smoking", "air pollution", "dust", "mud and dust", "pollutes", "pollution", "pollute", "burning of plastic", "burning", "set on fire", "polluting", "fire", "wood", "dusty"]
KSPCB_Pollution_Noise = ["loud speaker", "frequency noise", "loud music", "sound", "high noise", "noise", "horn"]

###Output file location to be modified during the runtime
fw = open('/Users/gkannappan/Desktop/In24Hrs/root/Classified_Final.txt', 'w+')
#fp =  open('/Users/gkannappan/Desktop/In24Hrs/root/Processed_File_Togo.txt')

###The input file to be modified at the runtime
fp = open('/Users/gkannappan/InTExt/data/File_with_Lat_Long.txt')



#iterates the content of the Verbatim (text1) using a for loop

print  >>fw, "DATE|CIVIC_BODY|CATEGORY|SUB_CATEGORY|AREA|LAT|LONG"
for k in fp:
    k = k.split('|')
    k2 = k[6]
    k0 = k[0]
    k3 = k[3]
    k7 = k[7]
    k8 = k[8]
    #print k2

#print k
#Remove Punctation Marks and Convert to LowerCase


    k2 = re.sub(r'[^\x00-\x7F]+',' ', k2)
    k2 = re.sub("[^a-zA-Z0-9\s]","", k2).lower()
    k2 = k2.strip('\r')
    #print k2


    #print any(l in k for l in One_Run) #This ll return True or False based on the keywords' presence in Verbatim
    #if any(l in k for l in Run_One) and not any(l in k for l in Extras_NoBall) and not any(l in k for l in Extras_Bye) and not any(l in k for l in Extras_LegBye):
    if any(l in k2 for l in BBMP_Road_Damage):
        print >> fw,"{}|BBMP|Road|Damage|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BBMP_Road_Pothole):
        print >> fw,"{}|BBMP|Road|Pothole|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BBMP_Road_Encroachment):
        print >> fw,"{}|BBMP|Road|Encroachment|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BBMP_Road_RoadMaintenance):
        print >> fw,"{}|BBMP|Road|Maintenance|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BBMP_Animals_StrayAnimals):
        print >> fw,"{}|BBMP|Animals|StrayAnimal|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BBMP_Cleanliness_Garbage):
        print >> fw,"{}|BBMP|Cleanliness|Garbage|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BTP_Traffic_TrafficJam):
        print >> fw,"{}|BTP|Traffic|TrafficJam|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BTP_Violation_Traffic):
        print >> fw,"{}|BTP|Violation|Traffic|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BTP_Violation_Parking):
        print >> fw,"{}|BTP|Violation|Parking|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BESCOM_Electricity_PowerOutage):
        print >> fw,"{}|BESCOM|Electricity|PowerOutage|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BESCOM_Infrastructure_Maintenance):
        print >> fw,"{}|BESCOM|Infrastructure|Maintenance|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BESCOM_Lights_Streelight):
        print >> fw,"{}|BESCOM|Lights|Streelight|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BMTC_Experience_RudeBehavior):
        print >> fw,"{}|BMTC|Experience|RudeBehavior|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BMTC_Infrastructure_BusShelter):
        print >> fw,"{}|BMTC|Infrastructure|BusShelter|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BMTC_Buses_MoreBuses):
        print >> fw,"{}|BMTC|Buses|MoreBuses|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BMTC_Others_Other):
        print >> fw,"{}|BMTC|Others|Other|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BWSSB_Water_Problem):
        print >> fw,"{}|BWSSB|Water|Problem|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BWSSB_Sewage_Problem):
        print >> fw,"{}|BWSSB|Sewage|Problem|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in KSPCB_Pollution_Air):
        print >> fw,"{}|KSPCB|Pollution|Air|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in KSPCB_Pollution_Noise):
        print >> fw,"{}|KSPCB|Pollution|Water|{}|{}|{}".format(k0, k3, k7, k8)
    else:
        print >> fw,"{}|Other|Other|Other|{}|{}|{}".format(k0, k3, k7, k8)
