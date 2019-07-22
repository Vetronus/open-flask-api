# What is Open Flask API ?
`version 1.1`

Open flask api is a simple API based on ReST API Architecture and programmed in Python-3 using flask micro-framework. It is created for begginers to understand the basics of creating a ReST API in Python.It can also be used as a template to create your new APIs.

In this API, we store store data of various users. we can:
- sign-up a user by providing required data using POST.
- get a list of users with data.
- get a specific user's data using his unique email.
- update the tag of user using PUT and his specific email.

##### Please note that this web-app is designed to be deployed on the HEROKU Platform. The URL to the dyno of this API is http://openflaskapi.herokuapp.com.

# Language, Framework and Plugins used :
- ### Python 3.6.2
- ### Flask micro-framework
- ### Flask ReSTfull
- ### Peewee

# How to use the APIs ?

#### [Postman](https://www.getpostman.com/) :
`You can use any tool for calling various http methods to get the response but I will suggest you to use`
[Postman](https://www.getpostman.com/).
`Also, if you don't know how to use Postman to send various types of request than watch some tuts online.`

#### Complete URI of API is http://openflaskapi.herokuapp.com/api/v1/users

## Structure of our URI :
- ### `http://openflaskapi.herokuapp.com/api/v1/users` | GET
This URI is used via GET method to get a JSON list of users from the database. Paste this URI in Postman and you will get a list of Users in form of JSON.

- ### `http://openflaskapi.herokuapp.com/api/v1/users` | POST
This URI is used via POST method to send a JSON containing all the information needed for adding a new user in the database. The needed data and format is :
```
{
    'name': 'User's Name',
    'email': 'user@email.com',
    'password': 'password',
    'tag': 'This Field is not required'
}
```
Paste the URI and JSON in the Postman and POST it, The user will be saved in the database. Please note that two users with same email are not compatible, and an error will be thrown.

- ### `http://openflaskapi.herokuapp.com/api/v1/users/[email]` | GET
The email in the URI is replaced with the email of the user. This URI is used via GET method to get a JSON containing user's info from the database.

- ### `http://openflaskapi.herokuapp.com/api/v1/users/[email]` | PUT
The email in the URI is replaced with the email of the user. This URI is used via PUT method to change the tag of a user. We need to send a JSON with the tag and its value.
```
{
    'tag': 'This is my updated tag !'
}
```

- ### `http://openflaskapi.herokuapp.com/api/v1/users/[email]` | DELETE
The email in the URI is replaced with the email of the user. This URI is used via DELETE method to delete user's info from the database.

## License and Usage :

This project is completely open-source and free-to-use. But you will need to mention about its great, super awesome author XD (JK, use it anywhere you want, I really don't care.) PS, Happy Coding!
