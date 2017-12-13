import csv

kml_initial = '<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2"><Placemark>'
kml_final = '</Placemark></kml>'
with open("kml.csv", 'r') as csvf:
    d_reader = csv.DictReader(csvf)
    for obj in d_reader:
        if obj['geometry'] != "":
            filename = "./kml_files/"+obj['ZIP']+'.kml'
            kml_intermidiate = obj['geometry']
            with open(filename, 'wa') as kmlfile:
                kmlfile.write(kml_initial+kml_intermidiate+kml_final)


                
        
    
     
