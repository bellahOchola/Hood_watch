# Hood_watch

#### The application will allow a user to post a project he/she has created and get it reviewed by his/her peers. 18/01/2020

>[bellahOchola](https://github.com/bellahOchola)

## Description
This application simply allow users to login and join different hoods and also see the details of a single hood. They can also add businesses and even create posts in their respective hoods.They can view and also edit their profile.

## Setup/Installation Requirements
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/bellahOchola/Hood_watch.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Hood_watch 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations hood
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`. 

## Live Page

## User Story  
  
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## Technologies Used
* Python3.6
* Django 3.0
* HTML5
* Bootstrap4
* Google fonts
* CSS
* Heroku(Deployment)

## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  

## Support and contact details
If in any case you come across any isssues when using this application, kindly contact me.@[bellahkenya@gmail.com]. Incase of any contributions fork the repo add your contributions.

### License
This project is under the MIT license
Copyright (c) 2020  
Christabel ochola
