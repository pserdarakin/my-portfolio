# main.py

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@example.com'

mail = Mail(app)

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        # Send the email
        msg = Message("New Contact Form Submission",
                      recipients=['your_recipient_email@example.com'])
        msg.body = f"""
        New contact form submission:
        
        Name: {form.name.data}
        Email: {form.email.data}
        Message: {form.message.data}
        """
        mail.send(msg)
        flash('Your message has been sent. Thank you!')
        return redirect(url_for('home'))
    return render_template("index.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
