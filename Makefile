.PHONY: help

DOCKER_COMPOSE := docker compose -f ./docker-compose.yml

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

add: ## Add a new dependency
	$(DOCKER_COMPOSE) run --rm app sh -c "python manage.py startapp $(word 2, $(MAKECMDGOALS))"


