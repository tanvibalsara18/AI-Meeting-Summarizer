# 🚀 AI-Meeting-Summarizer 

AI-Meeting-Summarizer transcribes meetings, extracts key insights, and sends concise summaries via email using NLP techniques.  

## 🔹 Features  
✅ **Speech-to-Text**: Convert meetings into transcripts  
✅ **AI Summarization**: Extract key points and action items  
✅ **Named Entity Recognition (NER)**: Identify important names, dates, and organizations  
✅ **Automated Email**: Send meeting summaries directly to participants  

## ⚙️ Tech Stack  
- **Python** (Backend)  
- **Streamlit** (Web UI)  
- **OpenAI GPT** (Summarization & NER)  
- **pydub** (Audio processing)  
- **SpeechRecognition** (Speech-to-text)  
- **smtplib** (Email automation)  

## 🚀 Setup  
```bash
git clone https://github.com/tanvibalsara18/AI-Meeting-Summarizer 
cd AI-Meeting-Summarizer 
pip install -r requirements.txt  
echo "OPENAI_API_KEY=your_api_key_here" > .env  
streamlit run app.py  
