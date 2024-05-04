import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    print("print de prueba")

    # Verificar si la solicitud es un POST
    if req.method == 'POST':
        try:
            # Leer el cuerpo de la solicitud
            req_body = req.get_json()

            # Realizar acciones basadas en los datos recibidos
            # Por ejemplo, guardar los datos en una base de datos, procesarlos, envi
