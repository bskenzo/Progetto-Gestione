python -m pip install -r requirements.txt

start cmd /k flask run 
timeout 3
start /MAX chrome "http://127.0.0.1:5000/"