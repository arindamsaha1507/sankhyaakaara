"""The app module."""

import streamlit as st
import yaml
from sankhyaakaara.converter import Converter, Style
from sankhyaakaara.languages import LANGUAGES

# Initialize logger


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

    script = st.sidebar.selectbox(
        "Select Script (लिपिं चिनु)", options=LANGUAGES, index=13
    )

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

        st.text("")

        input_instructions = writer("input", language, script)
        large_number = st.checkbox(input_instructions)

        if large_number:
            numeric = False
            max_value = int(2e17)
        else:
            numeric = True
            max_value = int(1e15)

    # Header section with title and links side by side
    header_col1, header_col2 = st.columns([4, 1])

    with header_col1:
        st.title(writer("title", language, script))
        st.write(writer("subtitle", language, script))

    with header_col2:
        st.markdown(
            "<div style='margin-top: 20px;'></div>", unsafe_allow_html=True
        )  # Add some top margin

        st.markdown(
            f"""
            <div style="text-align: right;">
                <a href="https://github.com/arindamsaha1507" target="_blank" style="text-decoration: none; display: block; margin-bottom: 8px;">
                    <span style="font-size: 16px;">👨‍💻</span>
                    <span style="color: #0366d6; font-weight: 500; margin-left: 5px;">{writer('credits', language, script)}</span>
                </a>
                <a href="https://github.com/arindamsaha1507/sankhyaakaara" target="_blank" style="text-decoration: none; display: block; margin-bottom: 8px;">
                    <span style="font-size: 16px;">⭐</span>
                    <span style="color: #0366d6; font-weight: 500; margin-left: 5px;">{writer('github_link', language, script)}</span>
                </a>
                <a href="https://t.me/sankhyaabot" target="_blank" style="text-decoration: none; display: block; margin-bottom: 12px;">
                    <span style="font-size: 16px;">🤖</span>
                    <span style="color: #0366d6; font-weight: 500; margin-left: 5px;">{writer('bot_link', language, script)}</span>
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")  # Horizontal divider

    st.write(f"###### {writer('helper', language, script)} ")

    query = base_input(language, script, max_value=max_value, numeric=numeric)

    button = st.button(writer("button", language, script))

    if button or st.session_state["flag"]:
        result = converter.get_word(query, script=script, style=style)
        st.write(f"```\n{result}\n```")


if __name__ == "__main__":
    main()
