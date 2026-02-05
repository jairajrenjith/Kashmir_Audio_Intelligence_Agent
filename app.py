import streamlit as st
import os

from src.preprocess import convert_to_wav
from src.transcribe import transcribe_audio
from src.keywords import load_keywords, find_threat_words
from src.ner import extract_entities
from src.risk_agent import load_sensitive_locations, compute_risk, detect_suspects
from src.report import highlight_text

st.title("🎧 Offline Multilingual Audio Intelligence Agent")

uploaded_files = st.file_uploader(
    "Upload Audio Files",
    type=["wav", "mp3", "m4a"],
    accept_multiple_files=True
)

if uploaded_files:
    keywords = load_keywords()
    sensitive_locs = load_sensitive_locations()
    all_reports = []

    for uploaded in uploaded_files:
        st.divider()
        st.subheader(f"Processing: {uploaded.name}")

        os.makedirs("temp", exist_ok=True)
        input_path = os.path.join("temp", uploaded.name)

        with open(input_path, "wb") as f:
            f.write(uploaded.read())

        wav_path = convert_to_wav(input_path)

        st.info("Transcribing & Translating...")
        transcript, lang, segments = transcribe_audio(wav_path)

        threat_words = find_threat_words(transcript, keywords)
        persons, locations, times = extract_entities(transcript)
        suspects = detect_suspects(persons, transcript, threat_words)

        risk = compute_risk(threat_words, locations, sensitive_locs)
        highlighted = highlight_text(transcript, threat_words)

        st.markdown("### 🌍 English Transcript")
        st.write(highlighted)

        report = {
            "File": uploaded.name,
            "Original Language": lang,
            "Threat Words": threat_words,
            "People Mentioned": persons,
            "Potential Suspects": suspects,
            "Locations": locations,
            "Time References": times,
            "Audio Segments": segments,
            "Risk Level": risk
        }

        st.markdown("### 🧠 Intelligence Report")
        st.json(report)

        if risk == "HIGH":
            st.error("🚨 HIGH RISK ALERT")
        elif risk == "MEDIUM":
            st.warning("⚠️ Medium Risk Detected")
        else:
            st.success("✅ Low Risk")

        all_reports.append(report)

    st.divider()
    st.header("📊 Batch Summary")

    st.json({
        "Total Files": len(all_reports),
        "High Risk": sum(r["Risk Level"] == "HIGH" for r in all_reports),
        "Medium Risk": sum(r["Risk Level"] == "MEDIUM" for r in all_reports),
        "Low Risk": sum(r["Risk Level"] == "LOW" for r in all_reports),
    })
