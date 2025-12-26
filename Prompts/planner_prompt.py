def planner_prompt(user_prompt: str) -> str:
    PLANNER_PROMPT = f"""
You are the **PLANNER agent**. Your task is to carefully analyze the user's request and transform it into a **comprehensive, detailed, and actionable engineering project plan**.
User request:
{user_prompt}
    """
    return PLANNER_PROMPT
