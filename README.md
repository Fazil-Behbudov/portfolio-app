# Portfolio App

A personal portfolio website built entirely in Python to showcase coding projects and apps.


## About
This project is a personal portfolio site developed with Python. It serves as a showcase for programming projects and applications.


## Features
- Display project highlights and summaries  
- Contact form with email sending functionality  
- Structured layout for easy navigation  
- Modular and easy-to-extend codebase

## Tech Stack
- Python (for backend logic)  
- `Home.py` — main application script  
- `send_mail.py` — handles email sending (likely via SMTP or an API)  
- `data.csv` — data source for projects or content  
- Static assets and templates stored in `images/` and `pages/` directories  
- Optional: additional dependencies configurable via `requirements.txt`

## Project Structure
```
portfolio-app/
├── .devcontainer/           # Dev container config (if using VS Code DevContainers)
├── images/                  # Image assets
├── pages/                   # HTML templates or page modules
├── Home.py                  # Entry point or main application logic
├── send_mail.py             # Handles sending emails from contact form
├── data.csv                 # Dataset for project listings or content
├── .gitignore               # Files to ignore in Git version control
└── README.md                # This file
```

## Getting Started

### Prerequisites
- Python 3.x installed
- Recommended: create and activate a virtual environment
- Dependencies (if any) listed in `requirements.txt`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Fazil-Behbudov/portfolio-app.git
   cd portfolio-app
   ```
2. (Optional) Set up virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix/macOS
   venv\Scripts\activate     # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App
Depending on your setup, run the app with:
```bash
python Home.py
```
Then open your browser and navigate to `http://localhost:<PORT>`.

## Usage
- View your portfolio on the homepage.
- Submit the contact form to send an email (ensure `send_mail.py` is configured correctly with SMTP credentials or API keys).
- Projects and details are pulled from `data.csv`; edit this file to modify project listings.

## Deployment
*(Optional: Describe how to deploy the app, such as using Heroku, Vercel, or a VPS.)*

## Contributing
Contributions are welcome!  
1. Fork the project  
2. Create a new branch (`git checkout -b feature/my-feature`)  
3. Make your changes and commit (`git commit -m 'Add some feature'`)  
4. Push to the branch (`git push origin feature/my-feature`)  
5. Open a Pull Request

## License
*(Add your license here, e.g., MIT, Apache 2.0, or “All rights reserved.”)*

## Contact
Fazil Behbudov — [your email or portfolio link]

Project Link: [https://github.com/Fazil-Behbudov/portfolio-app](https://github.com/Fazil-Behbudov/portfolio-app)

