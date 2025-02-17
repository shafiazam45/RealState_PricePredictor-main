import streamlit as st 
import pickle
import pandas as pd 
import numpy as np 

st.set_page_config(page_title="Plotting Demo")

with open("df.pkl","rb") as file:
    df = pickle.load(file)

with open("pipeline.pkl","rb") as file:
    pipeline = pickle.load(file)

# st.dataframe(df)


st.header("Enter your inputs")

#property_type
property_type = st.selectbox("Property Type",["flat","house"])

#sectors
sector = st.selectbox("sector",sorted(df["sector"].unique().tolist()))

#bedrooms
bedroom = float(st.selectbox("bedRoom",sorted(df["bedRoom"].unique().tolist())))

#bathrooms
bathroom = float(st.selectbox("bathroom",sorted(df["bathroom"].unique().tolist())))

#balcony
balcony = st.selectbox("Balconies",sorted(df["balcony"].unique().tolist()))

#property age
Property_age = st.selectbox("Property Age",sorted(df["agePossession"].unique().tolist()))

#built up area
built_up_area = float(st.number_input("Built up Area"))

#servant room
servant_room = float(st.selectbox("Servant Room",sorted(df["servant room"].unique().tolist())))

#store room
store_room = float(st.selectbox("store Room",sorted(df["store room"].unique().tolist())))

#furnishing type
furnishing_type = st.selectbox("furnishing type",sorted(df["furnishing_type"].unique().tolist()))

#luxury category
luxury_category = st.selectbox("Luxury Category",sorted(df["luxury_category"].unique().tolist()))

#floor category
floor_category = st.selectbox("Floor Category",sorted(df["floor_category"].unique().tolist()))


if st.button("predict"):

    # 1. form a dataset

    data = [[property_type,sector,bedroom,bathroom,balcony,Property_age,built_up_area,servant_room,store_room,furnishing_type,luxury_category,floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
        'agePossession', 'built_up_area', 'servant room', 'store room',
        'furnishing_type', 'luxury_category', 'floor_category']
    
    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    st.dataframe(one_df)


    # 2. predict
    base_price = np.expm1(pipeline.predict(one_df)[0])
    low = base_price - 0.22
    high = base_price + 0.22

    # 2. display
    st.text("The Price is between {} Cr and {} Cr".format(round(low,2),round(high,2)))

