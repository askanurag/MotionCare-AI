FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir .
CMD ["python", "-m", "healthcare_ai.cli", "train", "--csv", "data/demo.csv", "--output", "outputs/demo"]
