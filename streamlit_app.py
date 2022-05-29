import streamlit as sl
import pandas as pd

sl.title('My Parents New Health Diner')

sl.header('Breakfast Favorities')
sl.text('🥣 Omega 3 & Blueberry Oatmeal')
sl.text('🥗 Kale Spinach & Rocket Smoothie')
sl.text('🐔 Hard-Boiled Free-Range Egg')
sl.text('🥑🍞 Avocado Toast')

sl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Pick up list
sl.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Advocado', 'Strawberries'])

# Showing the list
sl.dataframe(my_fruit_list)
