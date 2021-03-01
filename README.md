### Intro 
This is a presentation of a linear regression model that can predict the value on an appartment based on a set of variables.

### Technologies

* Python 3.8.5
* Flask
* sklearn 
* pandas
* pytest

Hosting: DigitalOcean


### Usage
Make HTTP GET request to http://192.241.130.85:5000/predict and in the body send the data in the following format
```json
{
   "1":{
      "1":-117.130000,
		  "2":-118.040000
   },
   "2":{
      "1":32.700000,
		  "2":33.760000
   },
   "complexAge":{
      "1":42.000000,
		  "2":25.000000
   },
   "totalRooms":{
      "1":1210.000000,
		  "2":4061.000000
   },
   "totalBedrooms":{
      "1":292.000000,
		  "2":545.000000
   },
   "complexInhabitants":{
      "1":945.000000,
		  "2":1623.000000
   },
   "apartmentsNr":{
      "1":258.000000,
		  "2":527.000000
   },
   "8":{
      "1":0.899100,
		  "2":7.157200
   }
}
```