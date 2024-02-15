from flask import Flask, jsonify, abort
import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Database connection parameters
db_config = {
    "dbname": os.getenv("DB_NAME", "default_db_name"),
    "user": os.getenv("DB_USER", "default_user"),
    "password": os.getenv("DB_PASSWORD", "default_password"),
    "host": os.getenv("DB_HOST", "default_host")
}

@app.route('/v1/country/<country_name>')
def get_country_data(country_name):
    # Connect to the database
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Execute your query using a parameterized statement
    try:
        query = """
        SELECT * FROM covid_cases 
        JOIN countries ON countries.country_id = covid_cases.country_id 
        WHERE LOWER(countries.name) = LOWER(%s)
        """
        cursor.execute(query, (country_name,))

        # Fetch all rows as a list of dictionaries
        rows = cursor.fetchall()

        # If no data found for the country, return 404
        if not rows:
            abort(404, description=f"No data found for country: {country_name}")

    except psycopg2.Error as e:
        # Handle database errors
        cursor.close()
        conn.close()
        abort(500, description=str(e))

    # Convert to list of dictionaries for JSON output
    result = [dict(row) for row in rows]

    cursor.close()
    conn.close()

    return jsonify(result)

@app.route('/v1/countries')
def get_countries():
    # Connect to the database
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Execute your query using a parameterized statement
    try:
        query = """
        SELECT name FROM countries
        """
        cursor.execute(query)

        # Fetch all rows as a list of dictionaries
        rows = cursor.fetchall()

        # If no data found for the country, return 404
        if not rows:
            abort(404, description=f"No data found for countries")

    except psycopg2.Error as e:
        # Handle database errors
        cursor.close()
        conn.close()
        abort(500, description=str(e))

    # Convert to list of dictionaries for JSON output
    result = [dict(row) for row in rows]

    cursor.close()
    conn.close()

    return jsonify(result)
if __name__ == '__main__':
    app.run(debug=False)