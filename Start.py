import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    elephant_logo = Image.open("ELEphanT_logo.png")
    st.image(elephant_logo, width=440)
with col2:
    st.markdown("# ELEphanT \n ### Easy Language Evaluation Tool")
    st.write("This page is a web presentation for the tool I developed during a university research project. "
                 "The tool offers the possibility to examine to what degree a given text complies to the rules of Easy Language. ")
    st.markdown("You will be able to: \n - Use the tool to [analyze](https://aheuma-elephant-start-ysqsc4.streamlit.app/ELEphanT_%E2%80%93_Analyze_Your_Text) "
                "your own text \n - Learn about [Easy Language in Germany](https://aheuma-elephant-start-ysqsc4.streamlit.app/Information_on_Easy_Language) "
                "\n - Read about the [details of my research project](https://aheuma-elephant-start-ysqsc4.streamlit.app/Information_on_Research_Project)")
    st.markdown("The original tool can be found in a [repository](https://gitlab.rlp.net/aheumann/elephant) on Gitlab, without UI but including the "
                "possibility to analyze (and compare) multiple texts at once.")
st.sidebar.markdown("Copyright information: The logo has been developed on the basis of free resources from vecteezy.com. "
                    "\n - Artist: Vecteezy \n - Vector graphic: [Elephant Vectors](https://www.vecteezy.com/vector-art/2485692-elephant-kids-coloring-page-great-for-beginner-coloring-book)")
