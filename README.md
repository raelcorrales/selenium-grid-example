# Selenium Grid con Docker Compose

Este proyecto demuestra cómo configurar una Selenium Grid para pruebas distribuidas usando Docker Compose. Incluye un contenedor de Selenium Hub, varios contenedores de navegadores Chrome y un contenedor de servicio web ("web") que ejecuta tu script de prueba (`example.py`).

### Requisitos previos

- Docker instalado y funcionando ([https://www.docker.com/](https://www.docker.com/))
- Docker Compose instalado y funcionando ([https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/))

### Estructura del proyecto

```
docker-compose.yml  # Define los servicios para Selenium Grid
Dockerfile          # Construye la imagen del servicio "web"
src/
  - example.py      # Tu script de prueba Selenium
  - requirements.txt # Dependencias para el servicio "web"
```

2. **Iniciar la Selenium Grid**

    ```bash
    docker-compose up -d
    ```
    - Este comando construye la imagen del servicio "web" (si es necesario) y ejecuta todos los contenedores en modo detached (separado).

### Explicación de los archivos

**docker-compose.yml**

- Define servicios para Selenium Hub (`hub`) y navegadores Chrome (`chrome`) con capacidad de escalado.
- Configura puertos, variables de entorno y dependencias entre servicios.
- Puedes escalar la cantidad de navegadores Chrome ajustando la configuración `replicas` en el archivo `docker-compose.yml` para el servicio `chrome`.

**Dockerfile**

- Construye la imagen de Python 3.12 para el servicio "web".
- Instala dependencias de Python desde `requirements.txt`.
- Copia tu script de prueba (`example.py`) y los archivos del proyecto.
- Establece el comando para ejecutar `example.py` cuando se inicia el contenedor.

**example.py** (ubicado en `src/`)

- Demuestra el uso de Selenium con un WebDriver remoto (Selenium Hub).
- Inicia un navegador Chrome a través del hub.
- Navega a una página web, encuentra un elemento e imprime el título.
- Cierra el navegador.

### Variables de entorno

Se utilizan las siguientes variables de entorno en este proyecto:

- **SELENIUM_HUB_HOST:** Establecida en `hub` para apuntar al contenedor Hub.
- **SELENIUM_HUB_PORT:** Establecida en `4444` por defecto, que es el puerto expuesto para la comunicación de WebDriver.
- **SE_ENABLE_TRACING (Hub):** Habilita el rastreo de Selenium Grid (opcional).
- **SE_EVENT_BUS_HOST (Chrome):** Establece el host Hub.
- **SE_EVENT_BUS_PUBLISH_PORT (Chrome):** Establece el puerto de publicación para el bus de eventos.
- **SE_EVENT_BUS_SUBSCRIBE_PORT (Chrome):** Establece el puerto de suscripción para el bus de eventos.

