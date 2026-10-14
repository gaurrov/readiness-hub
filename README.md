# Student Readiness Web App

## Prerequisites

- Python 3.10+

## Setup & Run Instructions

1. **Clone the repository and navigate to the project directory:**
   ```bash
   cd readiness-hub
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # On Windows:
   python -m venv .venv
   .venv\Scripts\activate

   # On macOS/Linux:
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   flask --app app.routes run
   ```
   The application will start at `http://127.0.0.1:5000`.

5. **Run tests:**
   ```bash
   pytest
   ```
