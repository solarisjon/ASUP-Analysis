import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st
    
def graph_dataframe(df):
    """
    This function takes a DataFrame and generates a graph based on the data.
    It uses Plotly to create an interactive graph that can be displayed in a web browser.
    """
    # Convert the 'Time' column to datetime for accurate sorting
    df['Time'] = pd.to_datetime(df['Time'])

    # Sort the DataFrame by the 'Time' column
    df = df.sort_values('Time')

    # Check if the DataFrame is empty
    if df.empty:
        print("No data to display.")
        return

    
    
    # Create a scatter plot with port number as text label on each dot
    fig = px.scatter(
        df,
        x='Time',                # Use actual datetime for x-axis
        y='Count',               # Number of events
        color='Node',            # Color by node name
 #       text='Port',             # Show port number as label on each dot
        hover_data={
            'Node': True,
            'Port': True,
            'Date': True,
            'Time': True,
            'Count': True,
            'Message': True
        }
    )

    # Update layout for better readability
    fig.update_layout(
        title="Port Flapping Events (link down events)",
        xaxis_title="Date",
        yaxis_title="Count",
        legend_title="Node",
        template="plotly_white",
        extendsunburstcolors=True
        
    )

    

    # Show the figure
    #fig.show()
    st.plotly_chart(fig, use_container_width=True)