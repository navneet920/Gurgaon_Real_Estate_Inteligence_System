import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

#st.set_page_config(page_title="Plotting Demo")
def Analysis():
    st.title("Analytics")
    new_df=pd.read_csv("datasets/data_vz1.xls")
    feature_text=pickle.load(open('model/feature_text.pkl','rb'))
    #st.dataframe(new_df)
    group_df = new_df.groupby('sector')[['price', 'price_per_sqft', 'built_up_area',
                                         'latitude', 'longitude']].mean()

    st.header("Sector price per sqft GeoMap")
    fig = px.scatter_map(group_df, lat="latitude", lon="longitude",color="price_per_sqft", size="built_up_area",
                      color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                        map_style="open-street-map"
                         ,hover_name=group_df.index,width=1200,height=700)
    st.plotly_chart(fig,use_container_width=True)
    plt.rcParams['font.family'] = 'Arial'

    st.header("Features WordCloud")
    selected_sector = st.selectbox("Choose Sector", sorted(new_df['sector'].unique()))
    wordcloud = WordCloud(
        width=800,
        height=800,
        background_color='white',
        stopwords=set(['s']),
        min_font_size=10
    ).generate(feature_text)

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

    st.header("Area Vs Price")
    property_options = new_df['property_type'].unique().tolist()
    property_options.insert(0, 'overall')  # Add "overall" at the top

    property_type = st.selectbox("Select Property Type", property_options)

    if property_type == 'overall':
        filtered_df = new_df
    else:
        filtered_df = new_df[new_df['property_type'] == property_type]
    fig = px.scatter(filtered_df,x='built_up_area',y='price',color='bedRoom',
        labels={
            'built_up_area': 'Built-up Area (sq ft)',
            'price': 'Price (in Cr)',
            'bedRoom': 'Bedrooms'
        },
        title=f"Scatter Plot of Area vs Price ({property_type.capitalize()})"
    )

    st.plotly_chart(fig, use_container_width=True)


    st.header("BHK Pie Chart")
    sector_option=new_df['sector'].unique().tolist()
    sector_option.insert(0,'overall')
    selected_sector=st.selectbox('Choose Sector',sector_option)
    if selected_sector == 'overall':
        fig2=px.pie(new_df,names='bedRoom')
        st.plotly_chart(fig2,use_comtainer_width=True)
    else:
        fig2 = px.pie(new_df[new_df['sector']== selected_sector], names='bedRoom')
        st.plotly_chart(fig2, use_comtainer_width=True)

    st.header("Side By Side BHK Price Comparison")
    fig3=px.box(new_df[new_df['bedRoom'] <= 4],x='bedRoom',y='price')
    st.plotly_chart(fig3, use_comtainer_width=True)

    st.header("Side by Side Distplot for Property Type")
    fig4=plt.figure(figsize=(10,4))
    sns.histplot(new_df[new_df['property_type'] == 'house']['price'], kde=True, label='House', color='blue', stat='density')
    sns.histplot(new_df[new_df['property_type'] == 'flat']['price'], kde=True, label="Flat", color='orange', stat='density')
    plt.legend()
    st.pyplot(fig4)
