# HGNx-stage3
This is the third stage of the HGNx project. It is a web application I created using Python(Flask). The simple web app has /api endpoint that performs CRUD operations on a database. The database I used is AWS RDS (MYSQL).

The web app is deployed on render. The link to the endpoint is https://hgnx3.onrender.com/api.

# Installation
To run the web app locally, you need to have python3 installed on your machine. You can download python3 from https://www.python.org/downloads/. You also need to have pip installed on your machine. You can download pip from https://pip.pypa.io/en/stable/installing/.

## Clone the repository
```
git clone https://github.com/CyrusNchege/HGNx-stage3
```
```
cd HGNx-stage3
```
## Install dependencies
```
pip install -r requirements.txt
```
## Run the app
```
flask run
```
# API Documentation
The API has the following endpoints:
## GET /api
This endpoint returns all the data in the database.

## GET /api/user_id
This endpoint returns a single row in the database. The id is passed as a parameter in the url.

## POST /api
This endpoint adds data to the database. The data is sent as a JSON object in the request body. The JSON object should have the following keys: name, age

Example:
```
{
    "name": "Cyrus",
    "age": 23
}
```
## PUT /api/user_id
This endpoint updates data in the database. The data is sent as a JSON object in the request body. The JSON object should have the following keys: name, age

Example:
```
{
    "name": "Cyrusupdated",
    "age": 23
}
```
## DELETE /api/user_id
This endpoint deletes a row in the database. The id is passed as a parameter in the url.




