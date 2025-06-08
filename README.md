# Comprehensive Biometric Identification System Using Deep Learning

Bio Tech is an innovative Multi-Biometric Identification System that uses both Fingerprint Recognition and Facial Recognition to reliably authenticate and identify individuals.

## Features

- Clean, modern UI with animations
- Three main pages: Home, About Us, and Features
- Integration with external biometric identification services
- Responsive design for all devices

## Prerequisites

- Python 3.6 or higher
- Flask

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:

```
pip install -r requirements.txt
```

## Running the Application

To run the application, execute the following command in the project directory:

```
python app.py
```

The website will be available at `http://127.0.0.1:5000/`

## Project Structure

- `app.py` - Main Flask application
- `templates/` - HTML templates
  - `base.html` - Base template with navigation and footer
  - `home.html` - Home page
  - `about.html` - About Us page
  - `features.html` - Features page
- `static/` - Static files
  - `css/` - CSS stylesheets
  - `js/` - JavaScript files
  - `images/` - Images used in the website

## External Services

The website integrates with the following external biometric services:

- Fingerprint Recognition: [https://fingerprint.streamlit.app/](https://fingerprint.streamlit.app/)
- Face Recognition: [https://face-gemini-identifier-66.lovable.app/](https://face-gemini-identifier-66.lovable.app/)
