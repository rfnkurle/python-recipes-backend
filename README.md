# React-Django Recipe App Backend

<img width="1065" alt="Screen Shot 2024-07-22 at 1 56 32 PM" src="https://github.com/user-attachments/assets/83364cda-6c10-44d4-b25f-7f8f7b903b1e">



## Architecture Overview

### Backend (Django)
API Endpoints: The Django REST Framework creates API endpoints that the React frontend communicates with. These endpoints handle CRUD operations and data retrieval. For the purposes of this app, routes have been created that are able to post a new recipe, get all recipes, get a single recipe by id, or delete by id.
API Logic: Django views contain the logic to process requests, interact with models, and return responses.
Data Handling: Django models define the structure of the database, and serializers convert data between JSON and Django models. For the purposes of this application the Recipe model establishes the structure of the Recipe table in the SQL database.
Communication Between Frontend and Backend
HTTP Requests: In this application, React makes HTTP requests to Django endpoints to get, create, delete data. As mentioned before, requests are handled by the axios package through the RecipeService.js file. The Django corsheaders package was applied to allow easy access of API to the frontend.

## Deployment and Hosting
### Frontend Deployment: The finished React app is built into a static “dist” file using the Vite framework build tool. This “dist” file can be deployed purely as a frontend through static hosting service. For this project, an AWS s3 bucket deployment demonstrates this purely frontend dynamic. 

###Backend Deployment: Django is deployed to a server or cloud service, with the backend handling API requests from the React frontend. In this application an AWS ec2 instance was created and configured to serve the Django backend. 

###Integration and Deployment: CORS was used to ensure proper integration between the frontend and backend by configuring environment variables, API endpoints, and CORS settings. For ease of full application deployment, the Heroku service was utilized with python and node build packages.
