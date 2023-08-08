import streamlit as st
import duckdb
from timeit import default_timer as timer
st.set_page_config(
    page_title="Example of using Streamlit with MotherDuck",
    page_icon="✅",
    layout="wide",
                  )
col1, col2 = st.columns([3, 1])
################################
import duckdb
import pandas as pd
@st.cache_resource(ttl=5*60)
def get_data(SQL):
    con = duckdb.connect(f'''md:?token={st.secrets["md_token"]}''',read_only=True)
    try :
     df = con.sql(SQL).df()
    except Exception as er:
     df = pd.DataFrame([{'error':er}])    
    return df
###############################
SQL = st.text_input('Write a SQL Query', 'SHOW DATABASES')
start = timer()
df = get_data(SQL) 
end = timer()
st.write("Duration in Second")
st.write(round(end - start,2))
st.write(df)
