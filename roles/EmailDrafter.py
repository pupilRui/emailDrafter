import openai
from .ChatModelCompletor import get_completion_from_messages as get_completion_from_messages

class EmailSubjectGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_subject(self, customer_comment, language="English"):
        system_message = f"""
            You are a customer service representative of the store.\
            You need to generate an email subject based on the customer's comment and in {language} language.\
            The user comment will be provided delimited with \
            #### characters.\
            Only generate an email subject, with nothing else.\
        """

        user_message_1 = f"""
            {customer_comment} \
        """

        messages =  [
            {'role':'system',
            'content': system_message},
            {'role':'user',
            'content': f"####{user_message_1}####"},
        ]

        return get_completion_from_messages(messages)

class CommentSummarizer:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def summarize_and_translate(self, customer_comment, target_language):
        system_message = f"""
            You are a customer comment summarizer of the store.\
            You need to summarize the following customer comment and translate it into {target_language} language.\
            The customer comment will be delimited with \
            #### characters.\
            Only generate a summary, with nothing else.\
        """

        user_message_1 = f"""
            {customer_comment} \
        """

        messages =  [
            {'role':'system',
            'content': system_message},
            {'role':'user',
            'content': f"####{user_message_1}####"},
        ]

        return get_completion_from_messages(messages)
    
class EmailGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_email(self, customer_comment, comment_summary, sentiment, language, products):
        system_message = f"""
            You are a customer service representative of the store.\
            You need to generate an email based on the customer's comment, its summary, sentiment, and language.\
            The customer comment will be delimited with \
            #### characters.\
            The summary will be delimited with \
            ##### characters.\
            The sentiment will be delimited with \
            ###### characters.\
            Your email should be written in {language}.\
            The product info is {products}.\
            Only generate an email response, with nothing else.\
        """

        user_message_1 = f"""
            ####{customer_comment}#### \
            #####{comment_summary}##### \
            ######{sentiment}###### \
        """

        messages =  [
            {'role':'system',
            'content': system_message},
            {'role':'user',
            'content': f"{user_message_1}"},
        ]

        return get_completion_from_messages(messages)

