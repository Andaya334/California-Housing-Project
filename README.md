# California-Housing-Project

![image](https://user-images.githubusercontent.com/117672086/232669250-b9fcb017-f5d8-42f5-933a-9d70fe89b913.png)
![image](https://user-images.githubusercontent.com/117672086/232669471-91f73bbd-7a61-4887-bc0a-daf0e4ff0f46.png)
![image](https://user-images.githubusercontent.com/117672086/232669598-6f04bfe4-d567-4bd5-8041-a69d10934a89.png)

The purpose of this project is to find the median house value in relation to the distance of certain metropolitan such as San Diego, San Francisco, San Jose and Los Angeles.

This project will also demonstrate median household income, median age of the house, and proximity of the house to a metropolitan area.

First, you will need to set up a SQLite database containing the necessary data. Once the database is set up, you can run the provided Python code to create a Flask app with API endpoints for querying the database.

To access the API endpoints, you can use a tool like Postman or simply navigate to the appropriate URL in a web browser. The available endpoints include getting all housing data, filtering by distance to various metropolitan areas, filtering by median house value, median income, median age, total number of rooms, total number of bedrooms, and population.

Additionally, there is an index.html file and a style.css file included for displaying the data in a more user-friendly format.

Please note that this project is meant for educational purposes only and the data used may not be up-to-date or accurate for real-world use cases.


This is a simple Flask web application that provides a RESTful API for accessing data about California housing. The data is stored in an SQLite database, and the API endpoints allow users to filter and retrieve data based on various criteria.

Installation
To install and run the application, follow these steps:

Clone this repository to your local machine.
Create a virtual environment for the project: python3 -m venv env
Activate the virtual environment: source env/bin/activate
Install the required dependencies: pip install -r requirements.txt
Initialize the SQLite database: python init_db.py
Start the Flask application: python app.py
Open a web browser and navigate to http://localhost:5000/
API Endpoints
The following API endpoints are available:

/api/housing: Returns all data from the Housing table in the database.

/api/housing/distance_to_la/<float:distance>: Returns all data from the Housing table where the distance to Los Angeles is less than or equal to the specified distance (in miles).

/api/housing/distance_to_sf/<float:distance>: Returns all data from the Housing table where the distance to San Francisco is less than or equal to the specified distance (in miles).

/api/housing/distance_to_sd/<float:distance>: Returns all data from the Housing table where the distance to San Diego is less than or equal to the specified distance (in miles).

/api/housing/distance_to_sj/<float:distance>: Returns all data from the Housing table where the distance to San Jose is less than or equal to the specified distance (in miles).

/api/housing/distance_to_coast/<float:distance>: Returns all data from the Housing table where the distance to the coast is less than or equal to the specified distance (in miles).

/api/housing/median_house_value/<int:value>: Returns all data from the Housing table where the median house value is equal to the specified value.

/api/housing/median_income/<int:value>: Returns all data from the Housing table where the median income is equal to the specified value.

/api/housing/median_age/<int:value>: Returns all data from the Housing table where the median age is equal to the specified value.

/api/housing/tot_rooms/<int:value>: Returns all data from the Housing table where the total number of rooms is equal to the specified value.

/api/housing/tot_bedrooms/<int:value>: Returns all data from the Housing table where the total number of bedrooms is equal to the specified value.

/api/housing/population/<int:value>: Returns all data from the Housing table where the population is equal to the specified value.

Technologies Used
This project uses the following technologies:

Python
Flask
SQLite
SQLAlchemy
Contributing
Contributions to this project are welcome. If you find a bug or would like to suggest an improvement, please open an issue on the project's GitHub repository. If you would like to contribute code, please fork the repository and submit a pull request.
