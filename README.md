# Starting a Python Web Application Project - Standard Operating Procedure (SOP)

This Standard Operating Procedure (SOP) defines the standardized process for initiating new Python web application projects. It aims to ensure **consistency, best practices, and efficient project setup** across all development efforts using the specified technology stack. Adherence to this SOP will **facilitate collaboration, simplify onboarding of new developers, and improve the overall quality and maintainability of web applications**. This SOP covers project initialization, dependency management, database setup, basic application structure, version control, and provides guidance for development workflow. It serves as a foundation for building robust and scalable web applications.

## 1. Technology Stack:

*   **Operating System:** macOS (specifically tested on 15.3.1, but generally applicable to other macOS versions)
*   **Hardware:** Mac Mini M1 (ARM-based architecture)
*   **Integrated Development Environment (IDE):** Visual Studio Code (VS Code)
*   **Programming Language:** Python 3 (managed with Pyenv)
*   **Virtual Environment:** `venv` (built-in Python module)
*   **Web Frameworks:**
    *   ***Flask*** (for traditional web applications)
    *   ***Streamlit*** (for data visualization-focused web applications)
*   **Version Control:** Git (managed on GitHub)
*   **Database:** SQLite3

## 2. Project Setup:

2.1. **Create Project Directory:**

Replace with the desired name for your project (e.g., my_webapp).

```bash
mkdir <project_name>
cd <project_name>
```

2.2. **Initialize Git Repository:**

```bash
git init
```

This initializes a new Git repository in the project directory.

2.3. **Create Virtual Environment:**

```bash
python3 -m venv .venv
```

This creates a virtual environment named `.venv` in the project directory.

2.4. **Activate Virtual Environment:**

```bash
source .venv/bin/activate
```

This activates the newly created virtual environment. Your terminal prompt should now be prefixed with `(.venv)`.

2.5. **Install Project Dependencies:**

Create a `requirements.txt` file in the project root. This file will list all project dependencies. Initially, it will likely contain:

```
Flask
Streamlit
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

2.6. **Create Main Application File:**

Create a file named `app.py` for Flask and `streamlit_app.py` for Streamlit in the project root. This will be the main entry point for the chosen web application framework.

```bash
touch app.py streamlit_app.py
```

## 3. Project Structure (Example):

```
/
├── .git/                      # Repository (Automatically created when ***Step 2.2*** is successful)
├── .venv/                     # Virtual environment (Automatically created when ***Step 2.3*** is successful)
├── app.py                     # Main application file - Flask
├── streamlit_app.py           # Main application file - Streamlit
├── requirements.txt           # Project dependencies
├── static/                    # Static files (CSS, JavaScript, images) - Flask
├── all_pages/                 # For Streamlit
├── assets/                    # Static files (images, icons) - Streamlit 
├── templates/                 # HTML templates - For Flask
├── data/                      # Data files (SQLite database, CSVs, etc.)
└── __init__.py                # Makes the directory a Python package (if needed)
```

## 4. Database Setup (SQLite3):

4.1. **Create Database File:**

***This template includes a blank database with a generic table name `table1`. You can change the table name as needed for your specific project or delete it and recreate your own.***

Create a file named `database.db` (or similar) inside the `data` directory. This will be your SQLite database file. You can create it by simply running the sqlite3 command-line tool. You must add something to the database to force it to actually save. See 

```bash
sqlite3 data/database.db
```

The above command should return a prompt that looks like this:

sqlite>

***This is example schema. Add your own schema if/when it is determined.***

```sqlite3
CREATE TABLE table1 (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    value TEXT NOT NULL
);
.exit
```

4.2. **Database Interactions:**

Use the `sqlite3` Python library to interact with the database within your `app.py` or `streamlit_app.py` files.

## 5. Flask Application Development (Example `app.py`):

```python
from flask import Flask, render_template # Import necessary modules
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('data/database.db')
    conn.row_factory = sqlite3.Row  # To access columns by name
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    # Example: Fetch data from the database
    # ...
    conn.close()
    return render_template('index.html')  # Example: Render an HTML template

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

