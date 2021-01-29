
## ManageProduct
This project was generated with Python 3.8.5 and Django Framework 3.1.5

####### To run the application

- Crate a virtual environment (Windows)
virtual env -p manageProductsEnv
cd manageProductsEnv
Scripts/activate

- Install Django into your enviroment
pip install django

- Clone the project into your virtual enviroment 

- Install librarys REST
pip install djangorestframework
pip install django cors-headers

- Make the migrations of models
python manage.py makemigrations
python manage.py migrate

- Start the project
python manage.py runserver

######## Info about application
--Usually the app runs into http://127.0.0.1:8000/ (host)

# Admin page
- {host}/admin (Ex: http://127.0.0.1:8000/admin)
- User: Admin
- password: admin
-- Here you can add, edit and delete other admins or common users and give them permissions, also you can edit, add and delete products.
--- When an Administrator edit a product, all administrator receive the email (templates/email.html) 
--- When a common users add products to them wished list you can view this at "wished" field and most details about who user added at history of every product

# REST API
- {host}/products (Ex: http://127.0.0.1:8000/products)
-- Here you can consume the API (GET, POST, ETC)

## About Unit Test
-Install pytest
pip install pytest

-Read Json File
You can change the route of CrateNewProduct.json and add the absolute path into test_CreateProduct.py

-Run test
pytest product
--This test check the status of POST request

