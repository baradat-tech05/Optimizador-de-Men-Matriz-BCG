📊 Matriz BCG - Optimizador de Menu para Rentabilidad Gastronómica

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
git clone https://github.com/baradat-tech05/matriz-boston.git
cd matriz-boston
Configurar variables de entorno:
Crea un archivo .env basado en la configuración del proyecto (ejemplo):

Ini, TOML
DB_NAME=matriz_db
DB_USER=root
DB_PASSWORD=root
DB_HOST=db
Levantar el entorno con Docker:

Bash
docker-compose up --build
El servidor estará disponible en: http://localhost:8000

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
Hito Técnico: Se resolvió exitosamente la gestión de sockets en entornos híbridos y la sincronización de contratos entre URL y Vistas, garantizando un flujo de datos sin interrupciones.

📈 Funcionalidades Clave
Dashboard BCG: Visualización gráfica de la posición competitiva de los productos.

API REST: Interfaz para integración con otros sistemas o herramientas de BI.

Seguridad: Implementación de variables de entorno para protección de datos sensibles.

👤 Autor
Jesus Baradat - https://www.linkedin.com/in/jesus-baradat/

Proyecto desarrollado como proyecto final del Bootcamp Desarollo de aplicaciones Fullstack Python Trainee.
