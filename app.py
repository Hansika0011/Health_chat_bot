import streamlit as st
from transformers import pipeline

# Load AI Model (BERT-based Question Answering)
chatbot_model = pipeline("question-answering", model="deepset/bert-base-cased-squad2")

# Chatbot logic
def healthcare_chatbot(user_input):
    user_input = user_input.lower().strip()
    
    # If input is too short, make it a complete question
    if "cold" in user_input:
        user_input = "What should I do if I have a cold?"
    elif "fever" in user_input:
        user_input = "How can I treat a fever at home?"
    elif "cough" in user_input:
        user_input = "When should I see a doctor for a cough?"
    
    # Rule-based responses for common healthcare queries
    if "fever" in user_input:
        return "If you have a fever, rest, stay hydrated, and monitor your temperature. If it persists, consult a doctor."
    elif "headache" in user_input:
        return "Try drinking water and resting. If the headache persists, consult a doctor."
    elif "appointment" in user_input:
        return "Would you like me to schedule an appointment with a doctor?"
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly. If you have concerns, consult your doctor."
    else:
        # AI-generated response for general health questions
        context = "Common healthcare-related scenarios include symptoms of colds, flu, and allergies, along with medication guidance and appointment scheduling."
        response = chatbot_model(question=user_input, context=context)
        return response['answer']

# Streamlit Web App
def main():
    st.title("💬 Healthcare Assistant Chatbot")
    st.write("Ask me about symptoms, medications, or appointments!")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        st.write(f"**{message['role']}**: {message['content']}")

    user_input = st.text_input("How can I assist you today?")

    if st.button("Submit"):
        if user_input.strip():
            st.session_state.messages.append({"role": "User", "content": user_input})
            response = healthcare_chatbot(user_input)
            st.session_state.messages.append({"role": "Healthcare Assistant", "content": response})
            st.write(f"**Healthcare Assistant**: {response}")

if __name__ == "__main__":
    main()
