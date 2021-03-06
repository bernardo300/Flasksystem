from flask import Flask, render_template, session, redirect, url_for, flash
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, IntegerField
from flask_wtf import FlaskForm
from flask import abort
from flask import Flask
from flask import redirect, render_template

from flask_bootstrap import Bootstrap

from flask_moment import Moment
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'minhachavefacil'
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    name = 'Gabriel'
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow())


@ app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@ app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name)


@ app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@ app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    age = IntegerField('How is old?', validators=[DataRequired()])
    submit = SubmitField('Submit')
    # app.add_url_rule('/', 'index', index)
