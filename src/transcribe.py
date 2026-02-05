import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["HF_HUB_DISABLE_SYMLINKS"] = "1"
os.environ["HF_HOME"] = os.path.abspath("hf_cache")

from faster_whisper import WhisperModel

# Best balance of accuracy and speed (CPU-friendly but strong)
model = WhisperModel("large-v3", compute_type="int8")

def transcribe_audio(path):
    segments, info = model.transcribe(
        path,
        task="translate",      # 🔥 Direct speech → English
        beam_size=7,           # better decoding
        vad_filter=True        # remove silent/noisy parts
    )

    full_text = ""
    segment_data = []

    for seg in segments:
        full_text += seg.text.strip() + " "
        segment_data.append({
            "start": round(seg.start, 2),
            "end": round(seg.end, 2),
            "text": seg.text.strip()
        })

    return full_text.strip(), info.language, segment_data
