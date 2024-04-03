#!/bin/bash
# git clone https://github.com/avidaldo/machine-learning-python.git
# Cambia al directorio de tu repositorio de Git
cd machine-learning-python/

# Realiza un fetch para obtener las actualizaciones de las ramas remotas
echo "Realizando git fetch..."
git fetch

# Realiza un pull para fusionar las actualizaciones en la rama actual
echo "Realizando git pull..."
git pull

echo "Fetch y pull completados."
cd ../