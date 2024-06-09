import streamlit as st
from streamlit_extras.switch_page_button import switch_page

col1, col2 = st.columns(2)

st.image('logo.png', caption='')
             
st.title('Welcome to SavirLM! The Most Student Friendly Language Model.')
st.markdown(''' Now I know you all must be thinking, "this is just another ChatGPT or Khanmigo." You would be wrong to assume that.
            One thing I have noticed is kids struggle with their mental health. So I have incoporated Sentimental Analysis into my Language Model. The SavirLM is created 
            using Sentimental Analysis to deeply process what the user is saying. Many other models such as ChatGPT, Khanmigo and Gemeni are just acting like robots (which they are of course).
            However for a user to actually understand the concept we would like to put feelings and emotions in the model.''')
st.markdown("## Look no further SavirLM Got Your Back!")


if st.button("Want a report on your essay?"):
    switch_page('SavirLM Essay Report')

if st.button("Having Trouble Solving a Word Problem?"):
    switch_page('Enter Word Problem')

