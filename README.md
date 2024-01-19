
# Inventory-Management-Application
# Django-Inventory-Management-System
Welcome to the Readme for your Inventory Management Application!

This document provides a comprehensive overview of the features, functionalities, and technical details of the application.

# Overview:
    This Python (Django)-based application offers a user-friendly and secure platform for managing inventory, sales, purchases, and bills. It caters to two distinct user roles:
    Administrators: Can manage goods information, including adding, editing, and deleting products, setting reorder levels, and generating reports.
Staff Members: Can handle sales, purchases, generate bills and invoices, and print physical sales and purchase copies.
## Description
This system is built with Python (Django), JavaScript, Bootstrap, HTML, and CSS. The system offers a user-friendly front-end for general users and a secure back-end exclusively accessible to administrators. The back-end seamlessly retrieves and displays vital data from the database.

The system caters to two distinct user roles: administrators and staff members. Administrators have the privilege to log in and manage goods information, while staff members handle sales, purchases, bills, and invoice creation.

Powered sqlite3 database, our system not only stores all essential information but also boasts a user-friendly interface for effortless interaction. Users input data through this interface, and the system processes it, generating valuable insights based on user input. Additionally, the system diligently archives processed data in the database for future reference.

## Installation

Before you can run the application, ensure you have the following prerequisites and dependencies:

- Docker

To install the application, follow these steps:

1. Clone the repository:

   ```bash
   cd sales-and-inventory-management
   
2. Run the setup.sh file (Builds the Docker container):

    ```bash
    bash bin/setup.sh

# Key Features:-
    User-friendly interface: Built with Bootstrap, HTML, and CSS for a smooth and intuitive user experience.
    Secure back-end: Utilizes Django authentication and authorization features for secure access control.
    SQLite3 database: Efficiently stores product information, sales/purchase data, and generated reports.
    Data insights: Generates valuable reports based on user input, providing insights into inventory trends, sales performance, and more.
    QR code generation: Generate product-specific QR codes for easy identification and external use.
    Email confirmation: Automatically sends confirmation emails upon successful user registration.
    Printing capabilities: Print both sales and purchase bills for physical record keeping.
    Excel export: Export sales and transaction data to Excel spreadsheets for further analysis.
# Technology Stack:
    Front-end: Django templates, JavaScript, Bootstrap, HTML, and CSS
# Back-end: Python (Django)

# Database: SQLite3

# Prerequisites:

    Python (Python 3.10.9)
	 
    Django (Django==4.2.6)
	 
   # Additional libraries: See the requirements.txt file for full list
# Running the Application:

    Clone the repository.
	 
    Create a virtual environment and activate it (python3 -m venv venv && source venv/bin/activate).
	 
    Install required dependencies (pip install -r requirements.txt).
	 
    Run database migrations (python manage.py makemigrations && python manage.py migrate).
	 
    Create a superuser (python manage.py createsuperuser).
	 
    Start the development server (python manage.py runserver).


# Additional Notes:
This Readme is a starting point. You can customize it further to include specific details about your project, deployment instructions, and any additional features.
Consider adding screenshots or GIFs showcasing the application's user interface.
Provide contact information for any questions or support requests.





    

## Screenshots

![Screenshot (47)](https://user-images.githubusercontent.com/51537638/218985189-8ca2046e-02a8-4c8b-8243-0027fbfd728c.png)
![Screenshot (48)](https://user-images.githubusercontent.com/51537638/218985199-dfd74679-006a-4fe7-bd9a-fc1f244b8a5f.png)
![Screenshot (49)](https://user-images.githubusercontent.com/51537638/218985218-2c00c2f4-bf8a-4ab0-88cf-b374bcf1cdb2.png)
![Screenshot (50)](https://user-images.githubusercontent.com/51537638/218985221-3af9c58f-1015-4e3d-99b6-a93f1586d5aa.png)
![Screenshot (51)](https://user-images.githubusercontent.com/51537638/218985224-544832e1-938e-4b18-aec8-2efe8f55415e.png)
![Screenshot (52)](https://user-images.githubusercontent.com/51537638/218985242-e52fe221-3fb7-4393-b205-8d930f673037.png)
![Screenshot (53)](https://user-images.githubusercontent.com/51537638/218985248-2a2864a1-7b07-40b0-ab28-fdb3d40b0742.png)
![Screenshot (54)](https://user-images.githubusercontent.com/51537638/218985262-ce21da7e-dc14-47f2-b31d-94de04b49bb7.png)
![Screenshot (37)](https://user-images.githubusercontent.com/51537638/218985266-2bdf70a6-8f41-4e07-bafb-3cb97562ef85.png)
![Screenshot (38)](https://user-images.githubusercontent.com/51537638/218985272-1773c6af-db04-4221-9149-8b56f50638df.png)
![Screenshot (39)](https://user-images.githubusercontent.com/51537638/218985280-7a6a8116-6cdb-4281-9aae-a036a0c42157.png)
![Screenshot (40)](https://user-images.githubusercontent.com/51537638/218985289-d50e317c-a4c8-4546-88c9-b71a03e0cb37.png)
![Screenshot (41)](https://user-images.githubusercontent.com/51537638/218985303-a61516c4-b28d-4807-909e-761d820dc60c.png)
![Screenshot (42)](https://user-images.githubusercontent.com/51537638/218985321-fe56bfcf-2498-4ed0-bc7c-1611b7e9b2cd.png)
![Screenshot (43)](https://user-images.githubusercontent.com/51537638/218985330-ba9eea5c-ee39-4f5c-8cd4-5e9fadeb4e24.png)
![Screenshot (44)](https://user-images.githubusercontent.com/51537638/218985343-5dcb504a-0096-4138-9572-0f293ef25d98.png)
![Screenshot (45)](https://user-images.githubusercontent.com/51537638/218985351-356f0f61-f3e5-480b-ab88-9818cbfb91c1.png)
![Screenshot (46)](https://user-images.githubusercontent.com/51537638/218985357-fc0e7f3b-5729-4a32-95b3-c016aa48c219.png)
