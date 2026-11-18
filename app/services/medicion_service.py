#Capa de Servicio 
#En esta parte se debe conectar base de datos
#Por el momento es puro diseño :)

class MedicionService:
    @staticmethod
    def obtener_ultima():
        #TODO: conectar a base de datos
        return {"temperatura": 0, "humedad": 0, "ph": 0}

    @staticmethod
    def obtener_historial():
        #TODO: conectar a base de datos
        return[]