# Bynry Case Study

This is a my Django-based Service Request Management System for Gas Utility Company, that allows users to submit service requests, track their status, access customer support and enables administrators to manage these requests efficiently.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Setup Instructions](#setup-instructions)
3. [Installation of Dependencies](#installation-of-dependencies)
4. [Running the Project](#running-the-project)
5. [Screenshots and Features](#screenshots-and-features)

## Prerequisites

Make sure you have the following installed on your machine:

- Python (3.10 or above)

- Django (5.1.2)
  
## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/DarshanBanait/Bynry.git
   cd Bynry
2. **Create a Virtual Environment - Recommended
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate  # For Windows

##Installation of Dependencies

1. Install dependencies using pip
   ```bash
       pip install -r requirements.txt
   
##Running the Project

1. Apply Migrations
   ```bash
     python manage.py makemigrations
     python manage.py migrate

2. Create a Superuser (Admin)
   ```bash
     python manage.py createsuperuser

3. Run the development server
   ```bash
     python manage.py runserver

## Sign Up
![Image 1](images/image1.png)


## Login - Customer Account
![Image 2](images/image2.png)


![Image 3](images/image3.png)


## User Dashboard
![Image 4](images/image4.png)


## User Dashboard - Submitting New Request 
![Image 5](images/image5.png)


## Submitting a request
![Image 6](images/image6.png)


![Image 7](images/image7.png)


## User Dashboard - Tracking Request
![Image 8](images/image8.png)


## User Dashboard - Customer Support
![Image 9](images/image9.png)


## Login - Admin
![Image 10](images/image10.png)


## Admin Dashboard
![Image 11](images/image11.png)


## Admin Dashboard - Managing Requests
![Image 12](images/image12.png)


## Admin Dashboard - Assigning Requests to Employees
![Image 13](images/image13.png)


## Admin Dashboard - Updating Request Status
![Image 14](images/image14.png)


![Image 15](images/image15.png)


![Image 16](images/image16.png)

