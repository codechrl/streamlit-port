import numpy as np
import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages

add_page_title()
show_pages(
    [
        Page("pages/home.py", "Home", "🏠"),
        Page("pages/sentiment.py", "Sentiment Analysis", ":bar_chart:"),
        Page("pages/gender.py", "Gender", ":male_sign:"),
        Page("pages/instagram.py", "Instagram", ":camera:"),
    ]
)
