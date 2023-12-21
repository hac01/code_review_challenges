from flask import Flask, render_template, send_file, request
import csv
from io import StringIO

app = Flask(__name__)

csv_data = [
    {'Name': 'John Doe', 'Age': 25, 'Occupation': 'Engineer'},
    {'Name': 'Jane Smith', 'Age': 30, 'Occupation': 'Designer'},
    {'Name': 'Bob Johnson', 'Age': 22, 'Occupation': 'Developer'},
]

@app.route('/')
def index():
    return render_template('index.html', data=csv_data)

@app.route('/download_csv')
def download_csv():
    # Create a CSV string from the data
    csv_string = StringIO()
    csv_writer = csv.DictWriter(csv_string, fieldnames=['Name', 'Age', 'Occupation'])
    csv_writer.writeheader()
    csv_writer.writerows(csv_data)

    filename = request.args.get('filename', 'data.csv')

    response_headers = {
        'Content-Type': 'text/csv',
        'Content-Disposition': f'attachment; filename={filename}',
    }

    return send_file(csv_string, mimetype='text/csv', as_attachment=True, download_name=filename, headers=response_headers)

if __name__ == '__main__':
    app.run(debug=True)
