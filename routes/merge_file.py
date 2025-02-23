# / routes / merge_file.py

# system library -------------------------------------------------------------

# packages -------------------------------------------------------------------
from flask          import Flask, send_from_directory, render_template, request
from flask          import send_file, redirect, url_for, Blueprint
from flask          import session, jsonify
#from flask_session  import Session
from werkzeug.utils import secure_filename
import sqlite3


# local library --------------------------------------------------------------
from config.app_config          import AppConfig
from src.document_handler       import DocumentHandler
from src.web_form_handler       import WebFormHandler

# route variables ------------------------------------------------------------
merge_blueprint = Blueprint(name='merge_file', import_name=__name__)


@merge_blueprint.route('/template', methods=['GET', 'POST'])
def upload_template():
    """Upload a new word template file"""

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        # grab the file
        file = request.files['file']

        # if filename is empty re-direct
        if file.filename == '':
            return redirect(request.url)
        
        # if file is valid, read the file contents
        if file:
            dh = DocumentHandler(filename=secure_filename(file.filename))
            # proccess the word file
            dh.process_docx(file.read())

        if dh.valid_placeholders:
            return redirect(url_for("merge_file.set_placeholder_type",
                            template_id=dh.template_id
                            ))


    return render_template("template.html",
                            version=AppConfig.VERSION.value,
                            )

@merge_blueprint.route('/set_placeholder_type/<int:template_id>', methods=['GET', 'POST'])
def set_placeholder_type(template_id:int):
    """Set the type (inline, list, bullet) for each placeholder."""

    wf = WebFormHandler(template_id=template_id)

    if request.method == 'POST':
        # get the placeholder type
        placeholders = request.form.getlist('placeholder[]')
        types = request.form.getlist('replacement_type[]')
        wf.process_placeholders(placeholder_data=placeholders, types=types)
        

        return redirect(url_for('base.index'))


    if request.method == 'GET':
        templates = wf.fetch_all_templates()
        
        return render_template("placeholder_type.html",
                            version=AppConfig.VERSION.value,
                            placeholders=wf.fetch_all_placeholders(),
                            template_id=template_id
                            )
    
