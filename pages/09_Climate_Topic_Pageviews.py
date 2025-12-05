import os
import streamlit as st
import pandas as pd


path = os.path.join("..", "data", "st09_data.csv")
data = pd.read_csv(path)
data['year'] = data['year'].astype(str)


st.set_page_config(layout="wide")

st.header('2023 to Present Day Climate Change Article Pageviews')


st.markdown('By Amanda Cheng')
st.markdown('This page provides a time-series view of the Climate Change Related wikipedia pages viewed from 2023-2025/10/7.')
st.markdown("Research Question: How have people's engagement and interest in Wikipedia Climate Change Topics evolved in the past 3 years?")


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

