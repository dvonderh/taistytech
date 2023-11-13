# app.py
from flask import Flask, render_template, redirect, url_for, session
from flask_oidc import OpenIDConnect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dvonderh'
app.config['OIDC_CLIENT_SECRETS'] = 'client_secrets.json'  # Create this file with your Azure AD app info
app.config['OIDC_ID_TOKEN_COOKIE_SECURE'] = False
app.config['OIDC_REQUIRE_VERIFIED_EMAIL'] = False
oidc = OpenIDConnect(app)

@app.route('/')
def home():
    if oidc.user_loggedin:
        return 'Logged in as: ' + oidc.user_getfield('preferred_username')
    return 'Not logged in!'

@app.route('/login')
@oidc.require_login
def login():
    return redirect(url_for('.home'))

@app.route('/logout')
def logout():
    oidc.logout()
    return 'Logged out'

if __name__ == '__main__':
    app.run(debug=True)

