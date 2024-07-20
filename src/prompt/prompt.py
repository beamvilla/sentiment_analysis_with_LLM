def get_sentiment_classifier_prompt(message: str) -> str:
    prompt = f"""
    Your role: sentiment analyzer
    Task: Answer the one of sentiment in the sentiment list (["neutral", "negative", "positive", "question"]) of the given message.
    Message: {message}
    """
    return prompt