# Stark Portfolio - Flask Version

This is a Flask-powered portfolio website with a modern design featuring a neon, ambient, transparent, and dark theme.

## Features

- Responsive design with neon/dark theme
- Dynamic sections: Home, Skills, Projects, Contact
- Contact form with server-side processing
- Animated typing text and hover effects
- Smooth scrolling navigation

## Setup Instructions

### Prerequisites

- Python 3.6+
- pip (Python package manager)

### Installation

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Create a `.env` file in the project root with:
   ```
   SECRET_KEY=your_secret_key_here
   EMAIL_USER=your_email_username
   EMAIL_PASSWORD=your_email_password
   ```

### Running the Application

1. With the virtual environment activated, run:
   ```
   python app.py
   ```
2. Open your browser and go to `http://127.0.0.1:5000/`

## File Structure

```
portfolio/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (create this)
├── static/
│   ├── css/
│   │   └── style.css   # Main stylesheet
│   ├── js/
│   │   └── script.js   # JavaScript for animations
│   └── img/            # Images folder
└── templates/
    ├── layout.html     # Base template
    └── index.html      # Main content template
```

## Customization

- Edit templates in the `templates/` directory to change content
- Modify CSS in `static/css/style.css` to change the appearance
- Update JavaScript in `static/js/script.js` for different behaviors

## Contact Form Setup

To enable the contact form functionality:
1. Uncomment the email sending code in `app.py`
2. Set your email credentials in the `.env` file
3. Ensure you're using app-specific passwords for Gmail or other providers that require it 