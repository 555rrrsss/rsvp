## Environment & Application setup

Step 1: Download & install Python 3 -

The easiest way to setup a Python Environment on Windows is to download Anaconda - https://www.anaconda.com/download/

If on macOS, you can use `brew`

To setup homebrew, open the terminal and run the command

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`

Then install Python by running the following command

`$ brew install python`

Step 2: Install Pipenv

To setup & use isolated Virtual Environments, install pipenv

`$ pip install pipenv`

Step 3: Open the terminal & cd into project directory -

`$ cd /path/to/project`

Step 4: Activate/Create Virtual Environment

`$ pipenv shell`

Step 5: Run the following command to install all the dependencies -

`$ pipenv install`

Alternatively, you can run -

`$ pip install -r requirements.txt`

Step 6: Done!

# Run Locally:

Step 1: Open the terminal & cd into project directory -

`$ cd /path/to/project`

Step 2: Run the following command to run the application -

`$ python manage.py runserver`

Step 3: Copy the URL that will display in the terminal into your browser

Default URL - http://127.0.0.1:8000/

Step 4: Done!

Note: You may need to refresh your browser when front-end changes are made, back-end changes don't require re-running the application.

---

# Deployment Notes

#### NOTE: App uses WhiteNoise & does not require "collectstatic" Command or "DEBUG" to be set to "FALSE" in Settings

#### Set "DEBUG" to "FALSE" only for Production

#### What is WhiteNoise? -

[WhiteNoise](http://whitenoise.evans.io/en/stable/) allows your web app to serve its own static files, making it a self-contained unit that can be deployed anywhere without relying on nginx, Amazon S3 or any other external service. (Especially useful on Heroku, OpenShift and other PaaS providers.)
