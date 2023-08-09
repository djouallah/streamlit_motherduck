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
@st.cache_resource(ttl=5*60)
def define_connection():
    con = duckdb.connect(f'''md:?token={st.secrets["md_token"]}''',read_only=True)
    return con
con=define_connection()
###############################
st.write('try SHOW DATABASES and SHOW TABLES' )
SQL = st.text_input('Write a SQL Query', '''use tpch100 ; SELECT   l_returnflag,   l_linestatus,
SUM(l_quantity) AS sum_qty,   count(*) as nbr_rows FROM   lineitem WHERE   l_shipdate <= '1998-09-02'  GROUP BY all''')
try :
  start = timer()
  df = con.execute(SQL).df() 
  end = timer()
  st.write("Duration in Second")
  st.write(round(end - start,2))
  st.write(df)
except Exception as er:
 st.write(df = pd.DataFrame([{'error':er}]))
