# SaaS101
Django-stripe-subscriptions - In this project, we experiment with building a simple SaaS app with Stripe payment gateway API to client handle subscriptions and payments nicely.
The project is comprised of 7 parts accordingly. The code structure:
PART 1)PROJECT SETUP ENVIRONMENT, 
PART 2)STRIPE INTEGRATION 
PART 3)DATABASE MODEL 
PART 4)GET PUBLISHABLE KEY 
PART 5)CREATE CHECKOUT SESSION 
PART 6)USER REDIRECT 
PART 7)CREATE AND TEST STRIPE WEBHOOKS AND ENDPOINTS
More on this below
======================================================================================================================================
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
=======================================================================================================================================
**Project parts:**
Since this project code base was grabbed from this post from https://testdriven.io/blog/django-stripe-subscriptions/ , I feel like it is worth mentioning, and also I needed to put in some hints on how to achieve each step if you decided to code along from scratch instead of downloading and using the repo.
If you have decided to do it from scratch, use the hints below with the above post to code along. This offers the advantage of working COMMAND-LINE-INTERFACE commands:
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

**PART 2
STRIPE INTIGRATION**
20) To add Stripe payment gateway do in your terminal"**pip install stripe"**
21) Visit stripe.com and login to the dashboard. But if you don't have stripe account, just sign up then login
22) Inside Stripe dashboard, set up your account payment system step by step as Stripe will instruct you
23) Once completed, now we need a stripe API keys for integration so to the top-right corner and click on "Developers"
24) Still to the top-right corner, beside Developers, click on "Test mode" to toggle the API we need to test mode only
24) Still on the same page, check the right center of the window screen you will see "For developers", under there you can see our much-needed API keys which are 2, one is the Publishable key and the other is the Secret key. Copy both and keep them safe and secret
25) Under djangostripe/settings.py file paste the API keys at the bottom of the file using the following format:
STRIPE_PUBLISHABLE_KEY = '<enter your stripe publishable key>'
STRIPE_SECRET_KEY = '<enter your stripe secret key>'
26) Go back to the stripe dashboard and create a product by clicking on the **Products menu** on the top, then click the blue button that says "**Add product**"
27) Put your **product name, description, image/logo(optional), price, and product category**. Dont forget to select either recurring or one-time payment just below
28) Still on the same page, click on the "**Additional option**" to expand more. Then look for "**Feature list**" and click on it to add a line-by-line feature lists that will be displayed on the pricing table. You can also change the pricing model under the pricing information
29) Click add, and repeat steps 26 - 28 to add more products if you want
30) Next, grab the API ID of the price, and Save the ID for all the plans in the settings.py file like so:
# djangostripe/settings.py
STRIPE_PRICE_ID = 'price_1NY5nMKRuIYIFY0C742qZ0WG'
31) Under # subscriptions/views.py import login_required
32) **pip install django-allauth** (For addressing user authentication), then under # djangostripe/settings.py, add the following under INSTALLED_APPS (Check the post for code)
33) Add some code to django-allauth config to djangostripe/settings.py (Check the post for code)
34) Register the allauth URLs (Check the post for code)
35) Apply migrations **python manage.py migrate**
36) **python manage.py runserver** and sign up with username, email and password
37) Go back to your terminal and follow the link to confirm your email and login at the same time, you will see a blue button

**PART 3
DATABASE MODEL**
38) Create our model inside subscriptions/models.py (Check the post for code)
39) Register it with the admin in subscriptions/admin.py (Check the post for code)
40) python manage.py makemigrations
41) python manage.py migrate

**PART 4
GET PUBLISHABLE KEY**
42) mkdir static (Makes a folder called static)
43) cd static (To enter the folder static)
44) code main.js (Makes a new JavaScript file called main.js)(Check the post for code)
45) Perform a sanity check on the JS file (Check the post for code)
46) Update the settings.py file so Django knows where to find static files (Check the post for code)
47) Add the static template tag along with the new script tag inside the HTML template (Check the post for code)
48) Run the development server again. Navigate to http://localhost:8000/, and open up the JavaScript console. You should see the sanity check inside your console/terminal.
49) Next, add a new view to subscriptions/views.py to handle the AJAX request (Check the post for code)
50) Add a new URL as well to your subscriptions/urls.py as well (Check the post for the code)
51) Next, use the Fetch API to make an AJAX request to the new /config/ endpoint in the static/main.js file (Check the post for code)

**PART 5
CREATE CHECKOUT SESSION**
52) First, add the new view and update the subscriptions/views.py (Check the post for code)
53) Register the checkout session URL under subscriptions/urls.py (Check the post for code)
54) python manage.py makemigrations
55) python manage.py migrate
56) python manage.py runserver 
57) Click on the blue subscribe button and you will be redirected to the stripe subscription page for payments

**PART 6
USER REDIRECT**
58) Let's create success and cancel views under subscriptions/views.py
59) Create the success.html and cancel.html templates as well under templates (Check the post for code)
60) Register the new Views under subscriptions/urls.py (Check the post for code)
61) Use 4242 4242 4242 4242 for the card number to test, while expiration date = 20/28 or any future date, CVC=any 3 digits, then pay and your will be redirected to success page. If you did not login before it will ask you to Login before you can see it though

**PART 7
CREATE AND TEST STRIPE WEBHOOKS AND ENDPOINTS**
62) Create a new view called stripe_webhook which will create a new StripeCustomer every time someone subscribes to our service
1)Login to your stripe dashboard
2)Go to Developers ---->Webhooks
3)Click on "Add endpoint" and put https://github.com/stripe/stripe-cli for the endpoint URL with a description if you like
4)Select events to listen. Select all events.
5)Click on add endpoints and wait for it to add successfully
6)Copy the STRIPE_ENDPOINT_SECRET and past it under settings.py under your project folder
7)Go back to your local host and run the app, repeat step 61, and once you are done refresh your stripe webhook page to see subscription the event listed OR go to under payments to see the transactions
