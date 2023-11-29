"""The app module."""

import streamlit as st
import yaml

from converter import Converter, Style
from languages import LANGUAGES


def base_input(
    settings: dict, language: str, max_value: int, numeric: bool = True
) -> int:
    """Returns a numeric input widget."""

    if numeric:
        return int(
            st.number_input(
                settings["instruction"][language],
                value=1,
                min_value=0,
                max_value=max_value,
                step=1,
            )
        )

    query = st.text_input(settings["instruction"][language])

    if query != "":
        try:
            ret = int(query)

            if ret < 0 or ret > max_value:
                st.error(f"{settings['range'][language]} 0 - {max_value}.")
                return 0

            return ret

        except ValueError:
            st.error(settings["error"][language])
            return 0

    return 0


def main():
    """The main function."""

    converter = Converter()

    with open("ui_text.yml", "r", encoding="utf-8") as stream:
        settings = yaml.load(stream, Loader=yaml.FullLoader)

    language = "English"

    language = st.sidebar.selectbox(
        "Select Language (भाषां चिनोतु)", list(settings["title"].keys())
    )

    st.title(settings["title"][language])

    st.write(settings["subtitle"][language])

    st.write(f"###### {settings['helper'][language]} ")

    st.sidebar.title(settings["options"][language])

    with st.sidebar:
        st.write(f"### {settings['script'][language]}")
        script = st.selectbox(
            settings["script_options"][language], options=LANGUAGES, index=13
        )

        st.write(f"### {settings['joiner'][language]}")
        joiner = st.selectbox(
            settings["joiner_options"][language], options=["अधिक", "उत्तर"], index=0
        )
        style = Style.ADHIKA if joiner == "अधिक" else Style.UTTARA

        st.text("")

        input_instructions = settings["input"][language]
        large_number = st.checkbox(input_instructions)

        if large_number:
            numeric = False
            max_value = int(2e17)
        else:
            numeric = True
            max_value = int(1e15)

    query = base_input(settings, language, max_value=max_value, numeric=numeric)

    button = st.button(settings["button"][language])

    if button:
        st.write(f"### {converter.get_word(query, script=script, style=style)}")


if __name__ == "__main__":
    main()
