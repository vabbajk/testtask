FROM python:3.12-slim

WORKDIR /app

COPY app.py /app/app.py

RUN useradd --create-home --shell /usr/sbin/nologin appuser \
    && chown -R appuser:appuser /app

USER appuser

EXPOSE 8080
CMD ["python", "app.py"]
