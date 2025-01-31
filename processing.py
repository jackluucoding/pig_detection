# processing.py

from questions import questions, MAX_SCORE
from scoring import get_risk_category, format_recommendation
from state_utils import embed_state, extract_state

def process_message(user_input: str, history: list) -> list:
    """
    Process a single user message in the context of the existing chat history.
    - history is a list of messages in the format:
      [{"role": "user"|"assistant", "content": "..."}]
    - We embed the "state" in the last assistant message that contained it.
    """

    # 1) Find the last state (if any) by scanning from the end for an assistant message
    state = None
    for i in range(len(history) - 1, -1, -1):
        if history[i]["role"] == "assistant":
            potential_state = extract_state(history[i]["content"])
            if potential_state is not None:
                state = potential_state
                break

    # 2) If no state found, initialize it
    if not state:
        state = {
            "question_index": 0,
            "total_score": 0,
            "triggered_flags": []
        }

    q_index = state["question_index"]

    # 3) If we're still asking questions, interpret user_input as yes/no
    if q_index < len(questions):
        user_input_lower = user_input.strip().lower()
        if user_input_lower in ["yes", "no"]:
            # Update state based on yes/no
            if user_input_lower == "yes":
                state["total_score"] += questions[q_index]["weight_yes"]
                state["triggered_flags"].append(questions[q_index]["red_flag"])

            state["question_index"] += 1
            q_index = state["question_index"]

            # Move to next question or finalize
            if q_index < len(questions):
                next_question = questions[q_index]["text"]
                bot_response = f"Question {q_index+1}: {next_question}"
                bot_response += embed_state(state)
            else:
                # All questions answered -> compute results
                total_score = state["total_score"]
                triggered_flags = state["triggered_flags"]
                risk_percent = (total_score / MAX_SCORE) * 100
                risk_level = get_risk_category(risk_percent)
                recommendation = format_recommendation(risk_level)

                bot_response = (
                    "All questions answered! Here are your results:\n\n"
                    f"**Total Score**: {total_score}/{MAX_SCORE} ({risk_percent:.1f}%)\n"
                    f"**Risk Level**: {risk_level}\n\n"
                )
                if triggered_flags:
                    bot_response += "**Red Flags Identified**:\n"
                    for flag in triggered_flags:
                        bot_response += f" - {flag}\n"
                else:
                    bot_response += "No major red flags identified based on your answers.\n"

                bot_response += (
                    "\n**Recommendation**:\n"
                    f"{recommendation}\n\n"
                    "Thank you for using the Pig Butchering Scam Assessment!"
                )
        else:
            # Invalid response -> ask the same question again
            same_question = questions[q_index]["text"]
            bot_response = (
                f"Please answer 'yes' or 'no'.\n\n"
                f"Question {q_index+1}: {same_question}"
            )
            bot_response += embed_state(state)
    else:
        # If we're here, all questions are already answered
        # The user might keep typing. We can just respond politely.
        bot_response = (
            "All questions have been answered. "
            "If you want to start over, please refresh or restart."
        )

    # 4) Update the conversation
    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": bot_response})

    return history
