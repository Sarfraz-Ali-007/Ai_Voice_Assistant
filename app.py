import os
import tempfile

import streamlit as st

from audio_recorder_streamlit import audio_recorder

from agents.assistant import agent

from voice.stt import transcribe
from voice.tts import speak


st.title("AI Voice Assistant")

audio_bytes = audio_recorder()

if audio_bytes:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    ) as f:

        f.write(audio_bytes)

        audio_path = f.name

    user_text = transcribe(audio_path)

    st.write("You:", user_text)

    response = agent.invoke(
        {
            "messages":[
                ("user", user_text)
            ]
        }
    )

    assistant_text = response["messages"][-1].content

    st.write("Assistant:", assistant_text)

    audio_file = speak(assistant_text)

    st.audio(audio_file)
