# Introduction

This is a basic semi-functioning Django web app for a restaurant called Little Lemon, created as the capstone project for the Meta Back-End Developer Professional Certificate on Coursera.

## Usage

- Use `git clone` to get the project, or download it as a ZIP file and extract it
- Run `pipenv install` in a command line in the project directory
- Change the `DATABASES` variable on line 80 in `LittleLemon/settings.py` to match your database settings. By default, this uses a MySQL database with the following configuration:

```
DATABASES  =  {
	'default':  {
		'ENGINE':  'django.db.backends.mysql',
		'NAME':  'little_lemon',
		'HOST':  '127.0.0.1',
		'PORT':  '3306',
		'USER':  'root',
		'PASSWORD':  '',
		
		'OPTIONS':  {
		'init_command':  "SET sql_mode='STRICT_TRANS_TABLES'"
		}
	}
}
```
- Run `py manage.py runserver` in the project directory to run the server, which can be viewed at `https://127.0.0.1:8000` by default.
