## Speech-to-Text Transcription

This project is a Flask-based web application that uses the OpenAI Whisper ASR system to transcribe audio files to text.

## Features

- Upload audio files in .wav format
- Choose the language of the audio file (currently supports Turkish and English)
- View the transcription result

## Demo

You can watch a demo of the application in action below:

![audio](https://github.com/alpecevit/transcription_app/assets/89662849/d48bfa35-9b3a-4add-9e44-2d9a4a58328b)

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
