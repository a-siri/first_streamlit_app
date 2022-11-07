import streamlit as st
import snowflake.connector
import pandas
#st.title('my parents healthy dinner')
#st.header('Breakfast Favorites')
#st.text('🥣 Omega 3 & Blueberry Oatmeal')
#st.text('🥗 Kale, Spinach & Rocket Smoothie')
#st.text('🥚 Hard-Boiled Free-Range Egg')
#st.text('🥑🍞 Avacado toast')
#st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
#fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index))
#fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
#st.dataframe(fruits_to_show)
#st.header("Fruityvice Fruit Advice!")
#fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
#st.write('The user entered ', fruit_choice)
#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#st.text(fruityvice_response.json()) #just writes the data to the screen

# take the json version of the response & normalize it
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table
#st.dataframe(fruityvice_normalized)



#my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
#st.header("The fruit load list contains:")
#st.dataframe(my_data_rows)


#add_my_fruit = st.text_input('What fruit would you like to add?','jackfruit')
#st.write('Thanks for adding', add_my_fruit)

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),
CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)





