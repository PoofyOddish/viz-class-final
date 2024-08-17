import streamlit as st
import pandas as pd
import numpy as np

# import viz_utility as vutil
import altair as alt

@st.cache_data
def load_data():
    # Step 1: Import data
    pd.set_option('display.float_format', lambda x: '%.3f' % x)
    data1 = pd.read_csv('./data/2024 Movies Box Ofice Collection.csv', thousands=',')
    data2 = pd.read_csv('./data/2000-2009 Movies Box Ofice Collection.csv', thousands=',')
    data3 = pd.read_csv('./data/2010-2024 Movies Box Ofice Collection.csv', thousands=',')

    # Step 2a: Concat files into a single dataframe and clean up data types

    df = pd.concat([data1, data2, data3])
    df['Domestic'] = df['Domestic'].astype('float')
    df['Foreign'] = df['Foreign'].astype('float')
    df['Domestic_percent'] = df['Domestic']/df['Worldwide']*100
    df['Foreign_percent'] = df['Foreign']/df['Worldwide']*100
    df['Worldwide'] = df['Worldwide'].astype('float')
    df['year'] = df['year'].astype('category')

    # Step 2b: Create a new variable that buckets years
    df['Year_Group'] = pd.cut(df['year'], bins=[1999, 2019, 2022, 2024], labels=['Pre-COVID', 'Mid-COVID', 'Post-COVID'])

    # Step 2c: Create a new variable that buckets worldwide earnings
    df['WW_Gross'] = pd.cut(df['Worldwide'], bins=[0, 1000000, 100000000, 500000000,10000000000], labels=['<1mil', '1mil-100mil', '100mil-500mil','>500mil'])

    data = df

    return data

data = load_data()

st.markdown(
"""
### View distribution of domestic vs. foreign box office performance
"""
)

scatter = alt.Chart(data).mark_point().encode(
    x='Domestic:Q',
    y='Foreign:Q',
    color=alt.Color('Year_Group:O', legend=alt.Legend(title='Year_Group')).scale(scheme="set2"),
    tooltip=['Release Group:N','year:O','Worldwide:Q','Domestic:Q','Foreign:Q'])

box_dom = alt.Chart(data).mark_boxplot().encode(
    x='Year_Group:O',
    y='Domestic:Q',
    color=alt.Color('Year_Group:O', legend=alt.Legend(title='Year_Group')).scale(scheme="set2"),
    ).properties(
        width=175
    )

box_for = alt.Chart(data).mark_boxplot().encode(
    x='Year_Group:O',
    y='Foreign:Q',
    color=alt.Color('Year_Group:O', legend=alt.Legend(title='Year_Group')).scale(scheme="set2"),
    ).properties(
        width=175
    )

with st.container():

    st.markdown(
    """
The below scatterplot displays the distribution of domestic vs. foreign box office performance over time based on 
a year as defined below:
*   Pre-COVID (2000-2019) 
*   Mid-COVID (2020-2022)
*   Post-COVID (2023-2024)

From this scatterplot, there are a few interesting elements that can be highlighted.
*  There is a positive relationship between domestic and foreign performance. Highly successful movies tend to be successful both domestically and internationally.
*  Foreign success does not guarantee domestic success - there is interesting behavior along the y-axis where movies are highly successful to international audiences, but not successful (or released) to domestic audiences.
*  Post-COVID movies have not increased back to even mid-COVID levels. This may be due in part to having incomplete annual data for 2024 OR there are still movies yet to be released this year that may be highly successful.
*  Avatar and Avengers: Endgame were far more successful movies than I ever realized
"""
    )

    st.altair_chart(scatter, use_container_width=True)

    st.markdown(
        """
    The below boxplots confirm that for both domestic and international performance, performance has not returned to pre-COVID levels.

    It is interesting to see that the scale for foreign performance is twice that of domestic, indiciating that one country (USA) makes up such a large market share for box office performance.
"""

    )

    st.altair_chart(box_dom|box_for, use_container_width=True)

    #st.altair_chart(box_for, use_container_width=True)