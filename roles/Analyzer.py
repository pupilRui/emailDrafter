import openai

class CommentSentimentAnalyzer:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def analyze_sentiment(self, customer_comment):
        # Sentiment analysis of the customer's comment
        prompt_sentiment = f"Analyze the sentiment of the following customer comment: '{customer_comment}'. Is it Positive or Negative?"
        response_sentiment = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt_sentiment,
            max_tokens=50,
            temperature=0.7
        )
        sentiment = response_sentiment.choices[0].text.strip()

        return sentiment