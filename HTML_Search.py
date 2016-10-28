import urllib2,os

class bColour:
    WARNING = '\033[91m'
    HIGHLIGHT = '\033[1;37;41m'
    ENDC = '\033[0m'


print(bColour.HIGHLIGHT + "#########################################################" + bColour.ENDC)
print(bColour.HIGHLIGHT + "#              --Python HTML Flag Finder--              #" + bColour.ENDC)
print(bColour.HIGHLIGHT + "#                      By: SCOTTLB                      #" + bColour.ENDC)
print(bColour.HIGHLIGHT + "##########################2016###########################" + bColour.ENDC  + '\n')

#Array to look for things
SEARCH = []

#Get current path to find txt file
current = os.path.dirname(os.path.realpath(__file__))
#open the file
myFile = open(current + "/Search_Terms.txt","r")
#read each line
for line in myFile:
    #add the search term to the array
    SEARCH.append(line)

#Python 2.7 sucks
input = raw_input

#get URL input
URL = input("Enter the target URL: ")
print("\n")
#request the html
req = urllib2.Request(URL)
response = urllib2.urlopen(req)
page = response.readlines()

#line number counter
counter = 1
#occurance Counter
occurCounter = 0
#look through each line
for line in page:
    #look for each search term
    for x in SEARCH:
        #check if its a substring
        if(x in line):
            #print if its found
            print("FOUND " + x +" IN LINE: " + str(counter) + " :" +  bColour.WARNING + line.strip('\t\n') + bColour.ENDC)
            #Increment YO
            occurCounter += 1
    #increment that bitch        
    counter += 1
print("\n" + bColour.HIGHLIGHT + str(occurCounter) + " matches were found!" + bColour.ENDC)