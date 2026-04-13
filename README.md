📊 Matriz BCG - Optimizador de Menú para Rentabilidad Gastronómica

📝 Descripción del Proyecto
Este sistema automatiza el análisis de la Matriz BCG (Boston Consulting Group) para la gestión estratégica de menús en el sector gastronómico. La aplicación calcula la rentabilidad y popularidad de cada plato, clasificándolos automáticamente en los cuadrantes: Estrella, Vaca, Interrogante y Perro.
El proyecto ha sido desarrollado bajo un enfoque de QA-First, asegurando que la lógica de negocio sea verificable mediante una API REST antes de su visualización en el frontend.

🛠️ Stack Tecnológico
Backend: Django 5.x (Python)

Base de Datos: MySQL (Persistencia de datos)

Contenedores: Docker & Docker Compose

Testing: Postman para validación de API

🚀 Instalación y Despliegue
Este proyecto está completamente contenedorizado para garantizar que funcione en cualquier entorno (Windows, Linux, Mac).

Clonar el repositorio:
Bash
git clone https://github.com/baradat-tech05/Optimizador-de-Men-Matriz-BCG.git
cd matriz-boston

🛠️ Configuración para Entorno Local (Windows)
Si vas a ejecutar este proyecto localmente sin Docker, sigue estos pasos:

1. Requisitos Previos:
Python 3.10+ instalado.

MySQL Server instalado y corriendo localmente.

Base de datos creada manualmente:

SQL:
CREATE DATABASE matriz_bcg;

2. Entorno Virtual y Dependencias:
Desde la raíz del proyecto, crea y activa el entorno virtual, luego instala las librerías necesarias:

PowerShell

python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

3. Configuración de Base de Datos
Debido a que la configuración original está diseñada para Docker, debes ajustar el archivo backend/core/settings.py (o el archivo .env si se utiliza):

Host: Cambiar 'db' por '127.0.0.1'.

User/Password: Asegurarse de que coincidan con tus credenciales de MySQL local.

Ejemplo en settings.py:

Python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'matriz_bcg',
        'USER': 'root', 
        'PASSWORD': 'tu_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

4. Variables de Entorno y Migraciones
Dado que el código fuente reside en la carpeta /backend, es necesario indicar a Python la ruta del proyecto antes de ejecutar comandos de Django:
En PowerShell:
PowerShell

 Configurar la ruta del código:
$env:PYTHONPATH=".\backend"

 Ejecutar migraciones:
python manage.py migrate

 Crear usuario administrador:
python manage.py createsuperuser
5. Ejecución del Servidor
Para levantar el proyecto, usa siempre el prefijo del PYTHONPATH:

PowerShell

$env:PYTHONPATH=".\backend"; python manage.py runserver
Luego accede a: http://127.0.0.1:8000/

🧪 Validación de Calidad (QA)
Como parte del proceso de aseguramiento de calidad, se implementó un endpoint de API para validar la integridad de los datos de cada plato.

Prueba de Endpoint con Postman
Método: GET

URL: http://localhost:8000/api/platos/1/

Resultado esperado (Status 200 OK):

JSON
{
    "id_interno": 1,
    "nombre_producto": "pizza margherita",
    "precio": 13500.0,
    "categoria_actual": "Principal",
    "status_qa": "Data Verified"
}

![Matriz bcg postman 200 ok](https://github.com/user-attachments/assets/9b4826de-acba-4f25-bcbf-a2d347d61fd3)

Logro Técnico: 
Se resolvió exitosamente la persistencia y comunicación de datos en entornos híbridos y la sincronización entre endpoints, garantizando un flujo de datos sin interrupciones.


📈 Funcionalidades Clave:
Dashboard BCG: Visualización gráfica de la posición competitiva de los productos.

API REST: Interfaz para integración con otros sistemas o herramientas de BI.

Seguridad: Implementación de variables de entorno para protección de datos sensibles.

👤 Autor
Jesus Baradat - https://www.linkedin.com/in/jesus-baradat/

Aplicación desarrollada como proyecto final del Bootcamp Desarrollo de aplicaciones Fullstack Python Trainee.
