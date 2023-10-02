from flask import Flask, render_template, request, jsonify
import openai

import os
from roles.Customer import Customer
from variables import products
from roles.EmailDrafter import EmailSubjectGenerator, CommentSummarizer, EmailGenerator
from roles.Analyzer import CommentSentimentAnalyzer
import time

script_dir = os.path.dirname(os.path.abspath(__file__))

# Load .env file from script_dir
env_path = os.path.join(script_dir, ".env")
with open(env_path) as env:
    for line in env:
        key, value = line.strip().split("=")
        os.environ[key] = value

openai.api_key = os.environ.get("API_KEY")
openai.organization = os.environ.get("ORG_ID")



app = Flask(__name__)

language = "English"


# Initialize your classes and methods here
# For example:
# customer = Customer(api_key="YOUR_OPENAI_API_KEY", products=product_list)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_comment', methods=['POST'])
def generate_comment():
    # Call your methods to generate a comment
    # For example:
    # comment = customer.generate_question_or_comment()
    global language
    language = request.form.get('language')
    print("language: ", language)

    customer = Customer(openai.api_key, products, language)
    comment = customer.generate_question_or_comment()
    # comment = "This is a generated comment."  # Placeholder
    return jsonify({'comment': comment})

@app.route('/generate_reply', methods=['POST'])
def generate_reply():
    global language
    comment = request.form.get('comment')
    print("replying language: ", language)
    # language = request.form.get('language')


    email_subject_generator = EmailSubjectGenerator(openai.api_key)
    email_subject = email_subject_generator.generate_subject(comment, language)
    print(f"Email subject: {email_subject}")


    time.sleep(20)

    comment_summarizer = CommentSummarizer(openai.api_key)
    translated_summary = comment_summarizer.summarize_and_translate(comment, language)
    print(f"Translated summary: {translated_summary}")

    time.sleep(20)


    analyzer = CommentSentimentAnalyzer(openai.api_key)
    sentiment = analyzer.analyze_sentiment(comment)
    print(f"Sentiment: {sentiment}")

    time.sleep(20)


    # Step 4: Generate the email body
    contentGenerator = EmailGenerator(openai.api_key)
    reply = contentGenerator.generate_email(comment, translated_summary, sentiment, language, products)
    # print(f"Email body: {email_body}")
    # Call your methods to generate a reply to the comment
    # For example:
    # reply = reply_gen.generate_reply(comment)
    # reply = "This is a generated reply to your comment."  # Placeholder
    return jsonify({'reply': reply, 'subject': email_subject})

if __name__ == '__main__':
    app.run(debug=True)
