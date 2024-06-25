# Project Chiru

## Description
Project Chiru will create a user interface (UI) and test its functionalities using Selenium, Robot Framework, and data-driven approaches. It will handle data through Pandas and file interactions, potentially connecting to a server and database (SQL) for backend operations. This comprehensive plan ensures a well-tested UI with seamless data management.

## Purpose/Goals
To master the skills of end-to-end programing of project from creation,integration,testing,storing,fetching .


## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Directory Structure](#directory-structure)
4. [Technologies Used](#technologies-used)


## Installation
1. Clone the repository:
   
   git clone https://github.com/chiruteja135/project-chiru.git
   cd project-chiru
  Create and activate a virtual environment:
  
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  
  Install the required packages:
  pip install -r requirements.txt

## Directory Structure

project-chiru/
│
├── Webpages/
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── show_users.html
│   └── static/
│       └── css/
│           └── styles.css
│
├── tests/
│   ├── robot/
│   │   ├── test.robot
│   │   ├── csv_reader.py
│   │   ├── students.csv
│   │   └── database.db
│   └── setup_database.py
│
├── setup.sql
├── requirements.txt
└── README.md


**Technologies Used**

  Python: Programming language used for server-side logic and scripts.
  Flask: Web framework used to create the web server and handle routes.
  SQLite: Database engine used to store user data.
  Robot Framework: Testing framework used for automated testing.
  SeleniumLibrary: Library used within Robot Framework for browser automation.
  DatabaseLibrary: Library used within Robot Framework for database interactions.
  HTML/CSS: Frontend technologies used for web page structure and styling.
