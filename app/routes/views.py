from flask import Blueprint, render_template, jsonify
from app.services.medicion_service import MedicionService

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    dato = MedicionService.obtener_ultima()
    return render_template("mediciones.html", dato=dato)

@main_bp.route("/mediciones")
def mediciones():
    dato = MedicionService.obtener_ultima()
    return render_template("mediciones.html", dato=dato)

@main_bp.route("/graficas")
def graficas():
     return render_template("graficas.html")

@main_bp.route("/historial")
def historial():
     datos = MedicionService.obtener_historial()
     return render_template("historial.html", datos=datos)

@main_bp.route("/valoresSensores")
def valores_sensores():
     dato = MedicionService.obtener_ultima()
     return jsonify(dato)

@main_bp.route("/datosGraficas")
def datos_graficas():
     registros = MedicionService.obtener_historial()
     registros = registros[:20][::-1]
     return jsonify([
        {
            "temperatura": float(r["temperatura"]),
            "humedad": float(r["humedad"]),
            "ph": float(r["ph"]),
            "hora": str(r["hora"])[:8]
        } for r in registros
     ])