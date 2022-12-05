from app.memes import bp
from flask import render_template
from flask login import login_required



@bp.route('/')
@login.required
def index():
    return render_template('memes/index.html')