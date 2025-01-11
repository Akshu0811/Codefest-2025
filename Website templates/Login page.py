from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Create a JSON file to store user credentials
users_data = {
    "users": []
}

with open('login.json', 'w') as file:
    json.dump(users_data, file, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_email', methods=['POST'])
def submit_email():
    email = request.form['email']
    # Load the existing data
    with open('login.json', 'r') as file:
        data = json.load(file)
    
    # Add the email to the data
    data['users'].append({"email": email})
    
    # Save the data back
    with open('login.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    return "Email submitted successfully!"

if __name__ == "__main__":
    app.run(debug=True)