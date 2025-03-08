import streamlit as st
from speech_to_text import transcribe_audio
from summarization import summarize_text
from ner_extraction import extract_action_items
from email_sender import send_email

st.title("🎙️ AI-Powered Meeting Summarizer")

uploaded_file = st.file_uploader("Upload Meeting Audio", type=["mp3", "wav"])

if uploaded_file:
    st.write("🔄 Transcribing audio...")
    transcript = transcribe_audio(uploaded_file)

    st.write("### 📜 Transcript:")
    st.write(transcript)

    st.write("🔄 Summarizing meeting notes...")
    summary = summarize_text(transcript)

    st.write("### ✨ Summary:")
    st.write(summary)

    st.write("🔄 Extracting action items...")
    actions = extract_action_items(transcript)

    st.write("### 📌 Action Items:")
    st.write(actions)

    recipient_email = st.text_input("📧 Enter email to send summary:")
    if st.button("Send Summary"):
        send_email(summary, recipient_email)
        st.success("✅ Summary sent successfully!")
