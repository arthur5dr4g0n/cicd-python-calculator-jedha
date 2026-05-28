FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir pytest flake8
CMD ["python", "-m", "pytest", "tests/"]
