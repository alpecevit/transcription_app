## Speech-to-Text Transcription

This project is a Flask-based web application that uses the OpenAI Whisper ASR system to transcribe audio files to text.

## Features

- Upload audio files in .wav format
- Choose the language of the audio file (currently supports Turkish and English)
- View the transcription result

## Demo

You can watch a demo of the application in action below:

![audio_final](https://github.com/alpecevit/transcription_app/assets/89662849/13dc1f98-784e-4ecc-8b2c-b177d7b923c7)

## Installation

1. Clone the repository
2. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage
Run the Flask application:

```bash
python app.py
```

Open a web browser and navigate to http://localhost:5000
Upload your .wav file and select the language
Click on the submit button to get the transcription
Code Overview
The application uses the Flask framework and the WTForms library for handling file uploads and form data. The Whisper ASR model from OpenAI is used for the transcription.

The WavForm class defines the form used for file upload and language selection. The index function handles the form submission and file processing. If the file is valid, it is saved and then transcribed using the get_transcription function from the models.model module. The transcription result is then stored in the session and the user is redirected to the results page where the transcription is displayed.
