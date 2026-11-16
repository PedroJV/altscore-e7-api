from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Response

app = FastAPI()

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