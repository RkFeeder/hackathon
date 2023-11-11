import streamlit as st
from PIL import Image

image = Image.open(r'C:\Users\randy_dywt\Downloads\Python\hackathon\pages\Webtoon.png')

st.image(image, caption = '졸업 요건 웹툰')
