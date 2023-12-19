# flask_e2e_project

## Web Service
My web service in this repository is a simple Flask app that displays the overall percentage of hospitals reporting one or more elements for the previous week. This file updated weekly on Mondays. The reported list includes hospitals that are registered with the CMS and does not include pschiatric, rehabilitation, IHS facilities, or U.S Dept. of Veterans.

## Technologies
1. Github: file version control
2. Flask (Python, frontend, & backend): Micro web framework to build web applications.  
3. MySQL (database via Azure): open-source relational database management system. THe MySQL Flexibile Server on Azure contains the database of the repo that can be deployed through Azure
4. SQLAlchemy(ORM): Object Relational Mapping for python to create a connection with MySQL
5. .env file: configuration used to store environment values that are sensitive information or configuration settings for an application. In my repo, this was used to contain information for the google credentials and Google Oauth configuration
6. Tailwind (frontend styling): framework that allows us to create designs (using colors, fonts, shadows, adding google logo image)
7. Authorization (Google OAuth): allows us to grant access to resources based on authentication provided by Google
8. API Service (Flask Backend): Backend service that allows communication between different services. 
9. Logger: The file that records events, messages, and errors when the program is running. It is extremely important for debugging and understanding the behavior. This file allowed me to realize that there wasn't a connection between my .env file and Azure, so I had difficulties deploying it earlier.
10. Docker (containerization): PLatform for developing and running an application in containers
11. Azure Deployment: Azure Deployment is deploying an application to Azure so that it can run my program

## Running Web Service 
#### Deploy Locally
1. Download the file
2. Change directory to the folder using ```cd flask_e2e_project/app```
3. In the terminal, use ```python app.py``` to run it locally
### Deploy with Docker
4. Build docker image ```docker build -t <name>```
5. Use ```docker ps``` to see docker list
6. Run docker using ```docker run -p 8080:5000 <name>```
- [Running Docker](https://github.com/hal-yu/flask_e2e_project/blob/main/docs/docker_build_run.png)
### Deploy with Cloud/Azure
7. Download Azure CLI using ```curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash```. Use the link to login and authenticate 
8. Use ```az webapp up --name <NAME> --runtime PYTHON:3.9 --sku B1``` to create a web app
9. Click on the link it gives you once deployed and it should take you to your web page.
- [Azure Connection](e.g: [docker](https://github.com/hal-yu/flask_e2e_project/blob/main/docs/Azure_connection.png)

## ENV File Template
MySQL Connection:
```
DB_HOST = <azure-host-link>
DB_DATABASE = <database-name>
DB_USERNAME = <username>
DB_PASSWORD = <password>
```
Google OAuth
```
GOOGLE_CLIENT_ID = <client-id>
GOOGLE_CLIENT_SECRET = <client-secret>
```
 
