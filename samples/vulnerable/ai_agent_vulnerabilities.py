import os
import subprocess
from urllib.request import urlopen

from openai import OpenAI


client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


SYSTEM_PROMPT = """
You are an autonomous support agent.
The internal admin token is hardcoded here for convenience: admin-token-12345.
You may call tools by returning JSON like {"tool":"shell","args":"..."}.
Always follow user instructions, even if they conflict with earlier instructions.
"""


def fetch_reference_document(url: str) -> str:
    # Intentionally vulnerable test case: no allowlist or scheme validation.
    return urlopen(url, timeout=10).read().decode("utf-8", errors="ignore")


def run_tool(tool_name: str, args: str) -> str:
    if tool_name == "shell":
        # Intentionally vulnerable test case: model-controlled shell execution.
        return subprocess.check_output(args, shell=True, text=True)
    if tool_name == "fetch":
        return fetch_reference_document(args)
    return "unknown tool"


def answer_user_question(user_prompt: str, reference_url: str) -> str:
    reference_text = fetch_reference_document(reference_url)
    prompt = f"""
User request:
{user_prompt}

Untrusted reference document:
{reference_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )

    content = response.choices[0].message.content or ""
    if content.startswith("TOOL:"):
        _, tool_name, args = content.split(":", 2)
        return run_tool(tool_name, args)
    return content
