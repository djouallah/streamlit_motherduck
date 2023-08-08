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
#make sure you don't include http into the endpoint
@st.experimental_singleton
def define_view():
    import duckdb
    con = duckdb.connect(f"md:?token={st.secrets["md_token"]}",read_only=True)
    return con
con=define_view()
###############################
SQL = st.text_input('Write a SQL Query', 'SHOW DATABASES')
#@st.experimental_memo (ttl=5*60)
def get_data(SQL):
  return con.execute(SQL).df()
try :
  start = timer()
  df = get_data(SQL) 
  end = timer()
  st.write("Duration in Second")
  st.write(round(end - start,2))
  st.write(df)
except Exception as er:
 st.write(df = pd.DataFrame([{'error':er}]))
