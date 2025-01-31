# state_utils.py

import json
import re

def embed_state(state: dict) -> str:
    """
    Embed the state dictionary into the assistant message as a hidden tag <STATE>...</STATE>.
    We'll parse this out on the next call.
    """
    return f"\n<STATE>{json.dumps(state)}</STATE>"

def extract_state(message_content: str) -> dict:
    """
    Parse the state out of the message content (hidden in <STATE>...</STATE>).
    If not found or invalid, returns None.
    """
    pattern = r"<STATE>(.*?)</STATE>"
    match = re.search(pattern, message_content, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except:
            return None
    return None
