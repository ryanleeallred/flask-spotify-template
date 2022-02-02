from flask import Flask, render_template, request


def create_app():

    app = Flask(__name__)

    # configuration variable to our app
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    @app.route("/", methods=['GET', 'POST'])
    def home():
        print('This runs whenever the page is loaded')
        user_input = ''
        if request.method == "POST":
            print('This runs when the form is submitted')
            user_input = request.values['search']
            print(user_input)
        # query for all users in the database
        return render_template('base.html', title='Home', user_input=user_input)

    return app
