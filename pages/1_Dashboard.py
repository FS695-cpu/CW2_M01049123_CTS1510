import streamlit as st 
import pandas as pd 
from app.cyber_incidents import get_all_cyber_incidents, migrating_cyber_incidents
from app.db import get_connection

st.set_page_config(
    page_title= 'Home',
    page_icon='',
    layout='wide' 
)
if 'logged_in' not in st.session_state: 
    st.session_state['logged_in'] = False 
    
if not st.session_state['logged_in']: 
    st.warning('Please log in to access Dashboard.')
    st.stop()
else:
    st.success('you are logged in!')

conn = get_connection()
data = get_all_cyber_incidents(conn)



st.title('Cyber Incidents Dashboard') 

st.markdown("""
### Dashboard Overview
This is a  dashboard that provides an interactive view of cyber incidents data.  
You can filter incidents by severity level using the sidebar, explore category distributions, and have a look at the  trends over time.  
The goal is to make complex incident data easier to access, read, understand and analyze.
""")


with st.sidebar:
    st.header('Naavigation')
    severity_choice= st.selectbox('Severity Level', data['severity'].unique())

filtered_data = data[data['severity']== severity_choice]
data['timestamp'] = pd.to_datetime(data['timestamp'])

col1, col2 = st.columns(2)

with col1: 
    st.subheader(f'Cyber Incidents with Severity:{severity_choice}')
    st.bar_chart(filtered_data['category'].value_counts())
    st.markdown(f"""
    **Summary:**  
    - Most frequent categories appear clearly for severity *{severity_choice}*.  
    - The distribution highlights which incident types dominate.  
    - Useful for prioritizing response strategies.
    """)


with col2: 
    st.subheader('Category Trend Over Time')
    st.line_chart(filtered_data, x = 'timestamp', y = 'category')
    st.markdown(f"""
    **Summary:**  
    - Trends show how categories evolve across time.  
    - Severity *{severity_choice}* incidents cluster in certain periods.  
    - Helps identify spikes and recurring patterns.
    """)


st.subheader('Filtered data')
st.dataframe(filtered_data) 

st.markdown("""
### Conclusion: 
From the filtered data, you can see how incident categories vary across severity levels and how they evolve over time.  
This helps identify which types of incidents are most frequent and when they occur, this allows better risk management and decision-making.  
Overall, this dashboard provides a clear and interactive way to monitor cyber incident trends and understand it.
""")