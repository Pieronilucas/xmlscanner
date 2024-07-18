import xml.etree.ElementTree as ET
import streamlit as st
from io import StringIO
import zipfile

# Function to check for specific CFOP codes in the XML
def check_cfop(xml_content):
    tree = ET.ElementTree(ET.fromstring(xml_content))
    root = tree.getroot()
    ns = {'ns': 'http://www.portalfiscal.inf.br/nfe'}
    cfop_codes = {"5910", "5.910", "6.910", "6910"}

    for cfop in root.findall('.//ns:CFOP', ns):
        if cfop.text in cfop_codes:
            return True
    return False

# Streamlit app
st.image('https://lh5.googleusercontent.com/p/AF1QipPwvMJHXGz6LPsOtgxr-S9e4j3vOZKWVBil3EZr=w284-h160-k-no')
st.title("CFOP Bonificação")

uploaded_files = st.file_uploader("Upload XML", accept_multiple_files=True, type=["xml"])

if uploaded_files:
    flagged = []
    for uploaded_file in uploaded_files:
        xml_content = uploaded_file.read().decode("utf-8")
        if check_cfop(xml_content):
            flagged.append(uploaded_file.name)

    if flagged:
        st.write("XMLs com o CFOP:")
        for file in flagged:
            st.write(file)
    else:
        st.write("Nenhuma nota com CFOP de bonificação.")
