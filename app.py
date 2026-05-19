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

if uploaded_file:

    # Save temp file
    with open("temp_logs.txt", "wb") as f:
        f.write(uploaded_file.read())

    # ---------------- PROCESS DATA ----------------
    logs = read_logs("temp_logs.txt")

    freq = deduplicate(logs)
    incidents = create_incidents(freq, logs)
    timeline = generate_timeline(logs)

    # ---------------- INCIDENTS ----------------
    st.subheader("Incidents")

    for i, inc in enumerate(incidents, 1):
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
    st.subheader("Timeline")

    st.text("\n".join(timeline))


    # ---------------- AI ----------------
    mode = st.selectbox(
        "Select AI Mode",
        ["FULL", "SUMMARY", "ROOT_CAUSE", "IMPACT", "FIXES"]
    )

    if st.button("Generate AI Report"):

        report = generate_ai_report(incidents, timeline, mode)

        st.subheader("AI Report")

        # CLEAN, CONSISTENT OUTPUT (FIXED)
        st.code(report)


    # ---------------- GRAPH ----------------
    if st.button("Show Graph"):

        fig = generate_graph(incidents)

        st.pyplot(fig)