## 6. Streamlit Application Development (Example `streamlit_app.py`):

```python
import streamlit as st
import sqlite3
import pandas as pd

st.title("My Streamlit App")

def get_data():
    conn = sqlite3.connect('data/database.db')
    # Example: Fetch data using pandas
    df = pd.read_sql_query("SELECT * FROM your_table", conn)
    conn.close()
    return df

df = get_data()
st.dataframe(df)  # Display the dataframe
# ... other Streamlit elements
```

## 7. Version Control (Git & GitHub):

7.1. **Create `.gitignore` file:**

Create a `.gitignore` file in the project root and add the following to exclude files that should not be committed to version control:

```
.venv/
__pycache__/
*.pyc
data/database.db  # Consider if you want to track database changes
```

7.2. **Commit Changes:**

```bash
git add .
git commit -m "Initial commit"
```

7.3. **Create GitHub Repository:**

Create a new repository on GitHub.

7.4. **Push to GitHub:**

```bash
git remote add origin <repository_url>
git branch -M main
git push -u origin main
```

## 8. Development Workflow:

*   Make changes to your code.
*   Test your application thoroughly.
*   Commit your changes regularly with descriptive commit messages.
*   Push your changes to GitHub.

## 9. Pyenv Usage (Python Version Management):

Pyenv is crucial for managing multiple Python versions on your system. Before starting a new project, follow these steps:

9.1.  **Install Pyenv (if not already installed):** 

1. Install Homebrew if not already installed:  

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Install pyenv using Homebrew:

```bash
brew update  
brew install pyenv
```

3. Add pyenv to your shell. For example, with Zsh, add the following to ~/.zshrc:

***This is important to get correct. You may need to modify based on your system.***

```bash
export PYENV_ROOT="$HOME/.pyenv"  
export PATH="$PYENV_ROOT/bin:$PATH"  
eval "$(pyenv init --path)"
```

4. Restart or reload your shell to apply the changes:

```bash
source ~/.zshrc
```

9.2.  **Set the Python version for the project:**

```bash
pyenv local <python_version> # e.g., pyenv local 3.9.13
```

This creates a `.python-version` file in your project directory, automatically setting the Python version when you're in the project.

9.3.  **Verify the Python version:**

```bash
python --version
```

This should show the Python version you set with Pyenv.

## 10. VS Code Integration:

10.1.  **Python Extension:** 

Install the official Python extension for VS Code. This provides support for code completion, linting, debugging, and more.

10.2.  **Select Interpreter:** 

In VS Code, use the "Python: Select Interpreter" command to choose the Python interpreter from your `.venv` environment. This ensures VS Code uses the correct dependencies.

## 11. Streamlit Specific Notes:

11.1.  **Running Streamlit Apps:** 

Use the command `streamlit run app.py` to start your Streamlit application.

11.2.  **Streamlit Documentation:** 

Refer to the official Streamlit documentation for detailed information on available components and functionalities. https://docs.streamlit.io/

## 12. Flask Specific Notes:

12.1.  **Running Flask Apps:** 

Use the command `flask run` (after setting the `FLASK_APP` environment variable to your `app.py` file or using Flask's automatic detection if named `app.py`) to start your Flask application, or `python app.py` if you have the `app.run()` call in your main file.

12.2.  **Flask Documentation:** 

Refer to the official Flask documentation for detailed information.

## 13. SQLite3 Best Practices:

13.1.  **Connection Management:** 

Ensure you properly close database connections after use to prevent resource leaks. The examples provided in this SOP demonstrate this.

13.2.  **Data Modeling:** 

Consider using a database migration tool (like Alembic) for more complex projects to manage database schema changes effectively.

## 14. Deployment

Deployment strategies will depend on your chosen platform (e.g., Heroku, AWS, PythonAnywhere). This SOP focuses on project setup.

***This SOP provides a comprehensive starting point for your Python web application project. Remember to adapt it to your specific needs and project requirements. Always consult the official documentation for Flask, Streamlit, and other tools you are using for the most up-to-date information.***
