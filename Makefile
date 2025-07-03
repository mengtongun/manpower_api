# Makefile for Manpower API

.PHONY: help init-db up down logs ps build seed

default: help

help:
	@echo "Available commands:"
	@echo "  make init-db    Initializes the database. Creates the DB and tables."
	@echo "  make up         Starts services in detached mode."
	@echo "  make down       Stops and removes services, networks, and volumes."
	@echo "  make logs       Follows the logs of running services."
	@echo "  make ps         Lists running containers."
	@echo "  make help       Shows this help message."

init-db:
	@echo "--> Initializing database..."
	@docker exec manpower_db /opt/mssql-tools18/bin/sqlcmd -S localhost -U ${DB_USERNAME} -P ${DB_PASSWORD} -C -Q "CREATE DATABASE ${DB_NAME};"
	@echo "--> Database initialization complete."

seed:
	@echo "--> Seeding database..."
	@docker exec manpower_api python seed.py
	@echo "--> Database seeding complete."

build:
	@echo "--> Building services..."
	@docker compose build

up:
	@echo "--> Starting services..."
	@docker compose up -d

down:
	@echo "--> Stopping services and removing volumes..."
	@docker compose down -v

logs:
	@echo "--> Tailing logs..."
	@docker compose logs -f

ps:
	@echo "--> Checking container status..."
	@docker compose ps 