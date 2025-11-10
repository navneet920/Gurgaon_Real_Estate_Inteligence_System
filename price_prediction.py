import streamlit as st
import pickle
import pandas as pd
import numpy as np

def run_prediction():
    #st.set_page_config(page_title="viz Demo")

    with open('model/df.pkl','rb') as df_file:
        df=pickle.load(df_file)

    with open('model/pipeline.pkl','rb') as pipe_file:
        pipeline=pickle.load(pipe_file)

    #st.dataframe(df)
    st.header('Enter your inputs')
    #property_type
    property_type=st.selectbox('property Type ',['flat','house'])

    #sector
    sector=st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

    #bedRoom
    bedrooms=float(st.selectbox('Number of Bedroom',df['bedRoom'].unique().tolist()))

    #bathroom
    bathrooms=float(st.selectbox('Number of Bathroom',df['bathroom'].unique().tolist()))
    #balcony
    balcony=st.selectbox('Balconies',df['balcony'].unique().tolist())
    #agewePossession
    property_age=st.selectbox('property_Age',df['agePossession'].unique().tolist())
    #built_up_area
    built_up_area=float(st.number_input('Built_up_Area'))
    #servant room
    servant_room=float(st.selectbox('Servant Room',[0.0,1.0]))
    #store room
    store_room=float(st.selectbox('Store Room',[0.0,1.0]))

    furnishing_type=st.selectbox('Furnishing Type',df['furnishing_type'].unique().tolist())
    luxury_category=st.selectbox('luxury_category',df['luxury_category'].unique().tolist())
    floor_category=st.selectbox('floor category',df['floor_category'].unique().tolist())

    if st.button('Predict'):
        #form a dataframe
        data = [[property_type, sector, bedrooms, bathrooms, balcony, property_age,
                 built_up_area, servant_room, store_room, furnishing_type, luxury_category,
                 floor_category]]
        columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
                   'agePossession', 'built_up_area', 'servant room', 'store room',
                   'furnishing_type', 'luxury_category', 'floor_category']

        # convert to DataFrame
        one_df = pd.DataFrame(data, columns=columns)
        # st.dataframe(one_df)
        #predict
        base_price=np.expm1(pipeline.predict(one_df))[0]
        low=base_price-0.22
        high=base_price +0.22

        #display
        st.text("The price of the flat is between {} Cr and {} Cr".format(round(low,2),round(high,2)))