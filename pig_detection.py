import gradio as gr
from processing import process_message, questions, embed_state 

def build_app():
    with gr.Blocks() as demo:
        # Introductory text
        gr.Markdown("## Pig Butchering Detection System")
        gr.Markdown("Click 'Start' to begin the assessment. Then click 'Yes' or 'No' to answer each question.")
        
        # Chatbot component
        chatbot = gr.Chatbot(label="Chat Assessment", type="messages")
        
        # Buttons layout
        with gr.Row():
            start_btn = gr.Button("Start")
        
        with gr.Row():
            yes_btn = gr.Button("Yes", visible=False)
            no_btn = gr.Button("No", visible=False)
        
        with gr.Row():
            clear_btn = gr.Button("Clear", visible=False)  # Initially hidden
        
        # Start function: Begins the assessment
        def start_fn():
            state = {"question_index": 0, "total_score": 0, "triggered_flags": []}
            first_question = f"Question 1: {questions[0]['text']}"
            first_message = first_question + embed_state(state)
            initial_history = [{"role": "assistant", "content": first_message}]
            return (
                initial_history,          # Update chatbot
                gr.update(visible=True),  # Show Yes button
                gr.update(visible=True),  # Show No button
                gr.update(visible=False), # Hide Start button
                gr.update(visible=True)   # Show Clear button
            )
        
        # Yes button handler
        def respond_yes(chat_history):
            updated_history = process_message("Yes", chat_history)
            return updated_history
        
        # No button handler
        def respond_no(chat_history):
            updated_history = process_message("No", chat_history)
            return updated_history
        
        # Clear function: Resets the interface
        def clear_fn():
            return (
                [],                       # Clear chatbot
                gr.update(visible=False), # Hide Yes button
                gr.update(visible=False), # Hide No button
                gr.update(visible=True),  # Show Start button
                gr.update(visible=False)  # Hide Clear button
            )
        
        # Event handlers
        start_btn.click(
            fn=start_fn,
            inputs=[],
            outputs=[chatbot, yes_btn, no_btn, start_btn, clear_btn]
        )
        
        yes_btn.click(
            fn=respond_yes,
            inputs=[chatbot],
            outputs=[chatbot]
        )
        
        no_btn.click(
            fn=respond_no,
            inputs=[chatbot],
            outputs=[chatbot]
        )
        
        clear_btn.click(
            fn=clear_fn,
            inputs=[],
            outputs=[chatbot, yes_btn, no_btn, start_btn, clear_btn]
        )
    
    return demo

if __name__ == "__main__":
    demo = build_app()
    demo.launch(share=True)