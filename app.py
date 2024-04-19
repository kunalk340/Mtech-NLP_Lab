# import streamlit as st
# import openai
# from streamlit_chat import message

# st.write("Hello Welcome")
# openai.api_key = "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"

# def api_calling(prompt):
#     completions = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )
#     message = completions.choices[0].text
#     return message

# st.title("ChatGPT ChatBot With Streamlit and OpenAI")

# user_input = st.text_input("Write here")

# # Get or initialize session state variables
# user_input_history = st.session_state.get('user_input', [])
# openai_response_history = st.session_state.get('openai_response', [])

# if user_input:
#     output = api_calling(user_input)
#     output = output.lstrip("\n")

#     # Update session state variables
#     user_input_history.append(user_input)
#     openai_response_history.append(output)

# message_history = st.empty()

# if user_input_history:
#     for i in range(len(user_input_history) - 1, -1, -1):
#         # This function displays user input
#         message(user_input_history[i], 
#                 key=str(i), avatar_style="icons")
#         # This function displays OpenAI response
#         message(openai_response_history[i], 
#                 avatar_style="miniavs", is_user=True,
#                 key=str(i) + 'data_by_user')

import streamlit as st
import openai
from streamlit_chat import message
st.write("Hello ! Welcome to ChatBot")
openai.api_key = "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"

def api_calling(prompt):
    # completions = openai.Completion.create(
    #     engine="text-davinci",  # Use a supported model, e.g., text-davinci
    #     prompt=prompt,
    #     max_tokens=1024,
    #     n=1,
    #     stop=None,
    #     temperature=0.5,
    completions = openai.Completion.create(
    engine="text-gpt-3.5-turbo",  # Use a different model
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

    #)
    message = completions.choices[0].text
    return message

st.title("ChatGPT ChatBot With Streamlit and OpenAI")

user_input = st.text_input("Write here")

if user_input:
    output = api_calling(user_input)
    output = output.lstrip("\n")

    st.write("Bot Response:", output)
