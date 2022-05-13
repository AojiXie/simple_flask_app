# simple_flask_app

This is a simple flask application with function:

## Installation

requires python 3.9+ and flask (https://flask.palletsprojects.com/en/2.1.x/) v2.1+ to run.

Install the dependencies and start the server.

```sh
cd simple_flask_app
python3 flask_test.py
```
The application will be running on http://127.0.0.1:5000

## Test
```sh
curl -X POST http://127.0.0.1:5000/test --data '{"string_to_cut": "anywordyouwant"}' -H 'Content-Type: application/json'
```
