import streamlit as st
from chatbot import query_response

CSS_FIXED_INPUT = """
<style>
h1 {
    text-align: center;
}
div[data-testid="chat-input-container"] {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 999; /* Ensure it stays above other elements */
    background-color: white; /* Match background color */
    padding: 10px 0 10px 0; /* Add some vertical padding */
    box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow above input */
}
.main {
    padding-bottom: 80px; 
}
</style>
"""

def main():
    st.set_page_config(
        page_title="RUL Prediction Chatbot",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.markdown(CSS_FIXED_INPUT, unsafe_allow_html=True)

    st.title("🔋 RUL Metrics Chatbot (Powered by Ollama) 🔋")
    st.markdown("---")

    chat_container = st.container()
    input_placeholder = st.empty()

    # Initializing the chat history
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant",
                                         "content": "Hello! I am the RUL expert chatbot. How can I explain the final "
                                                    "model metrics to you?"}]

    # Displaying chat messages in the main container
    with chat_container:
        st.info("You can ask the LLM to explain the RMSE, the RUL error, or the EOL cycles.")
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

    with input_placeholder:
        if prompt := st.chat_input("Ask a question about the metrics..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.rerun()

    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        prompt_to_process = st.session_state.messages[-1]["content"]

        with st.spinner(" Thinking..."):
            response = query_response(prompt_to_process)

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()


if __name__ == "__main__":
    main()

