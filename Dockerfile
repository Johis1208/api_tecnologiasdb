# Usar una imagen base de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos
COPY requirements.txt requirements.txt

# Instalar las dependencias
RUN pip install -r requirements.txt

# Copiar los archivos de la aplicación
COPY . .

# Exponer el puerto para FastAPI
EXPOSE 8080

# Comando para ejecutar la aplicación FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]