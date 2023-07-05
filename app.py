from flask import Flask, render_template, request
import requests
import sqlite3

app = Flask(__name__)
DATABASE = 'country_data.db'

def create_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS countries (
                            country_name TEXT PRIMARY KEY,
                            capital TEXT,
                            population INTEGER,
                            currency TEXT,
                            flag TEXT
                        )''')

def set_values(country):
    country_name = str(country['name']['common'])
    capital = str(country['capital'][0])
    currencies = country.get('currencies', {})
    currency_code = next(iter(currencies.keys()), 'N/A')
    currency_name = currencies.get(currency_code, {}).get('name', 'N/A')
    population = country.get('population', 0)
    flag = country.get('flags', {}).get('png', '')

    return [country_name, capital, currency_name, population, flag]

def insert_countries(countries):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        country = set_values(countries[0])
        sql = "INSERT OR IGNORE INTO countries (country_name, capital, population, currency, flag) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(sql, (country[0], country[1], country[2], country[3], country[4]))

def fetch_country(country_name):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM countries WHERE country_name=?", (country_name,))
        country = cursor.fetchone()
    return country

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    country_name = request.form.get('country')
    country = fetch_country(country_name)

    if country:
        return render_template('result.html', country=country)
    else:
        url = f'https://restcountries.com/v3.1/name/{country_name}'
        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200 and data:
                countries = data
                insert_countries(countries)
                country = set_values(countries[0])
                return render_template('result.html', country=country)
            else:
                return render_template('error.html')
        except requests.exceptions.RequestException:
            return render_template('error.html')

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
