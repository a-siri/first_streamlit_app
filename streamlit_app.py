import streamlit as st
st.title("my name is sirisha")

st.text("my hub kalyan")
st.text("my kid ratnika")
import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randn(2, 2),
    columns=('col %d' % i for i in range(2)))

st.table(df)
