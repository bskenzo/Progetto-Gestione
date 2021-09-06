#!bin/sh

export FLASK_APP=app.py

osascript -e 'tell application "Terminal" to do script "cd && cd Desktop/progetto-test_finale_2 && flask run"'
sleep 3
open -a "Google Chrome" http://127.0.0.1:5000/

# per lanciare flask run devi essere nella cartella del progetto