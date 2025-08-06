FROM python:3.11-slim

WORKDIR /app

# Copy main.py directly
COPY main.py /app/main.py

RUN pip install fastapi uvicorn redis

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
