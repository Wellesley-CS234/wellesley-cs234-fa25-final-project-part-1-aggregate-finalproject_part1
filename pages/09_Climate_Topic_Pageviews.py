import os
import streamlit as st
import pandas as pd

st.set_page_config(page_title="2023 to Present Day Climate Change Article Pageviews", layout="wide")
st.title("2023 to Present Day Climate Change Article Pageviews")


st.markdown('By Amanda Cheng')
st.markdown('This page provides a time-series view of the Climate Change Related wikipedia pages viewed from 2023-2025/10/7.')
st.markdown("Research Question: How have people's engagement and interest in Wikipedia Climate Change Topics evolved in the past 3 years?")

if 'student_data' not in st.session_state:
    st.session_state['student_data'] = {}

if 'st09_df' not in st.session_state['student_data']:
    df = pd.read_csv("data/st09_data.csv")
    st.session_state['student_data']['st09_df'] = df

if 'student_data' not in st.session_state:
    st.warning("Please ensure the main Home Page ran successfully and the data files exist.")
elif st.session_state['student_data']['st09_df'].empty:
  st.warning("nope")
else:
  data = pd.read_csv("data/st09_data.csv")
  data['year'] = data['year'].astype(str)

  choice = st.selectbox(
      'Select years', ['All','2023','2024', '2025']
  )
  if choice == 'All':
    st.write(f'Full data:')
    chart_data = data
  else:
    chart_data = data[data['year']==choice]
    st.write(f'Data for year {choice}')


  #st.write(chart_data.head())
  st.line_chart(data=chart_data, x='month-day', y='z_score', color='year', x_label = 'Time', y_label='Z_Score')

  # st.line_chart(data=chart_data, x='month-day', y='z_score', color='year', x_label = 'Time', y_label='Z_score\nCC Pageviews')


  combined_data = data.sort_values('pageview', ascending=False)

  st.header('Top Ten Pageview Days')
  st.dataframe(combined_data.head(10)[['date', 'pageview']])

  st.header('View All Raw Data')
  st.dataframe(data)
