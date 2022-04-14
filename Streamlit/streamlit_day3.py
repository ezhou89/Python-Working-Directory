#import the streamlit library
import streamlit as st

#create the header for the app
st.header('st.button')


#conditional statement for printing alternative messages
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')