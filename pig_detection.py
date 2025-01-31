# app.py

import gradio as gr
from processing import process_message

def build_app():
    with gr.Blocks() as demo:
        gr.Markdown("Pig Butchering Detection Systems")
        gr.Markdown(
            "Type **yes** or **no** to each question. If you're starting, type anything and I'll begin asking."
        )

        chatbot = gr.Chatbot(label="Chat Assessment", type="messages")
        
        with gr.Row():
            user_input = gr.Textbox(
                label="Your answer", 
                placeholder="Type anything to start",
                show_label=True
            )

        with gr.Row():
            submit_btn = gr.Button("Submit")
            clear_btn = gr.Button("Clear")

        def respond_fn(user_message, chat_history):
            """
            user_message: str - new user input
            chat_history: list of {role, content} dicts
            Returns: (updated_history, updated_history, "") 
            where the empty string clears the input
            """
            updated_history = process_message(user_message, chat_history)
            return updated_history, updated_history, ""

        def clear_fn():
            """Reset the conversation and input field."""
            return [], [], ""

        # Handle submit button click
        submit_btn.click(
            fn=respond_fn,
            inputs=[user_input, chatbot],
            outputs=[chatbot, chatbot, user_input],
            scroll_to_output=True
        )

        # Also link the Enter key to submit
        user_input.submit(
            fn=respond_fn,
            inputs=[user_input, chatbot],
            outputs=[chatbot, chatbot, user_input],
            scroll_to_output=True
        )

        # Handle clear button click
        clear_btn.click(
            fn=clear_fn,
            inputs=[],
            outputs=[chatbot, chatbot, user_input],
            scroll_to_output=True
        )

    return demo

if __name__ == "__main__":
    demo = build_app()
    demo.launch(debug=True)
