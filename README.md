# Employee management system

EMS (Employee managament system) is a POC which handles employee and their attendance with peer-to-peer performance reviews as well.

## Installation

create a vitual environment with python version >= 3.11

### Install Dependencies
Go to the root folder and execute the following command to install all the virtual dependencies
```bash
pip install -r requirements.txt
```
create a `.env` file on the same level of settings.py file in the project directory

## API documentation
You can find the swagger documentation at the [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/). 
### Model
#### User
We store user name, email, mobile and requires password for the account creation. The url to create user would be [http://127.0.0.1:8000/users/](http://127.0.0.1:8000/users/)
#### Department
We ask for name of the department, so we can segregate the employees based on the department
#### Employee
We will create an employee with basic details such as date of joining, address and which department they belongs to, we will get remaining information from the user
#### Attendance
Employee can register their attendance for the day, by passing status (present, absent, late)
#### Performance
Employee can give the rating for their peer employees
### Authentication
User needs to logged in to perform employee related action. User can get an access token and a refresh token from the endpoint [http://127.0.0.1:8000/api/token/](http://127.0.0.1:8000/api/token/). This access token should be passed as Authorization header for endpoints which requires authentication

### Fake data population
We can populate fake data into the database
Run this command to create fake data
```bash
python manage.py seed_data
```

### Build
Run these commands from the path where `manage.py` file resides
```bash
cd employeesystem
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

