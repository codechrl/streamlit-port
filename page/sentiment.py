import numpy as np
import streamlit as st

st.title("Sentiment Analysis")

tab1, tab2 = st.tabs(["📈 **Sentiment - English**", "🗃 **Sentiment - Indonesia**"])
data = np.random.randn(10, 1)
tab1.subheader("Sentiment Analysis on English")
text = st.text_input("**Input**", "@codechrl its just so bad...")
button_clicked = st.button("Submit")
if button_clicked:
    st.write("You entered:", text)

tab2.subheader("Sentiment Analysis on Indonesia")
tab2.write(data)
