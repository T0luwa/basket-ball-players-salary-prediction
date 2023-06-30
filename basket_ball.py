import streamlit as st
import sklearn
import pickle
import pandas as pd
import numpy as np
from PIL import Image

basket_ball = pickle.load(open('/Users/test/Downloads/linearmodel.sav', 'rb'))

st.title('Basket ball salary prediction app')

st.sidebar.header('Player Data')

def user_report():
  position = st.sidebar.slider('Position', 0, 10, 1)
  rating = st.sidebar.slider('Rating', 50,100, 1 )
  team = st.sidebar.slider('Team', 0,30, 1 )
  country = st.sidebar.slider('Country', 0,3, 1 )
  draft_year = st.sidebar.slider('Draft Year', 2000,2020, 2000)
  draft_round = st.sidebar.slider('Draft Round', 1,10, 1)
  draft_peak = st.sidebar.slider('Draft Peak', 1,30, 1)

  user_report_data = {
      'position': position,
      'rating':rating,
      'team':team,
      'country':country,
      'draft_year':draft_year,
      'draft_round':draft_round,
      'draft_peak':draft_peak
  }
  report_data = pd.DataFrame(user_report_data, index=[0])
  return report_data

user_data = user_report()
st.header('Player Data')
st.write(user_data)

salary = basket_ball.predict(user_data)
st.subheader('Player Salary')
st.subheader('$'+str(np.round(salary[0], 2)))


