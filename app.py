"""The app module."""

import os
import logging  # Added for logging
from logging.handlers import SysLogHandler  # Added for Papertrail logging

from dotenv import load_dotenv

import streamlit as st
import yaml
from sankhyaakaara.converter import Converter, Style
from sankhyaakaara.languages import LANGUAGES

load_dotenv()

# Initialize logger
logger = logging.getLogger("PapertrailLogger")  # Added for Papertrail logging
logger.setLevel(logging.INFO)  # Added for Papertrail logging
handler = SysLogHandler(
    # address=("logs5.papertrailapp.com", 29849)
    address=(os.getenv("PAPERTRAIL_HOST"), int(os.getenv("PAPERTRAIL_PORT")))
)  # Update to your Papertrail host/port
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)  # Added for formatting logs
handler.setFormatter(formatter)  # Added for Papertrail logging
logger.addHandler(handler)  # Added for Papertrail logging


def base_input(language: str, script: str, max_value: int, numeric: bool = True) -> int:
    """Returns a numeric input widget."""

    if numeric:
        return int(
            st.number_input(
                writer("instruction", language, script),
                value=1,
                min_value=0,
                max_value=max_value,
                step=1,
            )
        )

    query = st.text_input(writer("instruction", language, script))

    if query != "":
        try:
            ret = int(query)

            if ret < 0 or ret > max_value:
                st.error(f"{writer('range', language, script)} 0 - {max_value}.")
                return 0

            return ret

        except ValueError:
            st.error(writer("error", language, script))
            return 0

    return 0


def writer(content: str, language: str, script: str) -> str:
    """Returns the content in the specified script."""

    with open("ui_text.yml", "r", encoding="utf-8") as stream:
        settings = yaml.load(stream, Loader=yaml.FullLoader)

    content = settings[content][language]

    if script == "Devanagari":
        return content

    return Converter().change_script(content, script)


def main():
    """The main function."""

    st.set_page_config(layout="wide")

    converter = Converter()

    if "flag" not in st.session_state:
        st.session_state["flag"] = False

    language = "English"

    language = st.sidebar.selectbox(
        "Select Language (भाषां चिनु)", ["English", "Samskritam"]
    )
    logger.info("Language selected: %s", language)  # Log the language selection

    script = st.sidebar.selectbox(
        "Select Script (लिपिं चिनु)", options=LANGUAGES, index=13
    )
    logger.info("Script selected: %s", script)  # Log the script selection

    with st.sidebar:
        st.title(writer("options", language, script))

        st.write(f"### {writer('joiner', language, script)}")
        joiner = st.selectbox(
            writer("joiner_options", language, script),
            options=[
                writer("joiner_adhika", language, script),
                writer("joiner_uttara", language, script),
            ],
            index=0,
        )

        style = (
            Style.ADHIKA
            if converter.change_script(joiner, "Devanagari") in ["अधिक", "adhika"]
            else Style.UTTARA
        )
        logger.info("Style selected: %s", style)  # Log the style selection

        st.text("")

        input_instructions = writer("input", language, script)
        large_number = st.checkbox(input_instructions)

        if large_number:
            numeric = False
            max_value = int(2e17)
        else:
            numeric = True
            max_value = int(1e15)

    st.title(writer("title", language, script))
    logger.info("Main title rendered.")  # Log the main title rendering

    st.write(writer("subtitle", language, script))
    logger.info("Subtitle rendered.")  # Log the subtitle rendering

    st.write(f"###### {writer('helper', language, script)} ")

    query = base_input(language, script, max_value=max_value, numeric=numeric)
    logger.info("Input number received: %s", query)  # Log the query input

    button = st.button(writer("button", language, script))

    if button or st.session_state["flag"]:
        result = converter.get_word(query, script=script, style=style)
        st.write(f"```\n{result}\n```")
        logger.info("Button clicked. Result: %s", result)  # Log button click and result


if __name__ == "__main__":
    logger.info("Application started.")  # Log application start
    main()
