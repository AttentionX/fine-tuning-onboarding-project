import sys
import gpt

model = gpt.ft_gpt

if len(sys.argv) > 1:
    if sys.argv[1] == 'o':
        model = gpt.gpt3
        print('Using GPT-3')
        
user_input = input("Enter a Question: ")

chat_history = '\nQ: '+user_input+'\nA: '

# answer = gpt.ft_gpt(chat_history)
answer = model(chat_history)
print('Answer:', answer)

# chat_history = ''

# while True:
#     user_input = input("Enter a Question: ")

#     chat_history += '\nQ: '+user_input+'\nA: '

#     answer = model(chat_history)
#     print('Answer:', answer)
#     chat_history += answer