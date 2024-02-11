#description: This is a 'smart' chatbot program

pip install nltk
#Import the libraries


import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np
import warnings
warnings.filterwarnings('ignore')

#Download the punkt package
nltk.download('punkt', quiet=True)
# Function to return a random greeting respond to users' greeting
def greeting_response(text):
  text = text.lower()

  #Bot's greeting response
  bot_greetings = ['Hi there!','Hello','Heyy']
  #Users greetings
  user_greetings = ['hi','hey','hello','greetings']

  for word in text.split():
    if word in user_greetings:
      return random.choice(bot_greetings)

def index_sort(list_var):
  length = len(list_var)
  list_index = list(range(0,length))

  x = list_var
  for i in range(length):
    for j in range(length):
      if x[list_index[i]] > x[list_index[j]]:
        #Swap
        temp = list_index[i]
        list_index[i] = list_index[j]
        list_index[j] = temp

  return list_index



# Load the dataset
import json

with open('/dataset.json', 'r') as file:
    dataset = json.load(file)

def bot_response(user_input):
    # Preprocess user input
    user_input = user_input.lower()

    # Calculate similarity between user input and dataset questions
    similarity_scores = []
    for qa_pair in dataset:
        question = qa_pair['question'].lower()
        combined_text = [user_input, question]

        # Convert text to vectors
        vectorizer = CountVectorizer().fit_transform(combined_text)

        # Calculate cosine similarity
        similarity = cosine_similarity(vectorizer)

        # Append similarity score
        similarity_scores.append(similarity[0,1])

    # Find the index of the most similar question
    max_index = np.argmax(similarity_scores)

    # Return the corresponding answer
    bot_response = dataset[max_index]['answer']

    return bot_response


import re
import random

print('Shielder: I am the Cervical-Shield 🎗️, How can I help you today?')

def greeting_response(user_input):
    greetings = ['hello', 'hi', 'hey', 'howdy', 'hola', 'hii']
    user_input = user_input.lower()
    for word in user_input.split():
        if word in greetings:
            return random.choice(greetings) + '. How can I assist you today?'
    return None

def handle_name_input(user_input):
    name_pattern = r"my name is (\w+)"
    match = re.search(name_pattern, user_input.lower())
    if match:
        return f"Nice to meet you, {match.group(1)}. How can I assist you?"
    return None

exit_list = ['exit', ' see you later', 'bye', 'quit', 'break', 'done']

while True:
    user_input = input()
    if user_input.lower() in exit_list:
        print('Shielder: Chat with you later!')
        break
    else:
        greeting = greeting_response(user_input)
        if greeting is not None:
            print('Shielder: ' + greeting)
        else:
            name_response = handle_name_input(user_input)
            if name_response is not None:
                print('Shielder: ' + name_response)
            else:
                print('Shielder: ' + bot_response(user_input))  # Assuming bot_response function is defined elsewhere
