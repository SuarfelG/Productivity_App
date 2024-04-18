from flask import Flask ,render_template, Blueprint
view=Blueprint('view',__name__)


@view.route("/")
def home ():
    return render_template('index.html')
