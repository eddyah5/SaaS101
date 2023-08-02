# SaaS101
Django-stripe-subscriptions - In this project, we experiment with building a simple SaaS app with Stripe payment gateway API to client handle subscriptions and payments nicely.
The project is comprised of 7 parts accordingly. More on this later.
====================================================================================================================
**TO USE THIS PROJECT FOLLOW THE FOLLOWING STEPS:
**
**a)**Fork/Clone this repo

**b)**Create and activate a virtual environment:
$ py -3 -m env .env
$ .env\scripts\activate

**c)**Install the requirements:
(env)$ pip install -r requirements.txt

**d)**Apply the migrations:
(env)$ python manage.py migrate

**e)**Add your Stripe test secret key, test publishable key, endpoint secret and price API ID to the settings.py file:
STRIPE_PUBLISHABLE_KEY = '<your test publishable key here>'
STRIPE_SECRET_KEY = '<your test secret key here>'
STRIPE_PRICE_ID = '<your price api id here>'
STRIPE_ENDPOINT_SECRET = '<your endpoint secret here>'

**f)**Run the server:
(env)$ python manage.py runserver

=====================================================================================================================
**Project parts:**
Since this project code base was grabbed from this post from https://testdriven.io/blog/django-stripe-subscriptions/ , I feel like it is worth mentioning, and also I needed to put in some hints on how to achieve each step if you decided to code along from scratch instead of downloading and using the repo. If you have decided to do it from scratch, use the hints below with the above post to code along. This offers the advantage of working COMMAND-LINE-INTERFACE commands:

**PART 1)
PROJECT SETUP ENVIRONMENT(WINDOWS ONLY ON YOUR VSCODE OR ANY OTHER CODE EDITOR)**
1) Inside your Code editor, open the terminal, then first **cd** into Desktop or any other location
2) **mkdir** django-stripe-subscriptions (create a folder called django-stripe-subscriptions)
3) **cd django-stripe-subscriptions** (into the folder django-stripe-subscriptions)
4) **py -3 -m venv .env** (creates an environmental variable env)
5) **.env\scripts\activate** (activates an environmental variable env)
6) **python -m pip install --upgrade pip** (upgrades pip)
7) **python -m pip install Django** (Install Django)
8) **django-admin startproject djangostripe .** (creates a new Django project, don't forget the . )
9) **python manage.py startapp subscriptions** (creates a new Django app)
10) Add the following lines under App in djangostripe/settings.py ['subscriptions.apps.SubscriptionsConfig',]
11) Create new view called "Home" under subscriptions/views.py and add your and point your home.html file (Check the post for code)
12) Assign a URL to the view created under subscriptions/urls.py (If there is no urls.py file under your app directory create it) (Check the post for code)
13) Make a URL for our app djangostripe/urls.py (Check the post for code)
14) Under the subscription app, create a new folder and call it "templates"
15) Inside the templates folder, create a new file names home.html and populate it(Check the post for code)
16) Update the settings.py and put "templates" under "Templates" and beside 'DISR'
17) **python manage.py migrate** migrates everything changes to the database
18) **python manage.py makemigrations** checks for more migration to do
19) **python manage.py runserver** (Starts your Django app, then you can visit http://127.0.0.1:8000/ to see the app running)

    Visit this link for the rest of it https://docs.google.com/document/d/1u0CWMwnbbOY_2PQVPqsxPr7YQ26KPA1uGXYV_VEip_s/edit?usp=sharing 
