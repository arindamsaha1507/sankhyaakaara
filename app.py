"""The app module."""

import streamlit as st

from converter import Converter
from languages import LANGUAGES


def wide_button_style():
    st.markdown(
        """
        <style>
        .wide-button {
            display: block;
            width: 100%;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )


def main():
    """The main function."""

    st.title("Sanskrit numerical tool")

    st.write("This tool converts numbers to Sanskrit words.")

    cols = st.columns(2)

    with cols[0]:
        query = st.number_input(
            "Enter a number", value=1, min_value=0, max_value=int(1e15), step=1
        )

    with cols[1]:
        script = st.selectbox("Select script", options=LANGUAGES, index=13)

    cols = st.columns(5)

    with cols[2]:
        button = st.button("Convert")

    if button:
        converter = Converter()
        print(script)
        print(converter.get_word(query, script=script))
        st.write(f"### {converter.get_word(query, script=script)}")


if __name__ == "__main__":
    main()
