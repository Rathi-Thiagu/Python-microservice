
findSponsor.py : create webservice using flask
data.db        : model to store and write sponsor keyword from the request
requirements.txt : install dependencies
Dockerfile ,docker-compose.yaml : To create docker image
test.py          : post the requests to the webservice url
#docker_image.tar : contains the docker image which can be loaded and executed
.venv  create virtual environment

Run the code: 
	create the project and load the files from github link in VS code
	prerequisite: 
		Python 
		Docker 
		Postman application 
	Open the terminal 
	Start the virtual environment
		python -m venv .venv
	Run this command 
		docker-compose up 
	This will start the developement server providing the base service url (BASEURL)
	If not using docker :
		$env:FLASK_APP = "classifySponser.py"
		$env:FLASK_ENV = "developement"
		$env:FLASK_DEBUG=1
		flask run
		

Access the End points: 
There is no specific userInterface. 
Requests can be posted from the postman app or open another terminal and execute "python test.py" by editing the endpoint URL. 

api/vocab - get  : BASEURL/api/vocab 
api/vocab - post : BASEURL/api/vocab 
	Choose Body , raw , content-type : application/json
				{
				"vocab" : ['#influencer'] 
				}
api/prediction - post : BASEURL/api/prediction 
	Choose Body , raw , content-type : application/json
				{
				"post_text" : "#ad The food delicious here. Its a must try restaurant in San Jose"
				}
						
Responses can be seen from the response tab of postman app. 