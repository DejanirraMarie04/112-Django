# How to create a Django project

## Step 1 
Create a folder for the project

## Step 2
Open folder in terminal

## Step 3
Create virtual enviornment-

    python/py -m venv venv 

## Step 4
Activate virtual enviornment-

    venv\Scripts\activate

## Step 5
Install Django dependency-

    pip install django

## Step 6
Run the startproject command in terminal to create project settings-

    django-admin startproject NAME_OF_PROJECT .
    Note: replace NAME_OF_PROJECT with config or any other name

    django-admin startproject config .

    Expected Output: two folders and a single file called **manage.py**

## Step 7
Running the Django project

    python/py manage.py runserver

## Step 8
Creating django apps

    Both OS: python manage.py startapp NAME_OF_THE_APP

## Models in Django

When we finish a model structure we need to run these commands in order:

    1. python manage.py makemigrations
    2. python manage.py migrate