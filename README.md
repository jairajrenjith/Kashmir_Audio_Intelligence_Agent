# Kashmiri Multilingual Audio Intelligence Agent

An **offline multilingual audio intelligence system** designed to analyze noisy real-world speech recordings containing **Kashmiri, Hindi, and Urdu** — often mixed within the same conversation — and convert them into **structured, actionable intelligence**.

This system helps analysts quickly prioritize large volumes of recordings by automatically detecting **threat signals, suspects, locations, and risk levels**.

---

## Core Capabilities

### Speech Recognition (Offline)
- Processes **noisy field audio**
- Handles **Kashmiri, Hindi, Urdu**, and mixed speech
- Uses **Faster-Whisper (Whisper large-v3)** for high-accuracy transcription
- Automatically detects spoken language

### Automatic Translation
- Converts transcripts into **clear English**
- Uses an offline **MarianMT multilingual model**

### Context-Aware Intelligence Extraction
The system identifies:

| Category | Extracted Information |
|---------|-----------------------|
| 👤 People | Names mentioned in conversation |
| 📍 Locations | Cities, regions, landmarks |
| 🕒 Time References | Dates, times, schedules |
| ⚠ Threat Keywords | Words like *attack, blast, weapon* |
| 🧍 Suspects | People linked with threat language |

### Risk Assessment Engine
Each audio file is classified as:

| Risk Level | Criteria |
|-----------|----------|
| **HIGH** | Threat keywords + sensitive location |
| **MEDIUM** | Threat keywords only |
| **LOW** | No threat indicators |

---

## System Architecture

```
Audio Input
   ↓
Preprocessing (Noise handling + WAV conversion)
   ↓
Speech-to-Text (Faster-Whisper)
   ↓
Language Detection
   ↓
Translation to English
   ↓
NLP Analysis (NER + Keyword Detection)
   ↓
Suspect Detection Logic
   ↓
Risk Scoring Engine
   ↓
Structured Intelligence Report
```

---

## Project Structure

```
KASHMIR_AUDIO_AGENT/
│
├── app.py                        # Streamlit UI entry point
├── requirements.txt              # Project dependencies
│
├── audio_samples/                # Example/test audio files
│
├── data/
│   ├── threat_keywords.txt
│   └── sensitive_locations.txt
│
├── hf_cache/                     # HuggingFace offline model cache
│
├── src/
│   ├── __pycache__/
│   ├── preprocess.py             # Audio conversion & cleanup
│   ├── transcribe.py             # Speech recognition (Whisper)
│   ├── translate.py              # Translation to English
│   ├── keywords.py               # Threat keyword detection
│   ├── ner.py                    # Named Entity Recognition
│   ├── risk_agent.py             # Risk scoring + suspect logic
│   └── report.py                 # Transcript highlighting
│
├── temp/                         # Temporary audio processing files
├── venv/                         # Virtual environment (optional)
├── temp.wav                      # Temporary converted audio
└── README.md
```

---

## How It Works (Step-by-Step)

### 1. Audio Preprocessing
Audio files are converted into:
- Mono channel  
- 16kHz sample rate  
Ensures optimal speech recognition accuracy.

### 2. Speech Recognition
Uses **Faster-Whisper (large-v3)** for:
- Offline transcription  
- Background noise handling  
- Voice Activity Detection  
Outputs transcript + timestamps.

### 3. Translation
Non-English speech is translated into English using MarianMT.

### 4. Threat Keyword Detection
Transcript is scanned for threat-related terms from a custom list.

### 5. Named Entity Recognition (NER)
Detects:
- People  
- Locations  
- Dates & Times  
Powered by spaCy multilingual model.

### 6. Suspect Identification
A person becomes a suspect if their name appears in a transcript containing threat keywords.  
Suspicion score increases with number of threat indicators.

### 7. Risk Scoring
Combines:
- Threat presence  
- Sensitive location detection  
Produces LOW / MEDIUM / HIGH risk classification.

---

## User Interface

Built with **Streamlit** for easy offline use:

- Upload multiple audio files  
- View translated transcript  
- See highlighted threat terms  
- Get structured intelligence report  
- Batch risk summary dashboard  

---

## 📊 Structured Output Example

```
{
  "File": "audio_01.wav",
  "Detected Language": "ur",
  "Threat Words": ["attack", "weapon"],
  "People Mentioned": ["Rashid", "Imran"],
  "Potential Suspects": [
    {"name": "Rashid", "suspicion_score": 2}
  ],
  "Locations": ["Srinagar"],
  "Time References": ["tomorrow night"],
  "Audio Segments": [
    {"start": 0.5, "end": 4.2, "text": "..."}
  ],
  "Risk Level": "HIGH"
}
```

---

## Installation

```bash
git clone <repo-link>
cd kashmir-audio-agent
pip install -r requirements.txt
python -m spacy download xx_ent_wiki_sm
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Offline Design

✔ No internet required after model download  
✔ All models cached locally  
✔ Optimized for CPU usage  

---

## Use Cases

- Security monitoring  
- Intelligence triage  
- Field audio analysis  
- Multilingual threat detection  
- Rapid risk prioritization  

---

## ⚠ Disclaimer

This tool provides **automated risk estimation** to assist human analysts.  
It does **not** make legal determinations or replace professional investigation.

---

## Future Enhancements

- Speaker identification  
- Accent adaptation  
- Emotion detection  
- Real-time stream processing  
- Custom regional language tuning  

---

By Jairaj R, Ham P R, Ajo Jose
