# TodoList App

A django app to create a todolist and check for completion

You can visit webapp at `https://isktodo.herokuapp.com`

To retrieve, update and delete with API visit `https://isktodo.herokuapp.com/todos-api/todos/`

To add new todo task visit `https://isktodo.herokuapp.com/todos-api/todos/add`


## Usage for Local Development

First clone this repository and `cd` into the folder

Run the following command afterwards

Create virtual environment
```
python -m virtualenv .venv
```


Activate virtual environment (for linux)
```
source .venv/bin/activate
```

Install packages from requirements.txt
```
pip install -r requirements.txt
```

Run the django app
```python
python manage.py runserver --settings=todolist.settings.local
```
