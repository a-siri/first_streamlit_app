import streamlit as st
st.title('my parents healthy dinner')
st.header('Breakfast Favorites')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🥚 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avacado toast')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas 
my_family=pandas.dataframe("row_id,relation,name")
st.dataframe(my_family)
