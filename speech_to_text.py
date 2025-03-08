import whisper

def transcribe_audio(audio_file):
    model = whisper.load_model("tiny")
    result = model.transcribe(audio_file)
    return result["text"]

if __name__ == "__main__":
    text = transcribe_audio("meeting_audio.mp3")
    print(text)
