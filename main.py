from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['POST', 'GET'])
def index():
    username_error = ''
    password_error = ''
    confirm_error = ''
    email_error = ''
    username = ''
    user_password = ''
    confirm_password = ''
    email = ''

    if request.method == 'POST':
        username = (request.form['username'])
        email = (request.form['email'])
        user_password = (request.form['user_password'])
        confirm_password = (request.form['confirm_password'])

        if username == '' or len(username) < 3 or len(username) > 20 or ' ' in username:
            username_error = 'Username Invalid'
        if user_password == '' or len(user_password) < 3 or len(user_password) > 20 or ' ' in user_password:
            password_error = 'Password Invalid'
        if confirm_password != user_password:
            confirm_error = 'Password Invalid'
        if email == '':
            email_error = ''
        elif len(email) < 3 or len(email) > 20 or ' ' in email or '.' not in email or '@' not in email:
            email_error = 'Email Invalid'
        if username_error == '' and password_error == '' and email_error == '':
            return render_template('welcome.html', username=username)

    return render_template('inputs.html',title="Signups", username_error=username_error, password_error=password_error, confirm_error=confirm_error, email_error=email_error, username=username, email=email, )


if __name__ == '__main__':
    app.run()