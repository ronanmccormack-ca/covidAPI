# COVID API

## Introduction

This COVID API provides up-to-date information about COVID-19 cases by country. It's built using Flask and connects to a PostgreSQL database to retrieve data.

## Features

- Retrieve COVID-19 case data for a specific country.
- Get a list of available countries with COVID-19 data.

## API Availability

The API is available at the following link: [COVID API](https://covidapi-zm9v.onrender.com)

You can access the endpoints detailed in the API Endpoints section using this URL.


### Libraries

- Python 3
- Flask
- psycopg2
- dotenv

## API Endpoints

### 1. Get COVID-19 Data by Country

- **URL:** `/v1/country/<country_name>`
- **Method:** `GET`
- **URL Params:** `country_name=[string]`
- **Success Response:**
  - **Code:** 200
  - **Content:** JSON object containing COVID-19 data for the specified country.
- **Error Response:**
  - **Code:** 404
  - **Content:** `{"error": "No data found for country: [country_name]"}`

### 2. Get List of Countries

- **URL:** `/v1/countries`
- **Method:** `GET`
- **Success Response:**
  - **Code:** 200
  - **Content:** JSON array containing the names of countries available in the dataset.
- **Error Response:**
  - **Code:** 404
  - **Content:** `{"error": "No data found for countries"}`

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

