import streamlit as st
st.title("my name is sirisha")

st.text("my hub kalyan")
st.text("my kid ratnika")
import pandas as pd

df = pd.DataFrame(
    
    columns=(("my hub","kalyan"),("my kid","ratnika")))

st.table(df)
