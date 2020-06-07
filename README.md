# Work Sample

Documentación de como fue diseñado el script:

Tecnologías: 
- Python 3.7+: fue utilizado para poder crear el script que nos permitirá subir los archivos al bucket de Amazon s3 a través del SDK boto3, que nos permite utilizar los servicios de Amazon s3 y Amazon EC2.
- AWS CLI
- Librerías boto3 y botocore

Script:

Utilizamos dos funciones de carga y descarga de los archivos:

- client.upload_file(path, bucketName, outputName)
- client.download_file(bucketName, path, saveName)

En este caso, el bucket que cree en mi cuenta de AWS fue challengenoc (console.aws.amazon.com/s3/buckets/challengenoc)

Sincronización entre S3 y EC2:

- Conexión remota a la instancia EC2:
   A través de una consola donde ejecutamos el comando ssh -i para el acceso a la misma.
   Dentro de ella, para poder realizar la conexión a la cuenta de Amazon, es necesario configurar las credenciales de la siguiente manera:
   $ aws configure
   AWS Access Key ID [None]: 
   AWS Secret Access Key [None]: 
   Default region name [None]: 
   Default output format [None]: 
    
   Investigando, encontré que existen al menos 2 formas para poder realizar la sincronización:
    - Clonar mi repositorio de github donde se encuentra, el script utilizado anteriormente para la carga y descarga de archivos de nuestra pc al bucket y correrlo dentro de la instancia.
    - Utilizando los comandos de aws sync, de AWS CLI.

  También, encontré que existe la posibilidad de generar un archivo crontab que nos permitiría automatizar la actualización de la sincronización entre S3 y EC2, pero no logré desarrollarlo.


Consideraciones extras:
  -Seguridad:
    Me parece un punto sumamente importante a la hora de carga y descarga de archivos. Estuve investigando y a futuro, en caso de que nuestras instancias de EC2 reciban aplicaciones web, el servicio de Elastic Load Balancing de AWS permite distribuir el tráfico de las aplicaciones. 
    
   
