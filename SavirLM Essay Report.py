import streamlit as st
from savir_essay_llm import generate_report
st.set_option('deprecation.showfileUploaderEncoding', False)


def generate_essay(essay_title, essay_content):
    st.title(essay_title)
    st.write(essay_content)


def main():
    st.title("Essay Grader")

    essay_title = st.text_input("Enter the title of the essay:")
    essay = st.text_area("Write your essay here:", height=300)


    if st.button("Generate Essay"):
        # Assuming you have a function to generate the essay content based on the input titles
        essay_content = generate_report(essay_title, essay)
        generate_essay(essay_title, essay_content)

if __name__ == "__main__":
    main()
