from flask import Blueprint, render_template, jsonify
from app.services.medicion_service import MedicionService


main_bp = Blueprint("main", __name__)

@main_bp.route("/")
@main_bp.route("/mediciones")

def mediciones():
    dato = MedicionService.obtener_ultima()
    return render_template("mediciones.html", dato=dato)


@main_bp.route("/graficas")

def graficas():
    return render_template("graficas.html")


@main_bp.route("/historial")

def historial():
    registros = MedicionService.obtener_historial()
    return render_template("historial.html", registros=registros)


@main_bp.route("/valoresSensores")

def valores_sensores():
    dato = MedicionService.obtener_ultima()
    return jsonify({
        "temperatura": float(dato.get("temperatura", 0)),
        "humedad": float(dato.get("humedad", 0)),
        "ph": float(dato.get("ph", 0))

    })


@main_bp.route("/datosGrafica")
def datos_graficas():
    registros = MedicionService.obtener_historial()

    #solamente los ultimos 20
    registros = registros[:20][::-1]
    return jsonify([
        {
            "temperatura": float(r["temperatura"]),
            "humedad": float(r["humedad"]),
            "ph": float(r["ph"]),
            "hora": str(r["hora"])
        } for r in registros
    ])
    





"""
main_bp = Blueprint("main", __name__)

# Datos simulados
# Después los conectamos a la BD real
DATO_EJEMPLO = {
    "temperatura": 6.87,
    "humedad": 8,
    "ph": 25
}

HISTORIAL_EJEMPLO = [
    {"id": 174, "temp": 6.63, "hum": 24.0, "ph": 25.0, "fecha": "2026-11-10", "hora": "10:00:15"},
    {"id": 173, "temp": 6.44, "hum": 28.0, "ph": 30.0, "fecha": "2026-11-10", "hora": "10:00:10"},
    {"id": 172, "temp": 6.93, "hum": 20.0, "ph": 20.0, "fecha": "2026-11-10", "hora": "10:00:05"},
]

@main_bp.route("/")
@main_bp.route("/mediciones")
def mediciones():
    return render_template("mediciones.html", dato=DATO_EJEMPLO)

@main_bp.route("/graficas")
def graficas():
    return render_template("graficas.html")

@main_bp.route("/historial")
def historial():
    return render_template("historial.html", registros=HISTORIAL_EJEMPLO)
"""