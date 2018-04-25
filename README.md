"# Django-Simple-REST-API" 

This App has exposed all the available REST METHOD(GET, POST, PUT, DELETE). I have try to make it simple.
rests.py is the script in app directory where all the methods implemented.

app Name - Devices

	Model(Table Name) - router
	
	Model(Table Name) Structure - 
		sapid = models.CharField(max_length=20, unique=True)    
		hostname = models.CharField(max_length=16, unique=True)
		loopback = models.CharField(max_length=16)
		macaddress = models.CharField(max_length=24)

	module -
		rest_framework.renderers import JSONRenderer

	
GET:- 	http://localhost:8000/devices/api/routers
		
	
POST:- 	http://localhost:8000/devices/api/createrouters 

		Required parameters: sapid,hostname,loopback,macaddress
	   
PUT:-	http://localhost:8000/devices/api/updaterouters 

		Required parameters: hostname
		
		Optional parameters: sapid, loopback, macaddress

DELETE:- 	http://localhost:8000/devices/api/deleterouters 

			Required parameters: hostname
		
		
For other setting, Please check repo
