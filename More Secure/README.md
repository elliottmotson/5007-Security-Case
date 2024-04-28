## Setup

# Linux

python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

# Windows

python.exe -m venv venv
./venv/Scripts/activate
pip install -r .\requirements.txt

## Run

. venv/bin/activate
export FLASK_DEBUG=1
python app.wsgi


View your local web server here:

http://127.0.0.1:5000/