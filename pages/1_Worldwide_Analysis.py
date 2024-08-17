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
### View below charts and analysis of worldwide box office performance
"""
)

# Create scatterplot
scatter = alt.Chart(data).mark_bar().encode(
    x='year:O',
    y='count(year)',
    color=alt.Color('WW_Gross:O', legend=alt.Legend(title='WW_Gross')).scale(scheme="set2"),
    tooltip=['year:O','count(year):Q']
    )

bar = alt.Chart(data).mark_line().encode(
    x='year:Q',
    y='count(year)',
    color=alt.Color('WW_Gross:O', legend=alt.Legend(title='WW_Gross')).scale(scheme="set2"),
    tooltip=['year:O','count(year):Q']
    )

covid = alt.Chart(pd.DataFrame({'year':['2019']})).mark_rule(color='red').encode(
    x='year:Q'
)

box = alt.Chart(data).mark_boxplot().encode(
    x='year:O',
    y='Worldwide:Q',
    color=alt.Color('Year_Group:O', legend=alt.Legend(title='Year_Group')).scale(scheme="set2"),
    )

with st.container():
    st.markdown(
    """
The below barchart displays the distribution of worldwide box office performance over time based on 
performance in the following ranges:
*   1mil-100mil  
*   100mil-500mil  
*   Greater than 500mil

From initial glance, it appears that there was a steep decrease in films that gross over 500 million around the start of COVID.
"""
    )
    st.altair_chart(scatter, use_container_width=True)

    st.markdown("""
    In viewing this same data as a line chart, it now become apparent that box office performance dipped in response to COVID-19 (indicated by line in red.)  
    
    Notably, there were fewer films grossing over 100mil as indicated by the decline in the green and blue lines and an increase in the orange line.            
                """)

    st.altair_chart(bar+covid, use_container_width=True)

    st.markdown(""" 
    While boxplots of this data have substantial noise, it is evident that even outlier activity has been pushed downward following the post-COVID-19 pandemic period, with fewer films reaching previous levels of success in the years following 2019.
""")

    st.altair_chart(box, use_container_width=True)