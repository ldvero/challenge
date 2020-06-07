import logging
import boto3
from botocore.exceptions import ClientError

def uploadFileS3():

    client = boto3.client('s3')

    conf = input("YES/NO: ")

    while (conf == "YES"):

        bucketName = input("Ingrese el nombre del bucket en el cual desea subir el archivo:   ")
        path = input("Ruta del archivo para subir:  ")
        outputName = input("Nombre de archivo para guardar en el bucket:  ")
        try:
            client.upload_file(path, bucketName, outputName)
            print("El archivo fue cargado con ")
        except ClientError as e:
           logging.error(e)
           print("El archivo no ha sido subido con exito")

def downloadFileS3():

    client = boto3.client('s3')

    conf = input("YES/NO: ")

    while (conf == "YES"):

        bucketName = input("Ingrese el nombre del bucket del cual desea descargar el archivo:   ")
        path = input("Ruta del archivo para descargar:  ")
        saveName = input("Nombre de archivo para descargar del bucket: ")
        try:
            client.download_file(bucketName, path, saveName)
            print("El archivo ha sido descargado")
        except ClientError as e:
            logging.error(e)
            print("No se pudo descargar el archivo")


if __name__ == "__main__":

    print("¿Cargar un archivo a un bucket?")
    uploadFileS3()
    print("¿Descargar un archivo desde un bucket?")
    downloadFileS3()
