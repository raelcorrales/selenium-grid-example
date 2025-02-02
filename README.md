# Automated Selenium Grid with Docker Compose
Este proyecto proporciona una implementación de un Selenium Grid utilizando Docker Compose para realizar pruebas distribuidas en un entorno de contenedores. El proyecto está diseñado para facilitar la ejecución de pruebas automatizadas en múltiples navegadores de manera escalable, utilizando Selenium Hub y nodos de Chrome.

## Requisitos Previos

- **Docker** instalado y funcionando. [Instalar Docker](https://www.docker.com/)
- **Docker Compose** instalado. [Instalar Docker Compose](https://docs.docker.com/compose/install/)

## Estructura del Proyecto
Esta es la estructura del proyecto, dentro de la carpeta src puede ir el codigo de tu proyecto en python que use el Grid:
```
selenium-grid-docker/
├── docker-compose.yml       # Define los servicios para Selenium Grid
├── Dockerfile               # Construye la imagen del servicio "web"
├── src/
│   ├── example.py           # Script de prueba Selenium
│   ├── requirements.txt     # Dependencias de Python
├── README.md                # Documentación del proyecto
├── .gitignore               # Archivos que no se deben incluir en el repositorio
```


## Instalación

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/tu-usuario/selenium-grid-docker.git
    cd selenium-grid-docker
    ```

2. **Construir y ejecutar los contenedores con Docker Compose:**
    ```bash
    docker-compose up -d
    ```

    Este comando construye las imágenes necesarias y ejecuta todos los contenedores en segundo plano.

### Explicación de los archivos
- **docker-compose.yml**: Define los servicios de Selenium Hub, nodos de Chrome y el servicio web que ejecuta las pruebas
- **Dockerfile**: Construye la imagen del contenedor web con Python y las dependencias necesarias.
- **src/example.py**: Script que realiza una prueba simple en un navegador Chrome controlado por Selenium.
- **requirements.txt**: Contiene las dependencias necesarias, como Selenium.

### Variables de entorno

Se utilizan las siguientes variables de entorno en este proyecto:

- **SELENIUM_HUB_HOST:** Establecida en `hub` para apuntar al contenedor Hub.
- **SELENIUM_HUB_PORT:** Establecida en `4444` por defecto, que es el puerto expuesto para la comunicación de WebDriver.
- **SE_ENABLE_TRACING (Hub):** Habilita el rastreo de Selenium Grid (opcional).
- **SE_EVENT_BUS_HOST (Chrome):** Establece el host Hub.
- **SE_EVENT_BUS_PUBLISH_PORT (Chrome):** Establece el puerto de publicación para el bus de eventos.
- **SE_EVENT_BUS_SUBSCRIBE_PORT (Chrome):** Establece el puerto de suscripción para el bus de eventos.

### Contribuciones
Si deseas contribuir a este proyecto, por favor realiza un fork del repositorio y abre un pull request con tus cambios.