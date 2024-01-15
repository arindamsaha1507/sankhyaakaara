"""Module for API."""

from fastapi import FastAPI

from languages import LANGUAGES
from converter import Converter, Style

app = FastAPI()

@app.get("/script/{script}/style/{style}/number/{number}")
async def api_converter(script: str, style: str, number: int):
    """API for Sanskrit Number Converter."""

    if script not in LANGUAGES:
        result = "Script not supported."
        status = "error"
    elif type(number) != int:
        result = "Number must be an integer."
        status = "error"
    elif number < 0:
        result = "Number must be positive."
        status = "error"
    elif style not in ["UTTARA", "ADHIKA"]:
        result = "Style must be either UTTARA or ADHIKA."
        status = "error"
    else:
        style = Style.ADHIKA if style == "ADHIKA" else Style.UTTARA
        result = Converter().get_word(number, script=script, style=style)
        status = "success"


    return {"result": result, "status": status, "scripts": LANGUAGES, "styles": [Style.ADHIKA.name, Style.UTTARA.name], "number": number, "script": script, "style": style.name}

