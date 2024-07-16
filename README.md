# TreeBo a state of the art sustainability ChatBot

## Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Briefly describe your project here.

## Prerequisites

Ensure you have the following installed:

- Python 3.8+
- pip (Python package installer)
- virtualenv (optional but recommended)
- PostgreSQL (or your preferred database)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```


## Running the Project

1. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

2. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

3. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The project will be accessible at `http://127.0.0.1:8000`.




## Contributing

To contribute to this project:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---
