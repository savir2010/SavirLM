import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import chabot_backend

if "word_problem" not in st.session_state:
    st.session_state.word_problem = ''
word_problem = st.session_state['word_problem']
st.markdown(f'## {word_problem}') 

if st.button("Change Problem"):
    st.session_state.messages = []
    switch_page('Enter Word Problem')

if "messages" not in st.session_state:
    st.session_state.messages = []





if st.session_state.word_problem != '':
    with st.chat_message("assistant"):
        response = chabot_backend.respond(word_problem,"",5)
        st.markdown(response)
else:
    with st.chat_message("assistant"):
        response = "How is your day"
        st.markdown(response)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter Text"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    sentiment = chabot_backend.get_sentiment(prompt)
    response = chabot_backend.respond(word_problem,context=prompt,sentiment=sentiment)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})




