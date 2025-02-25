import os

from elevenlabs import ElevenLabs

ELEVENLABS_API_KEY = os.getenv("API_KEY")
VOICE_ID = os.getenv("VOICE_ID")

client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
client.speech_to_speech.convert(
    voice_id=VOICE_ID,
    output_format="mp3_44100_128",
    audio={"type": "file"},
    model_id={"type": "json", "value": "eleven_multilingual_sts_v2"}
)
