"""The app module."""

import streamlit as st

from converter import Converter


def main():
    """The main function."""

    st.title("Sanskrit numerical tool")

    st.write("This tool converts numbers to Sanskrit words.")

    query = st.number_input(
        "Please enter a number",
        value=0,
        step=1,
        min_value=0,
    )

    if st.button("Convert"):
        converter = Converter()
        st.write(f"### {converter.get_word(query)}")


if __name__ == "__main__":
    main()
