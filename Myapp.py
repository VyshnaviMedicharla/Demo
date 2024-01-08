import streamlit as st
st.set_page_config(page_title="Naruto")
st.header("Amine")
col1,col2 =st.columns(2)
with col1:
  st.subheader("Naruto")
  st.image("./naruto.jpg",caption="Naruto",width=300,use_column_width=True)
  st.write("Naruto is a Hokage")
with col2:
  st.subheader("Hinata")
  st.image("./hinata.jpg",caption="Hinata",width=300,use_column_width= True)
  st.write("Hinata a Hyūga clan girl")
  
  
  
