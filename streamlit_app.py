import streamlit as st
#from streamlit_option_menu import option_menu
import subprocess
Trends=('Trend 1','Trend 2','Trend 2')   #variables(modifiable) for trend names
Trend_values=[0,0,0]                    #variables(modifiable) for trend values
countries= ["Global", "USA", "India", "Others"]                #variables(modifiable) for country names
paltforms_list=(["Twitter", "Facebook", "Instagram", "LinkedIn"])           #variables(modifiable) for platforms

# Set the page config to wide mode for better use of space

#funions


def for_each_platform(platformsnumber):
    
    for idx, platform in enumerate(platformsnumber):
     st.header(platform)
     navigate_to_posts(selected_trends)



    # Function to redirect to another Streamlit page
def navigate_to_posts(selected_trends):


    # Create columns dynamically based on the number of selected trends
    cols = st.columns(len(selected_trends))
    i=0

    # Iterate over each selected trend
    for trend, col in zip(selected_trends, cols):
        with col:
            st.header(trend)
            
   

 #page menue sections
#selected_menu=option_menu(menu_title=None,
            
 #                         options=["home","posts"],
  #                        icons=["house","Postcard heart"],
   ##                       menu_icon="cast",
       #                   default_index=0,
     ##                     orientation="horizontal",
                          
                          
        #                  )


    
st.set_page_config(layout="wide")

# Assuming the UI has a sidebar for filters
with st.sidebar:
    st.title("Filters")
    # Add filter options here
   # countries = ["Country 1", "Country 2", "Country 3"]  # Example countries list
    #platforms_list = ["Platform 1", "Platform 2", "Platform 3"]  # Example platforms list
    country = st.selectbox("Select Country/Region", countries)
    platforms = st.multiselect("Select Platforms", paltforms_list)
    b = st.button("Show trends")

# Main content area
st.title("Social Media Trends Dashboard")

# Split main content area into two sections
left_column, right_column = st.columns(2)

# Left column for round graphs
with left_column:
    st.header("Trend Visuals")
    # Example data for the pie chart
    # Example trend values
    chart_data = {Trends[0]: Trend_values[0], Trends[1]: Trend_values[1], Trends[2]: Trend_values[2]}
    # Create a pie chart using Streamlit's native chart function
    st.write("analytics")
    st.bar_chart(chart_data)

# Right column for content of posts
with right_column:
    st.header("Trend Posts")
    # Multiselect for filtering trends
    selected_trends = st.multiselect("Select Trends", Trends)
    # Display content related to selected trends
    # Placeholder for posts content
    button = st.button("Generate Posts")
    if button:
        for_each_platform(platforms)
    


