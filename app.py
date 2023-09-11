from flask import Flask, render_template_string
import pyodbc

app = Flask(__name__)

def get_data():
    # Define your database connection string
    conn_str = 'DRIVER={SQL Server};SERVER=bootcampserver2.database.windows.net;DATABASE=bootcampsep4server2;UID=bootcamp;PWD=Pass@123'

    # Connect to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Execute an SQL query to select the top 20 rows
    query = "SELECT TOP 20 CONCAT(FirstName, ' ', MiddleName, ' ', LastName) AS Name, CompanyName AS [Company Name], Phone AS [Phone Number] FROM SalesLT.Customer;"
    cursor.execute(query)

    # Fetch the results
    results = cursor.fetchall()

    # Close the database connection when done
    conn.close()

    return results

@app.route('/')
def display_data():
    # Define your HTML template as a string
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Data Display</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container mt-5">
            <h1>Customer Information (By Rohit Byas [EMPN0692])</h1>
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Company</th>
                        <th>Phone</th>
                        <!-- Add more table headers for your data columns -->
                    </tr>
                </thead>
                <tbody>
                    {% for item in data %}
                        <tr>
                            <td>{{ item.Name }}</td>
                            <td>{{ item['Company Name'] }}</td>
                            <td>{{ item['Phone Number'] }}</td>
                            <!-- Add more table data cells for your data columns -->
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """

    # Get data from the database
    data = get_data()

    return render_template_string(template, data=data)

if __name__ == '__main__':
    app.run(debug=False)
