# Container specification - packages the app into an image.
FROM python:3.11-slim
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
