# hackathon2019
We have built a cgportal microservice which registers a student with his name , email and resume file.
 Once the user registers we extract the skills, phone-number, email, from the submitted resume.
 The student can be searched using name via the seaarch tab in the UI.
 We have also incorportated elasticsearch into the microservice, once the user registers we add a data point for this into the elasticsearch server
 The elasticsearch  allows to look for a particular skill, mail, etc.
 The search result supports a download link for the resume.
 
 TechStack 
 1) Bootstrap for front end
 2) Python flask for server
 3) MongoDb as database (cloud instance)
 
 Prerequisites for the application
 1) Windows Machine
 2) Python 3.7 64 bits
	https://www.python.org/downloads/windows/
 3) Visual Studio build tools 2015 or later installed
 4) Elastic search setup from 
	https://www.elastic.co/downloads/elasticsearch
	and run the server using <elasticsearch_folder>\bin\elasticsearch
		
 Clone the project from git using
 git -clone https://github.com/nikash3/hackathon2019.git
	
 Goto hackathon2019 folder and run
 projectSetup.bat
