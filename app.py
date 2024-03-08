
from flask import Flask, request, render_template
import sqlite3, datetime

app = Flask(__name__)

#default route

@app.route('/')
def home():
    return "URL POST HOME PAGE - modified"

# Route to save an email in the SQLite database
@app.route('/storeids/<email>',)
def store_email(email):
    
    #return str(email)

    if email:
        # Open a connection to the SQLite database
        conn = sqlite3.connect('email.db')
        cursor = conn.cursor()

        # Create a table if it doesn't exist
        cursor.execute('CREATE TABLE IF NOT EXISTS emails (id INTEGER NOT NULL PRIMARY KEY, email TEXT, datetime DEFAULT current_timestamp)')

        # Insert the email into the database
        cursor.execute('INSERT INTO emails (email) VALUES (?)', (email,))

        conn.commit()
        conn.close()

        return 'Email saved successfully'
    else:
        return 'Please provide an email parameter in the request body'


# Route to display stored emails
@app.route('/showblockids', methods=['GET'])
def show_emails():
    conn = sqlite3.connect('email.db')
    cursor = conn.cursor()
    
    # Retrieve all emails from the database
    cursor.execute('SELECT * FROM emails')
    emails = cursor.fetchall()
    
    conn.close()
    
    return render_template('showblockids.html', emails=emails)
    # Render a simple HTML page to display the emails
    #email_list = [email[0] for email in emails]
    #return '<br>'.join(email_list)

    

if __name__ == '__main__':
    
    app.run(debug=True, host='0.0.0.0', port=3000)