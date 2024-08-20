import streamlit as st
import pandas as pd
import datetime
import pickle
import gzip
import time
from PIL import Image
from sklearn.preprocessing import (LabelEncoder,StandardScaler)
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

st.set_page_config(page_title='Singapore Resale Prediction',layout='wide',initial_sidebar_state='auto')

img = Image.open('RE_image.jpg')
st.image(img)

st.title('Singapore Resale Flats Price Prediction')
st.write('The resale flat market in Singapore is highly competitive, and it can be challenging to accurately estimate the resale value of a flat. There are many factors that can affect resale prices, such as location, flat type, floor area, and lease duration.<br>A predictive model can help to overcome these challenges by providing users with an estimated resale price based on these factors.',unsafe_allow_html=True)
st.write('This app helps you to predict the resale prices of flats in Singapore. based on historical data and also aims to assist both potential buyers and sellers in estimating the resale value of a flat.',unsafe_allow_html=True)
st.markdown(' ')
st.markdown(' ')
st.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size = "10">Check the price.. Make your decision wise..!!',unsafe_allow_html=True)
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

col1,col2,col3,col4,col5 = st.columns((0.2,0.2,1.2,0.2,0.2))
with col3:
    flatlist = ['1 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', '2 ROOM', 'EXECUTIVE', 'MULTI GENERATION', 'MULTI-GENERATION']
    flatlabellist = [0,2,3,4,1,5,6,7]
    flattype = st.selectbox('Flat Type',options=flatlist,index=None)
    if(flattype):
        for i in range(0,len(flatlist)):
            if(flatlist[i] == flattype):
                getflattype = flatlabellist[i]
    st.markdown(' ')

    getyear = st.slider('Selling Year',min_value=1990,max_value=2100)
    st.markdown(' ')
    
    storeylist = ['01 TO 03','01 TO 05','04 TO 06','06 TO 10','07 TO 09','10 TO 12','11 TO 15','13 TO 15','16 TO 18','16 TO 20']
    storeylabellist = [0,1,2,3,4,5,6,7,8,9]
    storeyrange = st.select_slider('Storey Range',options=storeylist)
    if(storeyrange):
        for i in range(0,len(storeylist)):
            if(storeylist[i] == storeyrange):
                getstorey = storeylabellist[i]
    st.markdown(' ')

    getfloorarea = st.number_input('Floor Area (sq.m)',min_value=0)
    st.markdown(' ')
    
    flatmodellist = ['IMPROVED', 'NEW GENERATION', 'MODEL A', 'STANDARD', 'SIMPLIFIED', 'MODEL A-MAISONETTE', 'APARTMENT', 'MAISONETTE', 'TERRACE', '2-ROOM', 'IMPROVED-MAISONETTE', 'MULTI GENERATION', 'PREMIUM APARTMENT', 'Improved', 'New Generation', 'Model A', 'Standard', 'Apartment', 'Simplified', 'Model A-Maisonette', 'Maisonette', 'Multi Generation', 'Adjoined flat', 'Premium Apartment', 'Terrace', 'Improved-Maisonette', 'Premium Maisonette', '2-room', 'Model A2', 'DBSS', 'Type S1', 'Type S2', 'Premium Apartment Loft']    
    flatmodellabellist = [ 7, 20, 12, 27, 26, 13,  3, 11, 30,  0,  8, 14, 22,  9, 21, 16, 29, 5, 28, 17, 15, 19,  4, 23, 31, 10, 25,  1, 18,  6, 32, 24,  2]
    flatmodel = st.selectbox('Flat Model',options=flatmodellist,index=None)
    if(flatmodel):
        for i in range(0,len(flatmodellist)):
            if(flatmodellist[i] == flatmodel):
                getflatmodel = flatmodellabellist[i]
    st.markdown(' ')

    getflatage = st.number_input('Flat Age (years)',min_value=1)
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')

    col6,col7 = st.columns((0.5,0.8),gap='small')
    with col6:
        searchimg = Image.open('search.jpg')
        st.image(searchimg,use_column_width=None)
    with col7:
        st.markdown('<br>',unsafe_allow_html=True)
        getpricebut = st.button('Check Price')
        if(getpricebut):
            with gzip.open('newmodel','rb') as f:                
                getmodel = pickle.load(f)
            inputpd = pd.DataFrame({'year':[int(getyear)], 'flat_type':[getflattype], 'storey_range':[getstorey], 'floor_area_sqm':[getfloorarea], 'flat_model':[getflatmodel], 'flat_age':[getflatage]})
            getout = int(getmodel.predict(inputpd))
            with st.spinner('Calculating'):
                time.sleep(5)
            st.markdown('<br>',unsafe_allow_html=True)
            concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><font size="10">:green[SGD $' + str(getout) + ']</b>'
            st.write('Estimated Resale Value : ',concatstr,unsafe_allow_html=True)
