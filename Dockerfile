
FROM python:3.9

WORKDIR / spam_prediction

COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY app.py .
COPY spam.csv .
COPY spam.pkl .
COPY train_model.py .
COPY vectorizer.pkl .

EXPOSE 8501 

CMD ["streamlit","run","app.py"]