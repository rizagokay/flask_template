from flask import (
    Blueprint, render_template
)
from .auth import login_required


bp = Blueprint('index', __name__)


@bp.route('/')
@login_required
def index():
    return render_template('index/index.html')
