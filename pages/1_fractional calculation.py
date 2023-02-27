import streamlit as st
import random
import math

st.title("fractional calculation")
st.caption("This page provides a simple, yet useful tool to create different exercises related to fractional calculation")
st.sidebar.success("Select page")



reduce_fractals_tab, add_fractals_tab, multiply_fractals_tab = st.tabs(["Reduce fractals", "Add/Substract fractals", "Multiply / Divide fractals"])

def reduce_fractals(numerator, denominator):
    gcd = math.gcd(numerator,denominator)

    numerator_new = numerator // gcd
    denominator_new = denominator // gcd

    return (numerator_new,denominator_new)



with reduce_fractals_tab:
    digit_range = st.slider("Digits of Numbers used", 1, 4, (1, 2),key="reduce_fractals_tab-digit_range")
    exercise_count = st.slider("Number of exercises to be generated",1, 20, (1,5),key="reduce_fractals_tab-exercise_count")

    if st.button("generate exercise(s)",key="reduce_fractals_tab-generate_button"):
        st.text("reduce the following fractions")
        for i in range(exercise_count[1]):
            numerator = random.randint(10**0,10**digit_range[1])
            denominator = random.randint(10**0,10**digit_range[1])

            gcd = math.gcd(numerator,denominator)

            reduced = reduce_fractals(numerator,denominator)
            numerator_result = reduced[0]
            denominator_result = reduced[1]

            st.latex(fr'''\frac{{{numerator}}}{{{denominator}}} = \frac{{{numerator_result}}}{{{denominator_result}}}''')
            st.text(f"(greatest common denominator: {gcd})")




with add_fractals_tab:
    digit_range = st.slider("Digits of Numbers used", 1, 4, (1, 2),key="add_fractals_tab-digit_range")
    exercise_count = st.slider("Number of exercises to be generated",1, 20, (1,5),key="add_fractals_tab-exercise_count")
    numerator1 = None
    denominator1 = None
    numerator2 = None
    denominator2 = None


    if st.button("generate exercise(s)",key="add_fractals_tab-generate_button"):
        st.text("Add and reduce the following expression(s)[solutions given for reference]:")
        for i in range(exercise_count[1]):
            numerator1 = random.randint(10**0,10**digit_range[1])
            denominator1 = random.randint(10**0,10**digit_range[1])
            numerator2 = random.randint(10**0,10**digit_range[1])
            denominator2 = random.randint(10**0,10**digit_range[1])
            add = random.choice([True, False])
            
            if add:
                add = "+"
                reduced = reduce_fractals((numerator1*denominator2)+(numerator2*denominator1),(denominator1*denominator2))
            else:
                add = "-"
                reduced = reduce_fractals((numerator1*denominator2)-(numerator2*denominator1),(denominator1*denominator2))

            
            numerator_result = reduced[0]
            denominator_result = reduced[1]


            st.latex(fr'''\frac{{{numerator1}}}{{{denominator1}}} {add} \frac{{{numerator2}}}{{{denominator2}}} = \frac{{{numerator_result}}}{{{denominator_result}}}''')








with multiply_fractals_tab:
    digit_range = st.slider("Digits of Numbers used", 1, 4, (1, 2),key="multiply_fractals_tab-digit_range")
    exercise_count = st.slider("Number of exercises to be generated",1, 20, (1,5),key="multiply_fractals_tab-exercise_count")
    numerator1 = None
    denominator1 = None
    numerator2 = None
    denominator2 = None


    if st.button("generate exercise(s)",key="multiply_fractals_tab-generate_button"):
        st.text("Add and reduce the following expression(s)[solutions given for reference]:")
        for i in range(exercise_count[1]):
            numerator1 = random.randint(10**0,10**digit_range[1])
            denominator1 = random.randint(10**0,10**digit_range[1])
            numerator2 = random.randint(10**0,10**digit_range[1])
            denominator2 = random.randint(10**0,10**digit_range[1])
            multiply = random.choice([True,False])

            if multiply:
                multiply = "*"
                reduced = reduce_fractals(numerator1*numerator2,denominator1*denominator2)
            else:
                multiply = "/"
                reduced = reduce_fractals(numerator1*denominator2,denominator1*numerator2)

            
            numerator_result = reduced[0]
            denominator_result = reduced[1]


            st.latex(fr'''\frac{{{numerator1}}}{{{denominator1}}} {multiply} \frac{{{numerator2}}}{{{denominator2}}} = \frac{{{numerator_result}}}{{{denominator_result}}}''')


