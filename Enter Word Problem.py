import chabot_backend
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
# Display chat messages from history on app rerun

# from streamlit_navigation_bar import st_navbar

# page = st_navbar(["Home", "Documentation", "Examples", "Community"])
st.markdown("## Enter A Word Problem")
word_problem = st.text_area("", height=150)
st.session_state.word_problem = ''
if st.button("Submit Problem"):

    st.session_state.word_problem = word_problem
    st.session_state.messages = []

    switch_page('SavirLM Helper')


# if st.button("Submit Problem"):
#     # Assuming you have a function to generate the essay content based on the input titles
#     with st.chat_message("assistant"):
#         response = word_problem
#         st.markdown(response)
#     st.session_state.messages.append({"role": "assistant", "content": response})

# if prompt := st.chat_input("Enter Text"):
#     # Display user message in chat message container
#     st.chat_message("user").markdown(prompt)
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})

#     response = f"Echo: {prompt}"
#     with st.chat_message("assistant"):
#         st.markdown(response)
#     st.session_state.messages.append({"role": "assistant", "content": response})


# # Initialize chat history
#     # if "messages" not in st.session_state:
#     #     st.session_state.messages = []




# # React to user input

