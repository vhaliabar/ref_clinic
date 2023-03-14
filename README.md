# EPAM_CLINIC PROJECT
[![Build Status](https://app.travis-ci.com/vhaliabar/ref_clinic.svg?branch=main)](https://app.travis-ci.com/vhaliabar/ref_clinic)
<a href='https://coveralls.io/github/vhaliabar/ref_clinic?branch=main'><img src='https://coveralls.io/repos/github/vhaliabar/ref_clinic/badge.svg?branch=main' alt='Coverage Status' /></a>
[![Flask](https://img.shields.io/badge/flask-blue.svg)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/mysql-blue.svg)](https://www.mysql.com/)
[![Pylint](https://img.shields.io/badge/pylint-blue.svg)](https://www.pylint.org/)

This is  **Flask-based** application, created for panients and hospital team to support medical processes! 

## Instalation
**To run the application locally, follow these steps:**
1. Clone github repository:
```
> git clone https://github.com/vhaliabar/ref_clinic.git
```
2. Create a virtual environment:
  ```
  > cd ref_clinic
  > python3 -m venv venv:
  ```
3. Activate virtual environment:
  ```
  > source venv/Scripts/activate
  ```
4. Install the required dependencies:
  ```
  > pip install -r requirements.txt
  ```
5. Set up the database:

  **First of all, you need to install MySQL server.
  <br> Next, configure MySQL connection by runing create_mysql.py file**
  ```
 >python ref_clinic/migrations/create_mysql.py
  ```
  **Secondly, create environmental veriable to support Flask app:**
  ```
  > $env:FLASK_APP = "ref_clinic"
  ```
6. Start application:
  ```
  > flask run
  ```
  You can specify port # using -p flag, as well as app name using --app <app name><br>
  <br>
  You can also run Python WSGI HTTP Server Gunicorn, for this run the following command:
  ```
  > gunicorn ref_clinic:main
  ```
  
## Usage
To use the application, open a web browser and navigate to http://localhost:5000. Most effects of using app you can obtain, use the following links:
 1. http://localhost:5000/doctor_list - if you want to retrieve all doctors from a database.
 2. http://localhost:5000/create_doctor - if you want to add new doctor to a database.
 3. http://localhost:5000/delete_doctor/1 - if you want to delete first doctor from a database.
 
There are only examples of how to use this application, you can find the rest of the links in the documentation folder

## Contributing
Contributions to the ref_clinic repository are welcome! To contribute, please follow these steps:

  1.Fork the repository.
  
  2.Create a new branch for your changes:
  ```
  >git checkout -b my-new-feature
  ```
  3.Make your changes and commit them:
  ```
  >git commit -am 'Add some feature'
  ```
  4.Push your changes to your fork:
  ```
  >git push origin my-new-feature
  ```
  5.Create a new pull request on the main repository
  
## Credits
**This project was created by [Viktor Haliabar](https://github.com/vhaliabar/) as part of the EPAM Python Course.**


