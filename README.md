# bike_availability
Checks if bike is available fulfilling requirements
## Get Started
Create a new virtual environment, and run `pip install -r requirements.txt`. Activate it afterwards. To run the script, simply `python canyon.py`.

If there are road bikes in stock when executing this script, the output will look like:
```
Bike Requirements:
        bike size: M
        models of interest: [‘ultimate’, ‘aeroad’, ‘inflite’]
        classes of interest: [‘cf’, ‘cfr’]
Following bikes fulfilling requirements are in stock
---------
Inflite CF SL 8
https://www.canyon.com/nl-be/road-bikes/cyclocross-bikes/inflite/cf-sl/inflite-cf-sl-8/3022.html?dwvar_3022_pv_rahmenfarbe=BU%2FPK
```

To define your own bike requirements: edit the main section in the script.

You can always attach notification triggers to the output of this script for full experience. 

## TODO
- [ ] Add an argument parser
- [ ] Add dockerfile
- [ ] Add suggestions how to add email notifications or desktop notifications
- [ ] Choose the county of Canyon website
- [ ] Add other classes of bikes (besides road bikes)

## Disclaimer
This is meant a fun side project.
