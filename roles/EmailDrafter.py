import openai

class EmailSubjectGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_subject(self, customer_comment, language="English"):
        # Use OpenAI API to generate an email subject based on the customer's comment and desired language
        prompt = f"Inferring an email subject from the following customer comment: '{customer_comment}' in the desired language: '{language}', directly return the subject without start with 'Possible email subject:'"

        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",  # specify the engine here
            prompt=prompt,
            max_tokens=50,
            temperature=0.7
        )

        return response.choices[0].text.strip()

class CommentSummarizer:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def summarize_and_translate(self, customer_comment, target_language):
        # Step 3.1: Generate the summary in English
        prompt_summary = f"Summarize the following customer comment: '{customer_comment}'."
        response_summary = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt_summary,
            max_tokens=100,
            temperature=0.7
        )
        english_summary = response_summary.choices[0].text.strip()

        # Step 3.2: Translate the English summary into the customer's selected language
        prompt_translation = f"Translate the following English summary into {target_language}: '{english_summary}'."
        response_translation = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt_translation,
            max_tokens=100,
            temperature=0.7
        )
        translated_summary = response_translation.choices[0].text.strip()

        return translated_summary
    
class EmailGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_email(self, customer_comment, comment_summary, sentiment, language, products):
        # Generate an email based on the customer's comment, its summary, sentiment, and language
        prompt_email = (f"Given the customer's comment: '{customer_comment}', "
                        f"its summary: '{comment_summary}', its sentiment: '{sentiment}', "
                        f"and the desired language: '{language}', "
                        f"and the product info: '{products}', craft an email response in 100 words:")
        
        response_email = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt_email,
            max_tokens=600,
            temperature=0.7
        )
        email_content = response_email.choices[0].text.strip()

        return email_content

