# Avidity Supply

For my Milestone Project 4 with Code Institute, I designed a website called Avidity Supply, inspired by a business my cousin and I started when we were younger, focused on creating minimalist street apparel, particularly hats.

To bring this vision to life, I utilized several tools and technologies: Django, Python, HTML, CSS and JavaScript.

The result is a functional, elegant e-commerce platform that showcases our streetwear designs with simplicity and sophistication.

![Website on different screen sizes](media/amir_avidity_supply.png)

[Access the live site here.](https://avidity-supply-1597743384d8.herokuapp.com/)

## Deployment

The project was deployed to [Heroku](https://dashboard.heroku.com/) using the following steps:

### Create the Database
Sqlite3 was used in development but cannot be used for the deployed project. An ElephantSQL database was created following the steps bellow:
- Go to the ElephantSQL, create an account and log in and access your dashboard
- Click on the “Create New Instance” button
- Set up your plan
  - Give your plan a Name (this is commonly the name of the project)
  - Select the Tiny Turtle (Free) plan
  - You can leave the Tags field blank
- Select “Select Region”
- Select a data center near you
- Then click “Review”
- Check your details are correct and then click “Create instance”
- Return to the ElephantSQL dashboard and click on the database instance name for this project
- In the URL section, clicking the copy icon will copy the database URL to your clipboard
### Create a new Heroku app
- Go to Heroku's website, create an account, login and click to create a new app
- Give your app a name and select the region closest to you. When you’re done, click Create app to confirm (must be a unique name)
- Open the Settings tab
- Add the config var DATABASE_URL, and for the value, copy in your database url from ElephantSQL. It should look something like this. Do not add quotation marks around your database url string.

### Project preparation in Gitpod
- In the terminal, install dj_database_url and psycopg2, both of these are needed to connect to your external database.

```
 pip3 install dj_database_url==0.5.0 psycopg2
```

- Update your requirements.txt file with the newly installed packages

```
 pip freeze > requirements.txt
```

- In your settings.py file, import dj_database_url underneath the import for os

```
 import os
 import dj_database_url
```

- Scroll to the DATABASES section and update it to the following code, so that the original connection to sqlite3 is commented out and we connect to the new ElephantSQL database instead. Paste in your ElephantSQL database URL in the position indicated

```
# DATABASES = {
 #     'default': {
 #         'ENGINE': 'django.db.backends.sqlite3',
 #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 #     }
 # }
     
 DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
 }
```

DO NOT commit this file with your database string in the code, this is temporary so that we can connect to the new database and make migrations. We will remove it in a moment.

- In the terminal, run the showmigrations command to confirm you are connected to the external database

```  
python3 manage.py showmigrations
```

- Migrate your database models to your new database

``` 
 python3 manage.py migrate
```

- Load in the fixtures. Please note the order is very important here. We need to load categories first

```
 python3 manage.py loaddata categories
```

- Then products, as the products require a category to be set

```
python3 manage.py loaddata products:
```

- Create a superuser for your new database:

```  
python3 manage.py createsuperuser
```

- You should now be able to go to the browser tab on the left of the page in elephantSQL, click the table queries button and see the user you've just created by selecting the auth_user table.
- We can now add an if/else statement for the databases in settings.py, so we use the development database while in development (the code we commented out) - and the external database on the live site (note the change where the db URL was is now a variable we will use in Heroku):

```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
      'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
      }
    }
```

- Install gunicorn which will act as our webserver and freeze this to the requirements.txt file:

```
pip3 install gunicorn
pip3 freeze > requirements.txt
```

- Create a Procfile in the root directory. This tells Heroku to create a web dyno which runs gunicorn and serves our django app. Add the following to the file (making sure not to leave any blank lines underneath):

```
web: gunicorn seaside_sewing.wsgi:application
```

- Log into the Heroku CLI in the terminal and then run the following command to disable collectstatic. This command tells Heroku not to collect static files when we deploy:

``` 
heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name-here
```

- We will also need to add the Heroku app and localhost (which will allow gitpod to still work) to ALLOWED_HOSTS = [] in settings.py

```
ALLOWED_HOSTS = ['{heroku deployed site URL here}', 'localhost' ]
```

- Save, add, commit and push the changes to GitHub. You can then also initialize the Heroku git remote in the terminal and push to Heroku with:

```
heroku git:remote -a {app name here}
git push heroku master
```

- You should now be able to see the deployed site (without any static files as we haven't set these up yet).
- To enable automatic deploys on Heroku, go to the deploy tab and click the connect to GitHub button in the deployment method section. Search for the projects repository and then click connect. Click enable automatic deploys at the bottom of the page.

### Generate a SECRET_KEY & Updating Debug
- Django automatically sets a secret key when you create your project, however we shouldn't use this default key in our deployed version, as it leaves our site vulnerable. We can use a random key generator to create a new SECRET_KEY which we can then add to our Heroku config vars which will then keep the key protected.
- Create a new key and copy the value.
- In Heroku settings create a new config var with a key of SECRET_KEY. The value will be the secret key we just created. Click add.
- In settings.py we can now update the SECRET_KEY variable, asking it to get the secret key from the environment, or use an empty string in development:

```
SECRET_KEY = os.environ.get('SECRET_KEY', ' ')
```

- We can now adjust the DEBUG variable to only set DEBUG as true if in development:

```
DEBUG = 'DEVELOPMENT' in os.environ
```

- Save, add, commit and push these changes.

### Set up AWS hosting for static and media files
- Sign up or login to your aws amazon account on the top right by using the manage my account button and then navigate to S3 to create a new bucket.
- The bucket will be used to store our files, so it is a good idea to name this bucket the same as your project. Select the region closest to you. In the object ownership section we need to select ACLs enabled and then select bucket owner preferred. In the block public access section uncheck the block public access box. You will then need to tick the acknowledge button to make the bucket public. Click create bucket.
- Click the bucket you've just created and then select the properties tab at the top of the page. Find the static web hosting section and choose enable static web hosting, host a static website and enter index.html and error.html for the index and error documents (these won't actually be used.)
- Open the permissions tab and copy the ARN (amazon resource name). Navigate to the bucket policy section click edit and select policy generator. The policy type will be S3 bucket policy, we want to allow all principles by adding * to the input and the actions will be get object. Paste the ARN we copied from the last page into the ARN input and then click add statement. Click generate policy and copy the policy that displays in a new pop up. Paste this policy into the bucket policy editor and make the following changes: Add a /* at the end of the resource value. Click save.
- Next we need to edit the the cross-origin resource sharing (CORS). Paste in the following text:

```
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```

- Now we need to edit the access control list (ACL) section. Click edit and enable list for everyone(public access) and accept the warning box.

### Creating AWS groups, policies and users
- Click the services icon on the top right of the page and navigate to IAM - manage access to AWS services. On the left hand navigation menu click user groups and then click the create group button in the top right. This will create the group that our user will be placed in.
- Choose a name for your group - for example manage-seaside-sewing, and click the create policy button on the right. This will open a new page.
- Click on the JSON tab and then click the link for import managed policy on the top right of the page.
- Search for S3 and select the one called AmazonS3FullAccess, then click import.
- We need to make a change to the resources, we need to make resources an array and then change the value for resources. Instead of a * which allows all access, we want to paste in our ARN. followed by a comma, and then paste the ARN in again on the next line with /* at the end. This allows all actions on our bucket, and all the resources in it.
- Click the next: tags button and then the next:review 
- Give the policy a name and description. Click the create policy button.
- Now we need to attach the policy we just created. On the left hand navigation menu click user groups, select the group and go to the permissions tab. Click the add permissions button on the right and choose attach policies from the dropdown.
- Select the policy you just created and then click add permissions at the bottom.
- Now we'll create a user for the group by clicking on the user link in the left hand navigation menu, clicking the add users button on the top right and giving our user a username. Select programamtic access and then click the next: permissions button.
- Add the user to the group you just created and then click next:tags button, next:review button and then create user button.
- You will now need to download the CSV file as this contains the user access key and secret access key that we need to insert into the Heroku config vars. Make sure you download the CSV now as you won't be able to access it again.

### Connecting Django to our S3 bucket
- Install boto3 and django storages and freeze them to the requirements.txt file.

```
pip3 install boto3
pip3 install django-storages
pip3 freeze > requirements.txt
```

- Add storages to the installed apps in settings.py
- Add the following code in settings.py to use our bucket if we are using the deployed site:

```
if 'USE_AWS' in os.environ:
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=9460800',
    }
    
    AWS_STORAGE_BUCKET_NAME = 'enter your bucket name here'
    AWS_S3_REGION_NAME = 'enter the region you selected here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```

- We can now go to Heroku and add the following config vars:
  - **AWS_ACCESS_KEY_ID** - *The access key value from the amazon csv file downloaded in the last section*
  - **AWS_SECRET_ACCESS_KEY** - *The secret access key from the amazon csv file downloaded in the last section*
  - **USE_AWS** - *True*
- Remove the DISABLE_COLLECTSTATIC variable.
- Create a file called custom_storages.py in the root and import settings and S3Botot3Storage. Create a custom class for static files and one for media files. These will tell the app the location to store static and media files.
- Add the following to settings.py to let the app know where to store static and media files, and to override the static and media URLs in production.

```
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

- Save, add, commit and push these changes to make a deployment to heroku. In the build log you should be able to see that the static files were collected, and if we check our S3 bucket we can see the static folder which has all the static files in it.
- Navigate to S3 and open your bucket. We now want to create a new file to hold all the media files for our site. We can do this by clicking the create folder button on the top right and naming the folder media.

### Setting up Stripe
- We now need to add our Stripe keys to our config vars in Heroku to keep these out of our code and keep them private. Log into Stripe, click developers and then API keys.
- Create 2 new variables in Heroku's config vars - for the publishable key (STRIPE_PUBLIC_KEY) and the secret key (STRIPE_SECRET_KEY) and paste the values in from the Stripe page.
- Now we need to add the webhook endpoint for the deployed site. Navigate to the webhooks link in the left hand menu and click add endpoint button.
- Add the URL for our deployed sites webhook, give it a description and then click the add events button and select all events. Click Create endpoint.
- Now we can add the webhook signing secret to our Heroku config variables as STRIPE_WH_SECRET.
- In settings.py:

```
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
```


## Credits
### Code
  - Boutique Ado walk-through project from [Code Institute](https://codeinstitute.net/)
  - [Bootstrap Docs](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
  - [Django-Allauth Documentation](https://django-allauth.readthedocs.io/en/latest/installation.html)

### Content
- Landing (Hero) Image sourced from [Freepik](https://www.freepik.com/).
- Product images were created on [Printify](https://printify.com/).

### Acknowledgements
- Amy Richards, Cohort Facilitator: Thank you, for all your help to myslef and the others during our journey.
- June 2023 Cohort: An amazing group of like minded people, who are always there to support one another and I appreciate you all, thank you!