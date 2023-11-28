"""The app module."""

import streamlit as st
import yaml

from converter import Converter, Style
from languages import LANGUAGES


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

    query = st.number_input(
        settings["instruction"][language],
        value=1,
        min_value=0,
        max_value=int(1e15),
        step=1,
    )

    button = st.button(settings["button"][language])

    if button:
        st.write(f"### {converter.get_word(query, script=script, style=style)}")


if __name__ == "__main__":
    main()
