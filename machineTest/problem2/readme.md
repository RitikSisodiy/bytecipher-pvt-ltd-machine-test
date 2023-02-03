##
# **Django Rest Framework for Product and User Management**

## **Introduction**

This is a Django Rest based RESTful API for product and user management using mongoDB. It includes the following functionalities:

1. User signup
2. User login
3. Add product
4. Delete Product
5. Search product by keyword

## **Prerequisites**

- Python 3.10.5
- Django 4.1.6
- Django Rest Framework (DRF)
- Django Rest Framework Simple JWT

## **Getting Started**
1. Change into the project directory

$ cd restApi

1. Install the required packages

$ pip install -r requirements.txt

1. Run the migrations

$ python manage.py migrate

1. Start the development server

$ python manage.py runserver

## **Endpoints**

### **User Signup**

- Endpoint: /api/signup/
- Method: POST
- Params: name, email, password

### **User Login**
To log in and get a JWT token, send a POST request to /api/login/ 
- Endpoint: /api/login/
- Method: POST
- Params: email, password

### **Add Product**

- Endpoint: /products/
- Method: POST
- Params: name, price, color, images (Multiple Image upload)

### **Search Product**

- Endpoint: /products/search?q=\<keyword\>
- Method: GET
- Params: q (keyword to search for products)

### **Update Product**
- Endpoint: /products/<id>
- Method: PUT
- Params: name, price, color, images (Multiple Image upload)
it is a partial update

### **Delete Product**
- Endpoint: /products/<id>
- Method: DELETE

## **Admin Interface**
To access the Django Admin interface, navigate to /admin/ in your browser. You will need to log in with a superuser account. From the admin interface
to create admin credentials run

-  python manage.py createsuperuser 

## **JWT Token**
The JWT token obtained from the login endpoint is required for accessing the protected endpoints (addProduct, searchProduct) as Bearer Token.

## **Conclusion**
This API provides a basic implementation of product and user using Django Rest Framework. we can add more functionalities as per the requirement.

Note : make sure to install mongodb compass and add mongodb database name in restApi/settings.py 
DATABASES = {
     'default': {
         'ENGINE': 'djongo',
         'NAME': 'restapiDb', #replace db name here
     }
 }