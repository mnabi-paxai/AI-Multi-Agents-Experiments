# quick_elevenlabs_check.py
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = (os.getenv("ELEVENLABS_API_KEY") or "").strip()
if not API_KEY:
    raise SystemExit("No ELEVENLABS_API_KEY found. Put it in .env or your shell.")

from elevenlabs import ElevenLabs  # SDK 2.x

client = ElevenLabs(api_key=API_KEY)

# --- 1) Auth sanity check (no shape assumptions) ---
try:
    models = client.models.list()          # returns a Python list in 2.15.0
    if not isinstance(models, list) or not models:
        raise RuntimeError("models list unexpectedly empty")
    first_model = models[0]
    # be defensive about attributes vs dicts
    model_name = getattr(first_model, "name", None) or getattr(first_model, "model_id", None) or str(first_model)
    print("Auth OK. First model:", model_name)
except Exception as e:
    raise SystemExit(f"Auth failed → {e}")

# --- 2) Pick a voice you actually have access to ---
try:
    # Prefer the new get_all() endpoint for user voices
    voices_resp = client.voices.get_all()  # returns an object with .voices in current docs
    voices = getattr(voices_resp, "voices", None) or voices_resp or []
    if not voices:
        raise RuntimeError("No voices returned on your account.")
    # choose by name if you like; here we just grab the first
    chosen = voices[0]
    voice_id = getattr(chosen, "voice_id", None) or chosen.get("voice_id")
    voice_name = getattr(chosen, "name", None) or chosen.get("name")
    print(f"Using voice: {voice_name} ({voice_id})")
except Exception as e:
    raise SystemExit(f"Could not list voices → {e}")

# --- 3) Generate speech (streamed) ---
text = "Hello from the updated ElevenLabs SDK!"
try:
    audio_stream = client.text_to_speech.convert(
        text=text,
        voice_id=voice_id,
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
    )
except Exception as e:
    raise SystemExit(f"TTS request failed → {e}")

# --- 4) Save the audio stream to file ---
out_path = "output.mp3"
with open(out_path, "wb") as f:
    for chunk in audio_stream:
        if isinstance(chunk, bytes):
            f.write(chunk)

print("Saved:", out_path)
