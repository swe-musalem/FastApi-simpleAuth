Setting Up a Python Project with Virtual Environment and requirements.txt
Create a New Project Directory: 
Set up a new Python project directory on your local machine.

Navigate to the Project Directory: Open a terminal or command prompt and navigate to the project directory.

Create a Virtual Environment: Create a new virtual environment using the following command:


python3 -m venv venv
Activate the Virtual Environment: Activate the virtual environment:

On macOS and Linux:

source venv/bin/activate
On Windows:

venv\Scripts\activate
Create a requirements.txt file: Create a requirements.txt file that lists the necessary Python packages and their versions:

pip freeze > requirements.txt
