import streamlit as st
st.title("my name is sirisha")

st.text("my hub kalyan")
st.text("my kid ratnika")
import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randn(2, 2),
    columns=(("my hub","kalyan"),("my kid","ratnika")))

st.table(df)
