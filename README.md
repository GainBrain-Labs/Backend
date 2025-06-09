create virtual env
python -m venv venv

then activate it 
venv\Scripts\activate

the install dependencies
pip install -r requirements.txt

then go to app
cd app

then run server
uvicorn main:app --reload


OR

run from backend folder directly
uvicorn app.main:app --reload
