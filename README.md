# ReservamosChallenge

Rest API to get weather forecast 
## Prerequisites

Make sure you have the following software installed on your machine:

- [Python](https://www.python.org/downloads/) (version x.x)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [virtualenv](https://pypi.org/project/virtualenv/)

## Local Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Tuury/ReservamosChallenge.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd ReservamosChallenge
    ```

3. **Create a virtual environment:**

    ```bash
    virtualenv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. **Install project dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The development server will start at `http://127.0.0.1:8000/`.
