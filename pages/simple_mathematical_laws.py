import streamlit as st
import random
import math

st.title("fractional calculation")
st.caption("This page provides a overview of the easiest mathematical laws.")
st.sidebar.success("Select page")



basics_tab, fraction_laws_tab = st.tabs(["basics", "fraction-laws"])



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


with fraction_laws_tab:

    with st.expander("definitions"):
        st.subheader("fraction definition:")
        st.latex(fr'''\frac{{a}}{{b}}''')
        st.write("is a fraction with **a** being **numerator** and **b** being **denominator** wih b ≠ 0")



        st.subheader("Reciprocal:")
        st.write("If a ≠ 0:")
        st.latex(fr'''\frac{{b}}{{a}}''')
        st.write("is the reciprocal to")
        st.latex(fr'''\frac{{a}}{{b}}''')
        st.write("It applies:")
        st.latex(fr'''\frac{{a}}{{b}} * \frac{{b}}{{a}} = 1''')

    with st.expander("expanding / reducing fractions"):
        st.subheader("Expanding fractions:")
        st.latex(fr'''\frac{{a}}{{b}} = \frac{{a * k}}{{b * k}}''')

        st.subheader("Reducing fractions")
        st.latex(fr'''\frac{{a}}{{b}} = \frac{{a ÷ k}}{{b ÷ k}}''')


    with st.expander("addition, subtraction, multiplication, division"):
        st.write("Addition")
        st.latex(fr'''\frac{{a}}{{b}} + \frac{{c}}{{b}} = \frac{{a + c}}{{b}}''')
        st.latex(fr'''\frac{{a}}{{b}} + \frac{{c}}{{d}} = \frac{{a * d + b * c}}{{b * d}}''')

        st.write("Subtraction")
        st.latex(fr'''\frac{{a}}{{b}} - \frac{{c}}{{b}} = \frac{{a - c}}{{b}}''')
        st.latex(fr'''\frac{{a}}{{b}} - \frac{{c}}{{d}} = \frac{{a * d - b * c}}{{b * d}}''')

        st.write("Multiplication")
        st.latex(fr'''\frac{{a}}{{b}} * \frac{{c}}{{d}} = \frac{{a * c}}{{b * d}}''')

        st.write("Division")
        st.latex(fr'''\frac{{a}}{{b}} ÷ \frac{{c}}{{d}} = \frac{{a}}{{b}} * \frac{{d}}{{c}} = \frac{{a * d}}{{b * c}}''')


    with st.expander("fraction notations"):
        st.subheader("decimal notation")
        st.latex(fr'''\frac{{a}}{{b}} = a ÷ b = c.d \quad \text{{(round to get decimal notation)}}''')
        
        st.subheader("mixed number")
        st.latex(fr'''\frac{{a}}{{b}} = c\frac{{d}}{{b}}''')

        st.subheader("percentages")
        st.latex(fr'''a.b = (a.b * 100)\%''')


