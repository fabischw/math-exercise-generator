import streamlit as st
import random
import math

st.title("fractional calculation")
st.caption("This page provides a overview of the easiest mathematical laws.")
st.sidebar.success("Select page")



basics_tab, fractal_laws_tab = st.tabs(["basics", "fractal-laws"])



with basics_tab:


    with st.expander("Commutative law"):
        st.latex(fr'''a + b = b + a''')
        st.latex(fr'''a * b = b * a''')
        st.latex(fr'''a\% * b = b\% * a''')



    with st.expander("associative law"):
        st.latex(fr'''a + (b + c) = (a + b) + c''')
        st.latex(fr'''a * (b * c) = (a * b) * c''')



    with st.expander("distributive law"):
        st.latex(fr'''a * b + a * c = a * (b + c)''')