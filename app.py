import streamlit as st
from phishing_detector import is_phishing
import plotly.graph_objects as go

st.set_page_config(page_title="Phishing URL Detector", layout="centered", page_icon=":shield:")

st.markdown("## 🛡️ Phishing URL Detection Web App")
st.markdown("Enter a URL below to check if it's potentially malicious.")

with st.form("url_form"):
    url = st.text_input("🔗 Enter URL", placeholder="https://example.com")
    submit = st.form_submit_button("Analyze")

if submit and url:
    result, score = is_phishing(url)
    st.markdown("---")
    st.markdown("### 🔎 Result")
    gauge_color = "red" if result == 1 else "green"

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score * 100,
        title={'text': "Threat Probability (%)"},
        gauge={'axis': {'range': [0, 100]},
               'bar': {'color': gauge_color},
               'steps': [
                   {'range': [0, 50], 'color': "lightgreen"},
                   {'range': [50, 100], 'color': "pink"}]}))

    st.plotly_chart(fig)

    if result == 1:
        st.error("⚠️ This URL is likely **phishing**.")
    else:
        st.success("✅ This URL seems **safe**.")