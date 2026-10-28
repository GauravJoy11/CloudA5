FROM python:3.9-slim
WORKDIR /cloud5
COPY python1.py .
CMD ["python","python1.py"]

