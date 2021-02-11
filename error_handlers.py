
from flask import current_app, render_template, request, jsonify
from werkzeug.exceptions import HTTPException
import logging

logger = logging.getLogger('werkzeug')

@current_app.errorhandler(Exception)
def handle_exception(e):
    logger.exception("An exception occured: %s" % str(e))
    if isinstance(e, HTTPException):
        return e
    if request.path.startswith('/rest/'):
        return jsonify(Message="An unhandled error occured."), 500
    return render_template("error.html", e=e), 500


@current_app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404