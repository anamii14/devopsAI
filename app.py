import streamlit as st

from main import (
    read_logs,
    deduplicate,
    create_incidents,
    generate_timeline
)

from ai_part import generate_ai_report
from graph_visualizer import generate_graph


st.set_page_config(page_title="DevOps AI Dashboard", layout="wide")

st.title("DevOps AI Incident Dashboard")

uploaded_file = st.file_uploader("Upload logs file", type=["txt", "log"])


# ---------------- SESSION STATE ----------------
if "logs" not in st.session_state:
    st.session_state.logs = None
if "incidents" not in st.session_state:
    st.session_state.incidents = None
if "timeline" not in st.session_state:
    st.session_state.timeline = None


# ---------------- PROCESS FILE (ONLY ON UPLOAD) ----------------
if uploaded_file and st.session_state.logs is None:

    with open("temp_logs.txt", "wb") as f:
        f.write(uploaded_file.read())

    st.session_state.logs = read_logs("temp_logs.txt")

    freq = deduplicate(st.session_state.logs)
    st.session_state.incidents = create_incidents(freq, st.session_state.logs)
    st.session_state.timeline = generate_timeline(st.session_state.logs)


# ---------------- INCIDENTS ----------------
if st.session_state.incidents:
    st.subheader("Incidents")

    for i, inc in enumerate(st.session_state.incidents, 1):
        st.markdown(f"""
### Incident {i}
- Service: {inc.get('service', '')}
- Issue: {inc.get('issue', '')}
- Severity: {inc.get('severity', '')}
- Count: {inc.get('count', '')}
- Timestamp: {inc.get('timestamp', '')}
---
""")

# ---------------- TIMELINE ----------------
if st.session_state.timeline:
    st.subheader("Timeline")
    st.text("\n".join(st.session_state.timeline))


# ---------------- AI ----------------
mode = st.selectbox(
    "Select AI Mode",
    ["FULL", "SUMMARY", "ROOT_CAUSE", "IMPACT", "FIXES"]
)

if st.session_state.incidents and st.button("Generate AI Report"):

    report = generate_ai_report(
        st.session_state.incidents,
        st.session_state.timeline,
        mode
    )

    st.subheader("AI Report")
    st.code(report)


# ---------------- GRAPH ----------------
if st.session_state.incidents and st.button("Show Graph"):

    fig = generate_graph(st.session_state.incidents)
    st.pyplot(fig)