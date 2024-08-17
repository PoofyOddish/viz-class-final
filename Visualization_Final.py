import streamlit as st
import pandas as pd
import numpy as np

# import viz_utility as vutil
import altair as alt

st.set_page_config(
    page_title="Final Viz Project",
    page_icon="🧑‍🤝‍🧑",
)

st.title("An analysis COVID-19's Impact on Domestic vs. Foreign Box Office Performance from 2000-2024")

st.markdown(
    """
    Howdy there 🤠  
    Welcome to my final project for Fundamentals of Data Visualization  *(fueled by [Streamlit](https://streamlit.io))*   

    ### 👈 Click on the links to the left to navigate through different analysis views
    Worldwide Analysis: Analysis of COVID-19's impact on worldwide box office performance
    Domestic vs. Foreign Analysis: Analysis of COVID-19's impact on domestic vs. foreign box office performance

   ### Overview of data used:
    This project uses data related to the top 200 performing Box Office movies for years 2000-2024. This data was retrieved from [Kaggle](https://www.kaggle.com/datasets/parthdande/movies-box-office-collection-data-2000-2024) in August 2024. Data was stored in three separate CSV files, and when combined together contains 8 columns and 5,000 rows. Columns are as follows:

    *   Rank of movie within year
    *   Name of movie
    *   Worldwide profit
    *   Domestic profit
    *   Foreign profit
    *   Percent of profit from domestic audiences
    *   Percent of profit from foreign audiences
    *   Year of movie release

    ### Goals for this project:
    The primary goal for this project will be to evaluate the potential impact on COVID-19 to box office sales through exploratory analysis. The key question I am to answer is to determine if there has been a measurable change box office performance in movies released pre-, during, and post-COVID-19 pandemic.

    ### Tasks for this project:
    The tasks for this project will include the following:
    *   A film studio is looking to release a new movie and wants to understand how much they should spend on marketing efforts for domestic vs. foreign audiences following COVID-19 pandemic
    *   Explore data to analyze correlation between domestic and foreign box office performance as it relates to COVID-19 pandemic
    *   Interact with visualizations to explore specific data elements that might fall outside of existing correlation

    ### Summary and justification of key elements of design:
    For this project, I primarily leveraged scatterplots, barcharts, and boxplots using discrete colors to break the dataset into discrete time periods of analysis.
    This was an effective strategy to visually highlight trends in the data in a quick and accessible way.

    ### Discussion of final evaluation approach:
    To evaluate this project, I recruited members of my family for a user research session. I gave a high level overview of the data that was included and how to interact with the visualizations, and from there I asked questions of them to understand how they would interact with the visualizations.
    
    #### Target question asked
    Did COVID-19 have an impact on box office performance?

    #### People recruited
    Members of my family who are familiar with COVID-19 and have seen at least one movie at a theater.

    #### Measures used to answer
    This primarily used insight depth to see at what level a user could both identify the potential impact of COVID-19 and justify it using data visualizations.

    #### Approach used to answer question
    This was primarily a thinkaloud session where I asked users to navigate visualizations and explain how they were interacting with it.

    #### How methods were instantiated
    Methods were instantiated through discussions with participants.

    #### Criteria used to indicate visualization was successful
    If a user was able to provide a level of depth above just answering the target question, the visualization was considered successful.

    ### Synthesis of findings
    Overall, I found the visualizations I compiled were effective as 3 of 3 test users were able to answer the target question.

    An area of improvement for me is that users were consistently confused on how to interpret the boxplot charts, so I would likely swap that out with a different chart type in the future that tells a more intuitive story.

"""
)
