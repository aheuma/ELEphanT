import streamlit as st
from pathlib import Path
from PIL import Image

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

st.set_page_config(layout="wide")
elephant_logo = Image.open("./ELEphanT_logo.png")
st.sidebar.image(elephant_logo, width=300)
st.sidebar.markdown("Copyright information: The logo has been developed on the basis of free resources from vecteezy.com. "
                    "\n - Artist: Vecteezy \n - Vector graphic: [Elephant Vectors](https://www.vecteezy.com/vector-art/2485692-elephant-kids-coloring-page-great-for-beginner-coloring-book)")

st.markdown("## Evaluating Easy Language in Children's Books")
exp0 = st.expander("Overview", expanded=True)
exp1 = st.expander("I. Introduction")
exp2 = st.expander("II. Preprocessing")
exp3 = st.expander("III. Tool Implementation")
exp4 = st.expander("IV. Tool Evaluation")
exp5 = st.expander("References")

with exp0:
    overview_md = read_markdown_file("./md-files/03_Overview.md")
    st.markdown(overview_md, unsafe_allow_html=True)
with exp1:
    introduction_md = read_markdown_file(
        "./md-files/03_Introduction.md")
    st.markdown(introduction_md, unsafe_allow_html=True)
with exp2:
    preprocessing_md = read_markdown_file(
        "./md-files/03_PreProcessing.md")
    st.markdown(preprocessing_md, unsafe_allow_html=True)
with exp3:
    implementation_md = read_markdown_file(
        "./md-files/03_Tool Implementation.md")
    st.markdown(implementation_md, unsafe_allow_html=True)
with exp4:
    evaluation_md = read_markdown_file(
        "./md-files/03_Tool Evaluation.md")
    st.markdown(evaluation_md, unsafe_allow_html=True)
with exp5:
    st.markdown("1:1 translation: \n - [bpb Standard German](https://www.bpb.de/shop/186122/allgemeine-geschaeftsbedingungen-mit-gesetzlichen-informationen/) "
                "\n - [bpb Easy Language](https://www.bpb.de/shop/201038/allgemeine-geschaefts-bedingungen-der-bpb-in-leicht-verstaendlicher-sprache/)")
    st.markdown("Easy language corpus: \n "
                "- [Deutsche Bundesregierung, Aufgaben von dem Bundes-Kanzler](https://www.bundesregierung.de/breg-de/leichte-sprache/aufgaben-bundeskanzler-leichte-sprache-1987838) \n"
                "- [Deutsches Bundesministerium für Gesundheit, Informationen zum Corona-Virus](https://www.zusammengegencorona.de/leichtesprache/informationen-zum-corona-virus/) \n"
                "- [Stadt Mainz, Johannes Gutenberg – Erfinder und Medienrevolutionär](https://www.mainz.de/microsite/gutenberg/service/gutenberg-website-leichte-sprache.php) \n"
                "- [Norddeutscher Rundfunk, Hamburger Rathaus wird 125 Jahre alt](https://www.ndr.de/fernsehen/barrierefreie_angebote/leichte_sprache/Hamburger-Rathaus-wird-125-Jahre-alt,rathaushamburg106.html) \n"
                "- [Lebenshilfe Landesverband Hamburg, Flüchtlinge mit Behinderung in Hamburg](https://ls.lhhh.de/wp-content/uploads/2017/02/20160224_projektzuflucht_leichtesprache.pdf) \n"
                "- [Stadt Hamburg, Das ist Hamburg](https://www.hamburg.de/barrierefrei/leichte-sprache/freizeit/15723834/das-ist-hamburg/) \n"
                "- [Bundesvereinigung Lebenshilfe e.V., Krieg in der Ukraine in Leichter Sprache](https://www.lebenshilfe.de/informieren/familie/krieg-in-der-ukraine-leichte-sprache) \n"
                "- [Lebenshilfe Bremen, Geschichten in Leichter Sprache](https://lebenshilfe-bremen.de/wp-content/uploads/2019/08/Leseprobe_Bart-ab_barrierefrei.pdf) \n"
                "- [Norddeutscher Rundfunk, Dornröschen in Leichter Sprache](https://www.ndr.de/fernsehen/barrierefreie_angebote/leichte_sprache/Dornroeschen,dornroeschenleichtesprache100.html) \n"
                "- [Barrierefreie IT Hessen, Barriere-Freiheit in der IT erklärt](https://lbit.hessen.de/startseite-leichte-sprache/texte-in-leichter-sprache/barriere-freiheit-in-der-it-in-leichter-sprache) \n")
    st.markdown("All websites were last accessed on 15.12.2022.")