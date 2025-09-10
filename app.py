from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# ✅ Gmail SMTP Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'chesangco3@gmail.com'  # Sender Gmail
app.config['MAIL_PASSWORD'] = 'mevi nuly wgbk  kdem'       # App password (no spaces)

mail = Mail(app)

# ✅ Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message_body = request.form['message']

    msg = Message(
        subject=f"New Contact from {name}",
        sender=app.config['MAIL_USERNAME'],
        recipients=['chesangco3@gmail.com'],  # Receiver Gmail
        body=f"""
You’ve received a new message from ChesangLTD’s website:

Name: {name}
Email: {email}

Message:
{message_body}

— ChesangLTD Web Contact
"""
    )
    mail.send(msg)
    return render_template('contact.html', success=True)


# ✅ Run the App
if __name__ == '__main__':
    app.run(debug=True)

