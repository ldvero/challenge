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

Sincronización entre S3 y EC2:

- remoto

#crontab
