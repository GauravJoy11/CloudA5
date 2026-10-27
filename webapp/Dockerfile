FROM python:3.9-slim
WORKDIR /webapp
COPY webapp.py .
RUN pip install --no-cache-dir flask
CMD ["python","webapp.py"]
