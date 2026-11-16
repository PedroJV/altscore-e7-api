from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, Response

app = FastAPI()

# ---------- E7 ----------
CODIGOS = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05",
}

SISTEMA_AVERIADO = "engines"


@app.get("/status")
def status():
    return {"damaged_system": SISTEMA_AVERIADO}


@app.get("/repair-bay", response_class=HTMLResponse)
def repair_bay():
    codigo = CODIGOS[SISTEMA_AVERIADO]
    return f"""<!DOCTYPE html>
<html>
<head>
    <title>Repair</title>
</head>
<body>
<div class="anchor-point">{codigo}</div>
</body>
</html>"""


@app.post("/teapot")
def teapot():
    return Response(status_code=418)


# ---------- E9 ----------
P_MIN, P_CRIT = 0.05, 10.0
V_CRIT = 0.0035
V_LIQUIDO_MIN = 0.00105
V_VAPOR_MIN = 30.0


@app.get("/phase-change-diagram")
def phase_change_diagram(pressure: float = Query(..., ge=P_MIN, le=P_CRIT)):
    fraccion = (pressure - P_MIN) / (P_CRIT - P_MIN)
    v_liquido = V_LIQUIDO_MIN + fraccion * (V_CRIT - V_LIQUIDO_MIN)
    v_vapor = V_VAPOR_MIN + fraccion * (V_CRIT - V_VAPOR_MIN)
    return {
        "specific_volume_liquid": round(v_liquido, 8),
        "specific_volume_vapor": round(v_vapor, 8),
    }
