# Nginx Reverse Proxy + Backend (Docker Compose)

## Описание

Проект поднимает два контейнера:

- `nginx` (reverse proxy) принимает HTTP-запросы на `80` порту хоста
- `backend` отвечает текстом `Hello from Effective Mobile!` на путь `/`

`backend` доступен только внутри docker-сети и не публикуется наружу.

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

## Требования

- Docker
- Docker Compose (плагин `docker compose`)

## Быстрый старт

```bash
cp .env.example .env
docker compose up -d --build
```

## Проверка результата

1. Проверка ответа приложения через nginx:

```bash
curl http://localhost
```

Ожидаемый ответ:

```text
Hello from Effective Mobile!
```

2. Проверка состояния сервисов:

```bash
docker compose ps
```

3. Проверка healthcheck'ов:

```bash
docker inspect --format='{{json .State.Health.Status}}' em-backend
docker inspect --format='{{json .State.Health.Status}}' em-nginx
```

## Остановка и очистка

Остановка контейнеров:

```bash
docker compose down
```

Остановка и удаление volumes (если нужны):

```bash
docker compose down -v
```

## Переменные окружения

Файл `.env` создается из `.env.example`.

- `BACKEND_CONTAINER_NAME` имя контейнера backend
- `NGINX_CONTAINER_NAME` имя контейнера nginx
- `BACKEND_PORT` внутренний порт backend (по умолчанию `8080`)
- `NGINX_HOST_PORT` порт хоста для nginx (по умолчанию `80`)
- `DOCKER_NETWORK_NAME` имя bridge-сети docker

## Как это работает

```text
Client (curl/browser)
        |
        v
localhost:80
        |
        v
nginx container (service: nginx)
        |
        v
proxy_pass -> backend:8080
        |
        v
backend container (service: backend)
```

- В `nginx/nginx.conf` настроен `upstream backend_upstream` -> `backend:8080`.
- Путь `/` проксируется в backend через `proxy_pass`.
- Backend не имеет `ports`, только `expose`, поэтому с хоста напрямую недоступен.

## Полезные команды

Логи сервисов:

```bash
docker compose logs -f
```

Логи конкретного сервиса:

```bash
docker compose logs -f nginx
docker compose logs -f backend
```

Проверка итогового compose-конфига после подстановки `.env`:

```bash
docker compose config
```

## Troubleshooting

- Ошибка `Bind for 0.0.0.0:80 failed: port is already allocated`:
  порт `80` занят на хосте. Измените `NGINX_HOST_PORT` в `.env`, например на `8081`.
- `curl http://localhost` не отвечает:
  проверьте `docker compose ps`, затем `docker compose logs -f nginx backend`.
- Backend unhealthy:
  проверьте, что backend слушает `0.0.0.0:8080` и доступен `http://127.0.0.1:8080/health` внутри контейнера.

## Технологии

- Docker
- Docker Compose
- Nginx (official image)
- Python `http.server`
