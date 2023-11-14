# Uventures Project README

Welcome to the Uventures  project! This README provides a guide on how to set up and run the project locally.

## Prerequisites

Before you begin, make sure you have the following installed on your machine:

- [Python](https://www.python.org/) (version 3.6 or higher)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/) (recommended for isolating Python environments)

## Setting up the Virtual Environment

1. Open a terminal and navigate to the project directory:

    ```bash
    cd /path/to/Uventures
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

    You should see the virtual environment name in your terminal prompt, indicating that the virtual environment is active.

## Installing Dependencies

1. With the virtual environment activated, install the project dependencies using:

    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

1. Apply initial migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

## Running the Development Server

1. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the project.


2. Access the admin interface at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with the superuser credentials.

## Stopping the Development Server

To stop the development server, press `Ctrl + C` in the terminal where the server is running.

## Additional Information

- Customize the project settings in the `settings.py` file.
- Explore the project structure and add your apps to the `INSTALLED_APPS` list in `settings.py`.
- Refer to the [Django Documentation](https://docs.djangoproject.com/) for more information on Django features and best practices.

Happy coding! If you have any issues or questions, feel free to reach out to [Your Contact Information].# Uventures
