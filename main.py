import numpy as np
import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages

add_page_title()
show_pages(
    [
        Page("page/home.py", "Home", "🏠"),
        Page("page/sentiment.py", "Sentiment Analysis", ":bar_chart:"),
        Page("page/gender.py", "Gender", ":male_sign:"),
        Page("page/instagram.py", "Instagram", ":camera:"),
    ]
)
