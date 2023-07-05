Certainly! Here's an updated version of the README.md file that includes information on the Dockerfile:

```
# Country Details App

This is a simple Flask web application that allows users to search for country details such as the country name, capital, population, currency, and flag. The application retrieves the data from the REST Countries API and stores it in a SQLite database for future searches.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/country-details-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd country-details-app
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Make sure you are in the project directory and the virtual environment is activated (if applicable).

2. Run the Flask application:

   ```bash
   python app.py
   ```

3. Open your web browser and go to `http://localhost:5000` to access the application.

4. Enter a country name in the search form and click the "Search" button.

5. If the country details are available in the database, they will be displayed. Otherwise, the application will retrieve the details from the REST Countries API, store them in the database, and display them.

## Docker

To run the application using Docker, follow these steps:

1. Build the Docker image:

   ```bash
   docker build -t country-details-app .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 5000:5000 country-details-app
   ```

   The application will be accessible at `http://localhost:5000` in your web browser.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

Make sure to update the Docker-related instructions if there are any specific commands or considerations related to your Docker setup.