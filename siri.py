import streamlit as st
st.title("my name is sirisha")

st.text("my hub kalyan")
st.text("my kid ratnika")
import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randn(2, 2),
    columns=((1,"my hub","kalyan"),(2,"my kid","ratnika")))

st.table(df)
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=("col %d" % i for i in range(5)))

# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

# Display a static table
st.table(df)

# CSS to inject contained in a string
hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

# Display an interactive table
st.dataframe(df)


