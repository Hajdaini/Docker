FROM python:3.6-alpine
COPY app/ /app/
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
