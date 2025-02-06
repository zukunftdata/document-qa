import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("Mini")
st.write(
    "Ask a question about anything – GPT will try to answer!"
    )

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
# openai_api_key = st.text_input("OpenAI API Key", type="password")
openai_api_key = st.secrets["my_api_key"]
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:

    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # Let the user upload a file via `st.file_uploader`.
    # uploaded_file = st.file_uploader(
    #     "Upload a document (.txt or .md)", type=("txt", "md")
    # )

    # Ask the user for a question via `st.text_area`.
    question = st.text_area(
        "Ask away, and see if I can answer you:",
        # placeholder="Can you give me a short summary?",
        # disabled=not uploaded_file,
    )

    if question:

        # Process the uploaded file and question.
        # document = uploaded_file.read().decode()
        messages = [
            {
                "role": "user",
                "content": f"{question}",
            }
        ]

        # Generate an answer using the OpenAI API.
        stream = client.chat.completions.create(
            model="o1-mini",
            messages=messages,
            stream=True,
        )

        # Stream the response to the app using `st.write_stream`.
        st.write_stream(stream)
