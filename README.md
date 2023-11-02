# Cloud-Jumpers-Back

pasos para usar el backend:

clonar el repositorio

Paso 1: Clonar el repositorio desde GitHub

Abre una terminal o línea de comandos en tu computadora.

Navega al directorio donde deseas clonar el repositorio. Puedes hacerlo con el comando cd (cambiar directorio).

Clona el repositorio de GitHub utilizando el comando git clone y la URL del repositorio. Reemplaza URL_del_repositorio_en_GitHub con la URL real de tu repositorio en GitHub.

´´´git clone URL_del_repositorio_en_GitHub´´´

Paso 2: Crear y activar un entorno virtual

En la misma terminal, navega al directorio recién clonado que contiene tu proyecto. Usando el comando cd, ve al directorio raíz del proyecto.

´´´cd nombre_de_la_carpeta_del_proyecto´´´

Crea un entorno virtual utilizando venv o virtualenv. Puedes usar uno de los siguientes comandos, dependiendo de tu sistema operativo:

En sistemas Unix/Linux:

python3 -m venv venv

source venv/bin/activate

En sistemas Windows:

python -m venv venv

venv\Scripts\activate

El entorno virtual se activará, y deberías ver el nombre del entorno virtual en el indicador de la línea de comandos.

Paso 3: Instalar dependencias

Con el entorno virtual activado, puedes instalar las dependencias del proyecto desde el archivo requirements.txt que se encuentra en el repositorio. Ejecuta el siguiente comando:

pip install -r requirements.txt

Esto instalará todas las dependencias necesarias para el proyecto en el entorno virtual.

Paso 4: Ejecutar el proyecto

Una vez que todas las dependencias estén instaladas, puedes ejecutar el proyecto según las instrucciones proporcionadas en el README o la documentación del proyecto. Por lo general, esto implica ejecutar un servidor de desarrollo o realizar otras acciones específicas según las necesidades del proyecto.

correr el comando python manage.py runserver

y se ejecutará el proyecto en el puerto 8000
