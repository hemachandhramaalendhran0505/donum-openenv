FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn pydantic numpy

CMD ["uvicorn", "api.server:app", "--host", "0.0.0.0", "--port", "7860"]