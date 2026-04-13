# Utilizamos una imagen oficial de Python
FROM python:3.11

# Para evita que Python genere archivos .pyc y permita ver logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo dentro del contenedor
WORKDIR /code

# Instacion de dependencias del sistema necesarias para MySQL
RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential pkg-config

# Instalar librerías de Python
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . /code/