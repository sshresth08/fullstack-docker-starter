# fullstack-docker-starter

A multi-service full-stack setup using Docker Compose — FastAPI + PostgreSQL running in isolated containers.

## Tech Stack
- Python 3.12 + FastAPI
- PostgreSQL 16
- Docker + Docker Compose

## Architecture
┌─────────────────┐     ┌─────────────────┐
│   API Service   │────▶│   DB Service    │
│  FastAPI :8000  │     │ PostgreSQL :5432 │
└─────────────────┘     └─────────────────┘
│                       │
└───────────────────────┘
Docker internal network

## Quick Start

```bash
git clone https://github.com/sshresth08/fullstack-docker-starter.git
cd fullstack-docker-starter
docker-compose up
```

API is available at: http://localhost:8000

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Hello World + DB connection info |
| GET | `/health` | Health check |

## Services

| Service | Image | Port |
|---------|-------|------|
| api | custom build (Python 3.12) | 8000 |
| db | postgres:16-alpine | 5432 |

## Stop & Clean up

```bash
# Stop services
docker-compose down

# Stop + delete volumes (resets database)
docker-compose down -v
```