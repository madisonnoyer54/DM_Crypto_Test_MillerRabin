# Makefile pour le projet test de MillerRabin


help:
	@echo "Action disponibles:"
	@echo "  install   - Installer les dépendaces"
	@echo "  run       - Exécuter le script"

install:
	pip install matplotlib

run:
	python3 main.py
