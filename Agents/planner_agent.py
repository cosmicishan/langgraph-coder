from Prompts import planner_prompt
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

import json

from langchain.chat_models import init_chat_model

from Loggers import logger

import os

from Prompts import *
from State import *

load_dotenv()

llm = init_chat_model(os.getenv("LLM_MODEL"), temperature=0, max_retries = 10)

def planner_agent(state: dict) -> dict:

    user_prompt = state["user_prompt"]

    response = llm.with_structured_output(Plan).invoke(planner_prompt(user_prompt))

    if response is None:

        logger.error("The planner agent didn't sent any response.")

    data = response.model_dump_json()

    data = json.loads(data)

    pretty_json = json.dumps(data, indent=4)

    logger.info("Logging output from the Planner_Agent:\n%s", pretty_json)  

    return {"plan": response}