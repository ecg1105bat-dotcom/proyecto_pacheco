from flask import Blueprint, render_template

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