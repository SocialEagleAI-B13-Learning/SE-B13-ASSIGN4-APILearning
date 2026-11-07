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

## Run the Streamlit app

1. In PowerShell, activate the project's virtual environment and install Streamlit:

   ```powershell
   .\venv\Scripts\Activate.ps1
   python -m pip install streamlit
   ```

2. Create `streamlit_test.py` with the following code:

   ```python
   import streamlit as st

   st.title("This is my Streamlit application")
   ```

3. Run the app from the project directory:

   ```powershell
   python -m streamlit run streamlit_test.py --server.showEmailPrompt false
   ```

4. Leave the terminal running. Streamlit prints a **Local URL**, usually
   http://localhost:8501. If the browser does not open automatically, open
   that URL manually. The page displays the heading **This is my Streamlit application**.

Press **Ctrl+C** in the terminal to stop the app.

## Grade manager

With Streamlit installed in the activated virtual environment, run:

```powershell
python -m streamlit run grade_app.py --server.showEmailPrompt false
```

Open the Local URL shown in the terminal (usually http://localhost:8501).
Enter a student name and a mark from 0 to 100, then select **Add student**.
The table shows each student's grade, and the page displays the class average,
highest mark, and lowest mark. The grade cutoffs are A: 90, B: 80, C: 70,
D: 60, and F: below 60.

Students are stored in Streamlit session state, so they survive script reruns
in the same session. They are not saved permanently; reloading the browser
or ending the session can reset the list. Press **Ctrl+C** to stop the app.
