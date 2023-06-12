import time

import numpy as np
import streamlit as st

st.title("Sentiment Analysis")
st.write("---")

text = st.sidebar.text_input("**Username**", "@codechrl its just so bad...")
button_clicked = st.sidebar.button("Analyze")

data = np.random.randn(10, 1)

st.subheader("Sentiment Analysis on Twitter")
if button_clicked:
    with st.spinner("Getting latest tweets..."):
        time.sleep(5)
    with st.spinner("Analyzing tweets..."):
        time.sleep(5)

    st.write("You entered:", text)
