# Utiliza una imagen base de Python 3.12
FROM python:3.12

# Establece el directorio de trabajo en el contenedor
WORKDIR /home/user

# Copia los archivos del proyecto al contenedor
COPY ./src /home/user

# Instala las dependencias desde requirements.txt
RUN pip install -r requirements.txt

# Establece el comando predeterminado
CMD ["tail", "-f", "/dev/null"]
