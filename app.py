import streamlit as st
import duckdb
from timeit import default_timer as timer
import pandas as pd
st.set_page_config(
    page_title="Example of using Streamlit with MotherDuck",
    page_icon="✅",
    layout="wide",
                  )
col1, col2 = st.columns([3, 1])
################################
con = duckdb.connect(f'''md:?token={st.secrets["md_token"]}''',read_only=True)
###############################
SQL = st.text_input('Write a SQL Query', 'SHOW DATABASES')
try :
  start = timer()
  df = con.execute(SQL).df() 
  end = timer()
  st.write("Duration in Second")
  st.write(round(end - start,2))
  st.write(df)
except Exception as er:
 st.write(df = pd.DataFrame([{'error':er}]))
con.close()
