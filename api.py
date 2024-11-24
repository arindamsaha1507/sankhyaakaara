"""Module for API."""

from enum import Enum

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

from sankhyaakaara.languages import LANGUAGES, LanguageEnum
from sankhyaakaara.converter import Converter, Style

app = FastAPI()


# Enum for Styles
class StyleEnum(str, Enum):
    """Enum for supported styles."""

    UTTARA = "Uttara"
    ADHIKA = "Adhika"


# Response Model
class ConverterResponse(BaseModel):
    """Response model for the converter API."""

    result: str
    status: str
    number: int
    script: str
    style: str


@app.get(
    "/convert",
    response_model=ConverterResponse,
    summary="Convert number to Sanskrit word",
    description="API for converting a number to a Sanskrit word in the specified script and style.",
)
async def api_converter(
    number: int = Query(..., ge=0, description="A positive integer to convert."),
    script: LanguageEnum = Query(
        LanguageEnum.DEVANAGARI, description="The script for conversion."
    ),
    style: StyleEnum = Query(StyleEnum.UTTARA, description="The style for conversion."),
):
    """API for Sanskrit Number Converter."""

    script = script.capitalize()

    # Validate script
    if script not in LANGUAGES:
        raise HTTPException(
            status_code=400,
            detail=f"Script not supported. Supported scripts: {LANGUAGES}",
        )

    # Convert style to the appropriate enum
    style_enum = Style.ADHIKA if style == StyleEnum.ADHIKA else Style.UTTARA

    # Perform conversion
    try:
        result = Converter().get_word(number, script=script, style=style_enum)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Conversion error: {str(e)}"
        ) from e

    # Return response
    return ConverterResponse(
        result=result,
        status="success",
        number=number,
        script=script,
        style=style_enum.name,
    )
