import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title("My Mom's New Healthy Diner")
streamlit.header('Breakfast Favourites')
streamlit.text('๐ฅฃ Omega 3 & Blueberry Oatmeal')
streamlit.text('๐ฅ Kale, Spinach & Rocket Smoothie')
streamlit.text('๐Hard-Boiled Free-Range Egg')
streamlit.text('๐ฅ๐Avocado Toast')
streamlit.header('๐๐ฅญ Build Your Own Fruit Smoothie ๐ฅ๐')



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Strawberries'])
streamlit.dataframe(my_fruit_list)

def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized
streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
   else:
      back_from_function=get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
      #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      #streamlit.dataframe(fruityvice_normalized)
except URLERROR as e:
  streamlit.error()
    
streamlit.write('The user entered ', fruit_choice)
add_my_fruit=streamlit.text_input('What fruit would you like information about?','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)
#streamlit.text(fruityvice_response.json())
#streamlit.stop()
streamlit.header("View Our Fruit List -Add Our Favourites!")
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")
         return my_cur.fetchall()
if streamlit.button('Get Fruit  List'):
   
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows=get_fruit_load_list()
   my_cnx.close()
   streamlit.dataframe(my_data_rows)
def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into fruit_load_list values('"+ new_fruit +"')")
         return "Thanks For Adding " + new_fruit

add_my_fruit=streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a  Fruit To the List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function=insert_row_snowflake(add_my_fruit)
   streamlit.text(back_from_function)
      
   
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")
