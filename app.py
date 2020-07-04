# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 10:06:51 2020

@author: aakash
"""

import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('911_data_processed.csv')

st.title('911 Portfolio Analysis')

d = df.groupby(['month', 'specific_reason'])['specific_reason'].count().unstack()
side_choice = st.sidebar.selectbox('Analysis', options=['Tables', 'Plotting', 'About Author'])

if side_choice=='Tables':
    html_df = """
            <div style="background-color:tomato">
            <h2 style="color:white;text-align:center;padding:5px"> Dataframe </h2>
            </div>
            """
    st.markdown(html_df, unsafe_allow_html=True)
    rows = st.slider('show rows? ', min_value=2, max_value=df.shape[0])
    if rows:
        st.dataframe(df[:rows])
        if st.button('data description'):
                st.info('Police Emergency and Non-Emergency calls to 911 from Montgomery County Pennsylvania.')
    if st.checkbox('describe'):
        html_desc = """
            <div style="background-color:tomato">
            <h2 style="color:white;text-align:center;padding:5px"> Dataframe describe  </h2>
            </div>
            """
        st.markdown(html_desc, unsafe_allow_html=True)
        st.dataframe(df.describe())
    if st.checkbox('info'):
        html_info = """
            <div style="background-color:tomato">
            <h2 style="color:white;text-align:center;padding:5px"> Dataframe info  </h2>
            </div>
            """
        st.markdown(html_info, unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({'Column': df.columns,'Dtype': df.dtypes.values}))
    if st.checkbox('show tables'):
        html_month = """
            <div style="background-color:tomato">
            <h2 style="color:white;text-align:center;padding:5px"> Main Reason count </h2>
            </div>
            """
        st.markdown(html_month, unsafe_allow_html=True)
        st.table(df.groupby('specific_reason')['month'].count())
        html_month_count = """
            <div style="background-color:tomato">
            <h2 style="color:white;text-align:center;padding:5px"> Main Reason count month wise </h2>
            </div>
            """
        st.markdown(html_month_count, unsafe_allow_html=True)
        st.table(d)
if side_choice=='Plotting':
    html_bar = """
            <div style="background-color:tomato">
            <h2 style="color:white;text-align:center;padding:5px"> Countplot-- Month wise Reason count </h2>
            </div>
            """
    st.markdown(html_bar, unsafe_allow_html=True)
    fig = px.bar(d, x=d.index.values, y=['EMS', 'Fire', 'Traffic'], barmode='group',
             height=400 ,labels={'x':'month', 'value':'count', 'variable': 'reason'}, 
            )
    fig.update_xaxes(dict( tickmode = 'array', tickvals = d.index.values,))
    st.plotly_chart(fig)
    if st.checkbox('See map'):
        html_map = """
            <div style="background-color:tomato">
            <h2 style="color:white;text-align:center;padding:5px"> Region wise emergencies </h2>
            </div>
            """
        st.markdown(html_map, unsafe_allow_html=True)
        map_data = pd.DataFrame(df[['lat','lng']].values, 
                            columns=['lat','lon'])
        st.map(map_data)

if side_choice=='About Author':
     html_about = """
            <div style="background-color:tomato">
            <h2 style="color:white;text-align:center;padding:5px"> About me </h2>
            </div>
            """
     st.markdown(html_about, unsafe_allow_html=True)
     about = """Aakash Singh Rawat created this mini app as a first streamlit webapp.I'm a NLP, 
         DL enthusiast and there may be more webapp for live prediction.
         Unitil then follow me on below platforms and also check github profile where I've uploaded many notebooks related to NLP, DL and ML."""
     st.info(about)
     git_url = 'https://github.com/akrawat912/'
     link_url = 'https://www.linkedin.com/in/aakash-singh-966746154/'
     if st.button('Github'):
         st.success(git_url)
     if st.button('LinkedIn'):
         st.success(link_url)
           
        