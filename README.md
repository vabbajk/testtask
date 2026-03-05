# Nginx Reverse Proxy + Backend (Docker Compose)

## Структура проекта

```text
.
├── backend/
│   ├── Dockerfile
│   └── app.py
├── nginx/
│   └── nginx.conf
├── .env.example
├── docker-compose.yml
└── README.md
```

## Как запустить

```bash
cp .env.example .env
docker compose up -d --build
```

## Как проверить

```bash
curl http://localhost
```

Ожидаемый ответ:

```text
Hello from Effective Mobile!
```

Проверка состояния контейнеров:

```bash
docker compose ps
```

Остановка:

```bash
docker compose down
```

## Как это работает

- `nginx` принимает входящий HTTP-трафик на порту `80` хоста.
- В `nginx.conf` настроен `upstream backend_upstream`, указывающий на сервис `backend:8080`.
- Запросы на путь `/` проксируются на backend.
- `backend` не публикует порт наружу и доступен только внутри docker-сети.

## Технологии

- Docker
- Docker Compose
- Nginx (official image)
- Python `http.server`
