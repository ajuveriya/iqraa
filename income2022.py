import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
import streamlit as st
#from sklearn.model_selection import train_test_split
#from sklearn.svm import SVC
#from tabulate import tabulate
school_df = pd.read_csv("school_income.csv")
st.title("IQRAA SCHOOL INCOME 2022")
st.sidebar.title("SCHOOL INCOME DETAILS")
if st.sidebar.checkbox("Show income data"):
    st.subheader("Full Dataset")
    st.dataframe(school_df)
    #st.write("January Income 2022: 250630")
    #st.write("January Expenditure 2022: 242644")
    #table = [['S.NO', 'NAME','INCOME', 'EXPENDITURE','BALANCE'], [1, 'QADEER PASHA', 250630,242644,7986], [2, 'KAREEMUDDIN',60370 ,47744,12626], [3, 'ARJ',73000 ,0,73000],[4, 'TOTAL',384000,	290388,73000]]
    df = pd.DataFrame(
    [['NAME', 'INCOME', 'EXPENDITURE','BALANCE'], ['QADEER PASHA', 250630,242644,7986], ['KAREEMUDDIN',60370 ,47744,12626], ['ARJ',73000 ,0,73000],['TOTAL',384000,	290388,73000]])
    st.table(df)
st.sidebar.subheader("Month Wise Income and Expenditure 2022")
plot_types = st.sidebar.multiselect("Select the Month:", 
                                    ('January', 'February', 'March', 'April', 'May', 'June','July',"August"))
if 'January' in plot_types:
    st.subheader("January 2022")
    st.dataframe(school_df)
    df = pd.DataFrame(
    [['NAME', 'INCOME', 'EXPENDITURE','BALANCE'], ['QADEER PASHA', 250630,242644,7986], ['KAREEMUDDIN',60370 ,47744,12626], ['ARJ',73000 ,0,73000],['TOTAL',384000,	290388,73000]],index=False)

    st.table(df)

if 'February' in plot_types:
    st.subheader("February 2022")
    st.dataframe(school_df)
    df = pd.DataFrame(
    [['NAME', 'INCOME', 'EXPENDITURE','BALANCE'], ['QADEER PASHA', 250630,242644,7986], ['KAREEMUDDIN',60370 ,47744,12626], ['ARJ',73000 ,0,73000],['TOTAL',384000,	290388,73000]])

    st.table(df)

