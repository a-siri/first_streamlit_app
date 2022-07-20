import streamlit as st
st.title("my name is sirisha")

st.text("my hub kalyan")
st.text("my kid ratnika")
import pandas as pd

df = pd.DataFrame(
    
    columns=((1,"my hub","kalyan"),(2,"my kid","ratnika")))

st.table(df)
