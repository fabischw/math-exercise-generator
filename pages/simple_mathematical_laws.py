import streamlit as st
import random
import math

st.title("Mathematische Regeln / Gesetze")
st.caption("Diese Seite beinhaltet ")
st.sidebar.success("Seite auswählen")



basics_tab, fraction_laws_tab = st.tabs(["Grundlagen", "Brüche"])



with basics_tab:


    with st.expander("Kommutativgesetz"):
        st.latex(fr'''a + b = b + a''')
        st.latex(fr'''a * b = b * a''')
        st.latex(fr'''a\% * b = b\% * a''')



    with st.expander("Assoziativgesetz"):
        st.latex(fr'''a + (b + c) = (a + b) + c''')
        st.latex(fr'''a * (b * c) = (a * b) * c''')



    with st.expander("Distributivgesetz"):
        st.latex(fr'''a * b + a * c = a * (b + c)''')


with fraction_laws_tab:

    with st.expander("Definitionen"):
        st.subheader("Bruchdefinition:")
        st.latex(fr'''\frac{{a}}{{b}}''')
        st.write("ist ein Bruch, dabei heißt **a**  **Zähler** und **b** **Nenner** mit b ≠ 0")



        st.subheader("Kehrbrüche:")
        st.write("If a ≠ 0:")
        st.latex(fr'''\frac{{b}}{{a}}''')
        st.write("ist Kehrbrüche zu")
        st.latex(fr'''\frac{{a}}{{b}}''')
        st.write("Es gilt:")
        st.latex(fr'''\frac{{a}}{{b}} * \frac{{b}}{{a}} = 1''')

    with st.expander("Erweitern / Kürzen"):
        st.subheader("Brüche erweitern:")
        st.latex(fr'''\frac{{a}}{{b}} = \frac{{a * k}}{{b * k}}''')

        st.subheader("Brüche kürzen")
        st.latex(fr'''\frac{{a}}{{b}} = \frac{{a ÷ k}}{{b ÷ k}}''')


    with st.expander("Addition, Subtraktion, Multiplikation, Division"):
        st.write("Addition")
        st.latex(fr'''\frac{{a}}{{b}} + \frac{{c}}{{b}} = \frac{{a + c}}{{b}}''')
        st.latex(fr'''\frac{{a}}{{b}} + \frac{{c}}{{d}} = \frac{{a * d + b * c}}{{b * d}}''')

        st.write("Subtraktion")
        st.latex(fr'''\frac{{a}}{{b}} - \frac{{c}}{{b}} = \frac{{a - c}}{{b}}''')
        st.latex(fr'''\frac{{a}}{{b}} - \frac{{c}}{{d}} = \frac{{a * d - b * c}}{{b * d}}''')

        st.write("Multiplikation")
        st.latex(fr'''\frac{{a}}{{b}} * \frac{{c}}{{d}} = \frac{{a * c}}{{b * d}}''')

        st.write("Division")
        st.latex(fr'''\frac{{a}}{{b}} ÷ \frac{{c}}{{d}} = \frac{{a}}{{b}} * \frac{{d}}{{c}} = \frac{{a * d}}{{b * c}}''')


    with st.expander("verschiedene Bruchschreibweisen"):
        st.subheader("Dezimalschreibweise")
        st.latex(fr'''\frac{{a}}{{b}} = a ÷ b = c.d \quad \text{{(runde, um Dezimalbruch zu erhalten)}}''')
        
        st.subheader("Gemischte Schreibweise")
        st.latex(fr'''\frac{{a}}{{b}} = c\frac{{d}}{{b}}''')

        st.subheader("Prozent")
        st.latex(fr'''a.b = (a.b * 100)\%''')


