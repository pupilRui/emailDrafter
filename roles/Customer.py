import openai

def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    return response.choices[0].message["content"]

class Customer:
    def __init__(self, api_key, products, language="en"):
        self.api_key = api_key
        self.products = products
        self.language = language
        openai.api_key = self.api_key

    def generate_question_or_comment(self):
        # Create a list of product names
        product_list = ", ".join(self.products.keys())
        
        # Use OpenAI API to generate a question or comment based on the product list
        prompt = (f"Craft a text message in {self.language} language. "
                f"Inquire about one or two of the following products: {product_list}. "
                f"Ask the store for more details in about 40 words.")
        
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",  # specify the engine here
            prompt=prompt,
            max_tokens=100,
            temperature=0.0
        )

        response_text = response.choices[0].text.strip()

        return response_text

