import streamlit as st
import random
import math

st.title("Bruchrechnen")
st.caption("Diese Seite bietet ein einfaches, aber nützliches Tool zur Erstellung verschiedener Übungen zum Bruchrechnen.")
st.sidebar.success("Seite auswählen")



reduce_fractals_tab, add_fractals_tab, multiply_fractals_tab = st.tabs(["Brüche kürzen", "Brüche addieren/subtrahieren", "Brüche multiplizieren/dividieren"])

def reduce_fractals(numerator, denominator):
    gcd = math.gcd(numerator,denominator)

    numerator_new = numerator // gcd
    denominator_new = denominator // gcd

    return (numerator_new,denominator_new)



with reduce_fractals_tab:
    digit_range = st.slider("Anzahl Stellen der Brüche", 1, 4, (1, 2),key="reduce_fractals_tab-digit_range")
    exercise_count = st.slider("Anzahl der Übungen",1, 20, (1,5),key="reduce_fractals_tab-exercise_count")

    if st.button("Aufgaben erstellen",key="reduce_fractals_tab-generate_button"):
        st.text("Kürze die Brüche:")
        for i in range(exercise_count[1]):
            numerator = random.randint(10**0,10**digit_range[1])
            denominator = random.randint(10**0,10**digit_range[1])

            gcd = math.gcd(numerator,denominator)

            reduced = reduce_fractals(numerator,denominator)
            numerator_result = reduced[0]
            denominator_result = reduced[1]

            st.latex(fr'''\frac{{{numerator}}}{{{denominator}}} = \frac{{{numerator_result}}}{{{denominator_result}}}''')
            st.text(f"(ggV: {gcd})")




with add_fractals_tab:
    digit_range = st.slider("Anzahl Stellen der Brüche", 1, 4, (1, 2),key="add_fractals_tab-digit_range")
    exercise_count = st.slider("Anzahl der Übungen",1, 20, (1,5),key="add_fractals_tab-exercise_count")
    numerator1 = None
    denominator1 = None
    numerator2 = None
    denominator2 = None


    if st.button("Aufgaben erstellen",key="add_fractals_tab-generate_button"):
        st.text("Addiere/Subtrahiere und kürze die Brüche:")
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
    digit_range = st.slider("Anzahl Stellen der Brüche", 1, 4, (1, 2),key="multiply_fractals_tab-digit_range")
    exercise_count = st.slider("Anzahl der Übungen",1, 20, (1,5),key="multiply_fractals_tab-exercise_count")
    numerator1 = None
    denominator1 = None
    numerator2 = None
    denominator2 = None


    if st.button("Aufgaben erstellen",key="multiply_fractals_tab-generate_button"):
        st.text("Multipliziere / Dividiere und kürze die Brüche:")
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


