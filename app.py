"""The app module."""

import streamlit as st

from converter import Converter


def main():
    """The main function."""

    st.title("Sanskrit numerical tool")

    st.write("This tool converts numbers to Sanskrit words.")

    query = st.text_input("Please enter a number")

    if st.button("Convert"):
        query = query.strip().replace(",", "")

        if not query:
            st.error("Please enter a number.")
            return

        if query[0] == "-":
            st.error("Please enter a non-negative number.")
            return

        if not query.isnumeric():
            st.error("Please enter a valid number.")
            return

        if "." in query:
            st.error("Decimal points not allowed.")
            return

        try:
            query = int(query)
        except ValueError:
            st.error("Please enter a valid number.")
            return

        if query >= 1e17:
            st.error("Number too large. Enter a number upto 1e^17.")
            return

        converter = Converter()
        st.write(f"### {converter.get_word(query)}")


if __name__ == "__main__":
    main()
