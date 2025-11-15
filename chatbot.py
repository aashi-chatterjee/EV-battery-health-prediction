import requests


#Metric and Formatting Functions
def final_rul_metrics():
    return {
        'Final_RMSE_Ah': 0.1935,
        'Final_MAE_Ah': 0.1554,
        'True_EOL_Cycle': 242,
        'Predicted_EOL_Cycle': 19,
        'RUL_Error_Cycles': -223
    }


def format_metrics(metrics):
    return (
        f"Final Model Performance (Unseen B18):\n"
        f"- Capacity Prediction RMSE: {metrics['Final_RMSE_Ah']:.4f} Ah\n"
        f"- Capacity Prediction MAE: {metrics['Final_MAE_Ah']:.4f} Ah\n"
        f"- True End-of-Life (EOL) Cycle (Capacity <= 1.40 Ah): {metrics['True_EOL_Cycle']}\n"
        f"- Predicted EOL Cycle: {metrics['Predicted_EOL_Cycle']}\n"
        f"- RUL Prediction Error: {metrics['RUL_Error_Cycles']} cycles"
    )


OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_response(full_prompt, model_name="llama3"):
    try:
        payload = {
            "model": model_name,
            "prompt": full_prompt,
            "stream": False
        }
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()

        response_data = response.json()
        return response_data.get("response", "Error: LLM response key not found.")

    except requests.exceptions.RequestException as e:
        return (
            f"ERROR: Could not connect to Ollama at {OLLAMA_URL}. "
            f"Detail: {e}"
        )


def query_response(user_query, model_name="llama3"):
    metrics = final_rul_metrics()
    metrics_string = format_metrics(metrics)

    system_prompt = (
        "You are a highly restrictive, expert AI assistant specializing in Lithium-ion Battery RUL metrics. "
        "Your absolute, non-negotiable instruction is: **You MUST answer the user's question based ONLY on the metrics provided in the 'Metrics Context' section.** "
        "If the user asks a question about any external data (like 'Tesla', 'mileage', 'new battery data', or 'generalization'), "
        "you MUST state clearly that the model's scope is strictly limited to the provided B18 experiment data and that you cannot answer the question."
        "If you can answer, be helpful, concise, and use clear language (e.g., explain that a negative RUL error means the model predicted failure too early)."
    )

    full_prompt = (
        f"{system_prompt}\n\n"
        f"--- Metrics Context ---\n"
        f"{metrics_string}\n\n"
        f"--- User Query ---\n"
        f"User: {user_query}"
    )

    llm_response = generate_response(full_prompt, model_name=model_name)
    return llm_response


def start_chatbot():
    print("--- 🤖 RUL Metrics Expert Chatbot Initiated ---")
    print("Ask me about the model's RMSE, RUL Error, or True EOL Cycle.")
    print("Type 'exit' or 'quit' to end the session.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['exit', 'quit']:
            print("\nChatbot: Thank you for reviewing the RUL project metrics. Goodbye! 👋")
            break

        if not user_input.strip():
            continue

        chatbot_response = query_response(user_input)

        print(f"Chatbot: {chatbot_response}\n")


if __name__ == "__main__":
    start_chatbot()
