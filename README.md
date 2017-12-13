# uszipkml


This repo is collection of the United States zip code area KML files . These files can be used with google maps API
to plot the respective area of the zip code on google maps.

All files are contained in the kml_files directory. With file name as zipcode + .kml

Python 2 program is used to extract this information from kml.csv file , Which is the main source of this information 
and also included in this repo

csvtokml.py is a file that is used to extract each and every .kml files in kml_files directory 


------------------------------------------------------------------------------------------------------------------------------
NOTE : 
      you can clear content of kml_files directory and then run csvtokml.py using
      
      $python csvtopy.py  
      
      to produce all those files again in kml_files directory again
