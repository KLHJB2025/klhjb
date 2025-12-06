# app.py: This is your website's main code
import streamlit as st
from google import genai
import os 

# --- 1. Set up the website look and title ---
st.title("🗣️ Your Gemini Protocol Website")
st.write("Interact with the AI model you built in Google AI Studio.")

# Create a box for the user to type in
user_input = st.text_input("Enter your request here:", key="input_prompt")

# Create a button that starts the action
if st.button("Get AI Response"):
    if user_input:
        # --- 2. Initialize the AI Client SECURELY ---
        # The code looks for the key in the Streamlit Secrets (an environment variable)
        try:
            api_key_safe = os.environ.get("GEMINI_API_KEY")
            if not api_key_safe:
                st.error("Deployment Error: API Key not found. Please set the GEMINI_API_KEY secret.")
                st.stop()
                
            client = genai.Client(api_key=api_key_safe)
        except Exception as e:
            st.error("Could not start the AI connection. Check your setup.")
            st.stop()

        # --- 3. Call the AI and wait for the response ---
        with st.spinner('The AI is processing your protocol...'): 
            try:
                # Calls the Gemini model
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=user_input
                )
                # --- 4. Display the answer to the user ---
                st.subheader("✅ AI Protocol Result:")
                st.info(response.text) 
            except Exception as e:
                st.error(f"Something went wrong while getting the answer: {e}")
    else:
        st.warning("Please type a request first!")
