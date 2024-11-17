import streamlit as st
import plotly.express as px
import pandas as pd

# Title of the app
st.title('World Map Viewer of Potential Conflict Zones')

# File uploader to allow users to upload a CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Check if the uploaded file has the necessary columns
    required_columns = ['Country', 'Civilian Danger', 'Doctor Danger']
    if all(col in df.columns for col in required_columns):
        # Dropdown menu for selecting the column to visualize
        column_name = st.selectbox(
            'Select a column to visualize:',
            ['civilian_danger', 'doctor_danger'],
            index=0  # Default to civilian_danger
        )

        # Create a choropleth map based on the selected column
        fig = px.choropleth(df, locations='country', locationmode='country names',
                            color=column_name,
                            color_continuous_scale='Reds',
                            range_color=[1, 10],  # Fix the color scale range
                            labels={column_name: column_name.replace("_", " ").title()},
                            title=f'World {column_name.replace("_", " ").title()}')

        # Update map appearance
        fig.update_geos(
            showcoastlines=True,
            coastlinecolor="Black",
            projection_type="natural earth"
        )

        # Customize color bar and legend
        fig.update_layout(
            coloraxis_colorbar=dict(
                title=column_name.replace("_", " ").title(),
                tickvals=[1, 3, 5, 7, 9],
                ticktext=['Low', 'Medium', 'High', 'Very High', 'Extreme']
            ),
            font=dict(family="Roboto, sans-serif", size=14)  # Apply Roboto font to all text
        )

        # Display the choropleth map
        st.plotly_chart(fig)

    else:
        st.error(f"The uploaded CSV must contain the following columns: {', '.join(required_columns)}")

else:
    st.info("Please upload a CSV file with 'Country', 'Civilian Danger', and 'Doctor Danger' columns.")

