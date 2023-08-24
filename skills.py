import pandas as pd
import streamlit as st
st.set_page_config(layout='wide')

def main():
    if 'analyst' not in st.session_state:
        st.session_state.analyst = pd.DataFrame(columns=["Data Analyst"])
    if 'bi' not in st.session_state:
        st.session_state.bi = pd.DataFrame(columns=["BI Analyst"])
    if 'engineer' not in st.session_state:
        st.session_state.engineer = pd.DataFrame(columns=["Data Engineer"])
    if 'scientist' not in st.session_state:
        st.session_state.scientist = pd.DataFrame(columns=["Data Scientist"])

    if st.button("Restore Data"):
        st.session_state.analyst = pd.DataFrame(columns=["Data Analyst"])
        st.session_state.bi = pd.DataFrame(columns=["BI Analyst"])
        st.session_state.engineer = pd.DataFrame(columns=["Data Engineer"])
        st.session_state.scientist = pd.DataFrame(columns=["Data Scientist"])
        st.success("Restored the DataFrames to their original state.")
    df = pd.read_excel("skills.xlsx")
    skills = df["skills"].values.tolist()

    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        skill = st.radio("Select Column:", skills)
    with c2:
        if st.button("Add to Data Analyst"):
            st.session_state.analyst = st.session_state.analyst.append({"Data Analyst":skill}, ignore_index = True)
            st.success("Added to Data Analyst's skills list")
        st.write(st.session_state.analyst)
    with c3:
        if st.button("Add to BI Analyst"):
            st.session_state.bi = st.session_state.bi.append({"BI Analyst":skill}, ignore_index = True)
            st.success("Added to BI Analyst's skills list")
        st.write(st.session_state.bi)
    with c4:
        if st.button("Add to Data Engineer"):
            st.session_state.engineer = st.session_state.engineer.append({"Data Engineer":skill}, ignore_index = True)
            st.success("Added to Data Engineer's skills list")
        st.write(st.session_state.engineer)
    with c5:
        if st.button("Add to Data Scientist"):
            st.session_state.scientist = st.session_state.scientist.append({"Data Scientist":skill}, ignore_index = True)
            st.success("Added to Data Scientist's skills list")
        st.write(st.session_state.scientist)
    
    st.write(" ")
    

main()
