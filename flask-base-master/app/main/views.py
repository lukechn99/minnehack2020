from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_rq import get_queue

from app import db
from app.main.forms import (
    SearchForm
    
)
from app.email import send_email
from app.models import User
from app.models import Courses

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('main/index.html')


@main.route('/about')
def about():
    editable_html_obj = EditableHTML.get_editable_html('about')
    return render_template(
        'main/about.html', editable_html_obj=editable_html_obj)


@main.route('/matches')
def matches():
	return render_template('main/matches.html')

@main.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if request.method == 'POST' and form.validate_on_submit():
        user_ids = Courses.query.filter_by(course_name=form.search.data)
        user_ids = [x.__dict__.get('user_id') for x in user_ids]
        users = []
        for u in user_ids:
            users.append(User.query.filter_by(id=u))
    return render_template('main/search.html', form=form, users=users)
    
# SQL :
# SELECT * FROM census 
# WHERE sex = F
# SQLAlchemy :
# db.select([census]).where(census.columns.sex == 'F')
# 
# SQL :
# SELECT state, sex
# FROM census
# WHERE state IN (Texas, New York)
# SQLAlchemy :
# db.select([census.columns.state, census.columns.sex]).where(census.columns.state.in_(['Texas', 'New York']))

# SELECT user_id
# FROM courses
# WHERE courses.course_name == query
    # queryCourse = []
    # users = User.query.all()
    # courses = Courses.query.all()
    # result = Courses.query.filter_by(Courses.course_name = query).all()
    # result = db.select([courses.columns.user_id]).where(courses.columns.course_name == query)
    # # result = ["id", "id"]
# # SELECT email, name 
# # FROM users
# # WHERE user_id == id
    # # course_name
    # # user_id
    # output = db.select([users.columns.email, users.columns.first_name, users.columns.last_name]).where(
        # user.column.id in result)
    
    # return render_template('main/results.html')
