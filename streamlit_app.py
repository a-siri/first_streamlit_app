import streamlit as st
st.title('my parents healthy dinner')
st.header('Breakfast Favorites')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🥚 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avacado toast')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.set_index('Fruit')))

# Display the table on the page.
st.dataframe(my_fruit_list)
