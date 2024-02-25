from flask import Flask, render_template, redirect, session, url_for, abort
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
import os
from models.model import get_transcription
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor

model_id = "openai/whisper-large-v3"
model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch.float32, low_cpu_mem_usage=True,
    use_safetensors=True)
model.to("cpu")
processor = AutoProcessor.from_pretrained(model_id)


class WavForm(FlaskForm):
    file = FileField(label='Upload your file:', validators=[FileRequired()])
    language = SelectField(label='Choose your language:',
                           validators=[DataRequired()],
                           choices=[('tr', 'tr'), ('en', 'en')])
    submit = SubmitField()


app = Flask(__name__)

app.config['SECRET_KEY'] = ''
app.config['UPLOAD_EXTENSIONS'] = ['.wav']
app.config['UPLOAD_FOLDER'] = 'static/uploaded_files/'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = WavForm()

    if form.validate_on_submit():
        f = form.file.data
        language = str(form.language.data)
        filename = secure_filename(f.filename)

        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            else:
                actual_file = app.config['UPLOAD_FOLDER'] + filename
                session['filename'] = filename
                session['text'] = get_transcription(actual_file, language,
                                                    model, processor)

                return redirect(url_for('results'))
        else:
            abort(400)

    return render_template('index.html', form=form)


@app.route('/results', methods=['GET', 'POST'])
def results():
    text = session['text']
    filename = session['filename']
    session.clear()
    return render_template('results.html', text=text,
                           filename=filename)


if __name__ == '__main__':
    app.run()
