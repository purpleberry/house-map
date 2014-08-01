import csv
import json
import urllib.request

total = 0
count = 0


perpostcode = {}

# Open the house price data and populate the house price dictionary
with open('pp-monthly-update-new-version.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        postcode = row[3]
        area = postcode[:postcode.find(" ")]
        if area not in perpostcode: # create a new dictionary entry and zero it
            perpostcode[area] = {'total': 0, 'count': 0, 'avprice': 0}
        perpostcode[area]['total'] += int(row[1])
        perpostcode[area]['count'] += 1
        total = total + int(row[1])
        count = count + 1

# calculate the average values in each area and update the dictionary
#for area in perpostcode:
    #perpostcode[area]['avprice'] = perpostcode[area]['total'] / perpostcode[area]['count']
    #print (area, perpostcode[area]['avprice'],perpostcode[area]['count'])
total = 0
count = 0
with open('2014-04-cambridgeshire-street.csv', newline='') as policedatafile:
    spamreader = csv.reader(policedatafile, delimiter=',', quotechar='"')
    for row in spamreader:
        lat=row[5]
        lng=row[4]
        if lat != 'Latitude':
            #print(lat)
            #print(lng)
            #lat =51.590524
            #lng = -1.415645
            latlongurl = 'http://uk-postcodes.com/latlng/'+lat+','+lng+'.json'
            print(latlongurl)
            postcodecsv = urllib.request.urlopen(latlongurl)
            postcode = json.loads(postcodecsv.read().decode('utf8'))['postcode']
            print(postcode)
            postcodedata = csv.reader(postcodecsv, delimiter=',', quotechar='"')
            for postcoderow in postcodedata:
                print(postcodedata.__next__()[0])
        

        #total = total + int(row[1])
        
        



lat =51.590524
lng = -1.415645
latlongurl = 'http://uk-postcodes.com/latlng/'+str(round(lat,9))+','+str(round(lng,9))+'.csv'
postcodecsv = urllib.request.urlopen(latlongurl).read()        
print(postcodecsv)


