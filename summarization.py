from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small")

def summarize_text(text):
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    sample_text = "Your long meeting transcript..."
    print(summarize_text(sample_text))
