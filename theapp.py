# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 21:46:17 2023

@author: DAMMY
"""

import pandas as pd
import streamlit as st
import plotly.express as px 
from PIL import Image

st.set_page_config(page_title='Survey Results')
st.header('Survey Results 2021')
st.subheader('I hope this webapp will be helpful')

### ---Let us load Dataframe

excel_file = 'Survey_Results'
sheet_name = 'DATA'
upload=st.file_uploader('Upload your Dataset(In excel format)')
if upload is not None:
    df=pd.read_excel(upload)

if st.checkbox('preview Dataset'):
    if st.button('Head'):
        st.write(df.head())
    if st.button('Tail'):
        st.write(df.tail())
