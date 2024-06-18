FROM python:3.10

WORKDIR /Users/1zuu/Library/Mobile Documents/com~apple~CloudDocs/ML STU/Docker for Data Science/Churn Prediction

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY src ./src
COPY artifacts ./artifacts

CMD ["python","app.py"]