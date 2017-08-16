Please Note That this file is incomplete and is currently being updated. This project is also not complete and currently under development.

# What is Open Flask API ?

Open flask api is a simple API web-app based on ReST API Architecture and programmed in Python-3 using flask microframework. It is created for begginers to understand the basics of creating a ReST API in Python.It can also be used as a template to create your new APIs
## Please note that this web-app is designed to be deployed on the HEROKU Platform.

The URI of this API is [https://openflaskapi.heroku.com](https://openflaskapi.heroku.com).

# How to use the APIs ?

You can use any tool for calling various http methods to get the response but I will suggest you to use [Postman](https://www.getpostman.com/).

## Complete URI of API is https://www.openflaskapi.herokuapp.com/api/v1/

## Structure of our URI :
https://www.openflaskapi.herokuapp.com/api/v1/users
This URI is used via GET method to get a JSON list of users from the database.

https://www.openflaskapi.herokuapp.com/api/v1/users
This URI is used via POST method to send a JSON containing all the information needed for adding a new user in the database. The needed data and format is : 
{
    'name': 'User Name',
    'email': 'user@email.com',
    'password': 'password',
    'tag': 'This Field is not required'
}

https://www.openflaskapi.herokuapp.com/api/v1/users/[email]
The email in the URI is replaced with the email of the user. This URI is used via GET method to get a JSON containing user's info from the database.

https://www.openflaskapi.herokuapp.com/api/v1/users/[email]
The email in the URI is replaced with the email of the user. This URI is used via PUT method to change the tag of a user. We need to send a JSON with the tag and its value.
{
    'tag': 'This is my tag !'
}