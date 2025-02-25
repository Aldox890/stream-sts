import os

import keyboard
import sounddevice as sd
import numpy as np
import wave


def record_audio(filename, samplerate=44100, channels=1):
    print("Press and hold space to record...")
    audio_data = []
    recording = False

    def callback(indata, frames, time, status):
        if status:
            print(status)
        if recording:
            audio_data.append(indata.copy())

    with sd.InputStream(samplerate=samplerate, channels=channels, callback=callback):
        while True:
            if keyboard.is_pressed('space'):
                if not recording:
                    print("Recording started...")
                    recording = True

            elif recording:
                print("Recording stopped.")
                break

    audio_array = np.concatenate(audio_data, axis=0)

    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes((audio_array * 32767).astype(np.int16).tobytes())


if __name__ == "__main__":
    input_audio = "recorded.wav"

    record_audio(input_audio)
