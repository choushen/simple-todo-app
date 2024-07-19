# Simple Todo App

A todo app built with Django and PostgreSQL, designed for use in automation testing demos and tech tests.

## Features

- User authentication with custom user models
- Create, view, and delete todo items
- User-friendly interface with Django templates
- PostgreSQL integration for robust data handling

## Folder Structure

```
simple_todo_app/
├── accounts/
│   ├── migrations/
│   ├── templates/accounts/
│   ├── __init__.py
│   ├── account_manager.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── simple_todo_app/
│   ├── static/css/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todos/
│   ├── migrations/
│   ├── templates/todos/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── manage.py
```

## Getting Started

### Prerequisites

- Python 3.x
- Django
- PostgreSQL

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/simple_todo_app.git
   ```
2. Navigate to the project directory:
   ```
   cd simple_todo_app
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
4. Configure the PostgreSQL database settings in `simple_todo_app/settings.py`.

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser to access the admin panel:
   ```
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```
   python manage.py runserver
   ```

### Usage

1. Access the app at `http://127.0.0.1:8000/`.
2. Register a new user or log in with the superuser account.
3. Create, view, and delete todo items.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Work in Progress

This project is a work in progress. Here are some things I need to do:

- **Configure Unit Test Runner**: Ensure the unit test runner is properly configured for seamless test execution.
- **Integrate Docker**: Containerize the application using Docker for consistent and isolated environments.
- **Build a CI/CD Pipeline**: Implement a continuous integration and continuous deployment (CI/CD) pipeline to automate testing and deployment processes.

## Disclaimer

> **Disclaimer:** This project is under active development. The current state of the project is not representative of the final product. Contributions and suggestions are welcome.
