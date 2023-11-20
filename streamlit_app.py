"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd

st.set_page_config(
   page_title="Area 51",
   page_icon="👽",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.ballons()

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

st.session_state

