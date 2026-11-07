# SE-B13-ASSIGN3-APILearning
Create FASTAPI and relvant details

## Run the API

With the virtual environment activated, install the server and start the app:

```powershell
python -m pip install uvicorn
python -m uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs for the interactive API documentation.
Running `python main.py` checks that the module loads, but does not start a server.

To add two numbers, send a GET request to
`http://127.0.0.1:8000/sum?num1=2&num2=3`. The response is `{"sum": 5.0}`.
