# index.py
import streamlit as st

# Sidebar for navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Select a page:', ('csv_input', 'historical'))

if page == 'csv_input':
    st.write('You are on the Home page!')
    st.write('This is where you can upload your CSV and view the map for the World Conflict Zones.')

    # Import and run the csv_input page's main function
    from csv_input import main as csv_input_main
    csv_input_main()  # This will call the main function from csv_input.py

elif page == 'historical':
    st.write('You are on the Historical Data page!')
    st.write('This page allows you to upload and view historical conflict data.')

    # Import and run the historical page's main function
    from historical import main as historical_main
    historical_main()  # This will call the main function from historical.py
