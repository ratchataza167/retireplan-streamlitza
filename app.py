"""Streamlit entry point for the supplied RetirePlan HTML dashboard."""
from pathlib import Path
from urllib.parse import urlencode
import json

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="RetirePlan Dashboard", page_icon="💰", layout="wide")

PARAMETERS = {"age", "retire", "life", "invest", "monthly", "growth", "withdraw", "ret_pre", "ret_post", "inf"}
query = urlencode({key: st.query_params[key] for key in PARAMETERS if key in st.query_params})
# Serialize URL values as data, never executable JavaScript or HTML.
encoded_query = json.dumps(query, ensure_ascii=True).replace("<", "\\u003c")
html = Path(__file__).with_name("dashboard.html").read_text(encoding="utf-8")
html = html.replace("<head>", f"<head><script>window.__initialQuery = {encoded_query};</script>", 1)
components.html(html, height=1000, scrolling=True)
