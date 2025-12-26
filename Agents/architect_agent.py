from Prompts import architect_prompt
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

import json

from langchain.chat_models import init_chat_model

import os

from Loggers import logger

from Prompts import *
from State import *

load_dotenv()

llm = init_chat_model(os.getenv("LLM_MODEL"), temperature=0, max_retries = 10)

def architech_agent(state: dict) -> dict:

    plan = state["plan"]

    response = llm.with_structured_output(TaskPlan).invoke(architect_prompt(plan.model_dump_json()))

    if response is None:

        logger.debug("The architect error didn't work.") 

    
    data = response.model_dump_json()

    data = json.loads(data)

    pretty_json = json.dumps(data, indent=4)

    logger.info("Logging output from the Architect_Agent:\n%s", pretty_json)  

    response.plan = plan
    return {'task_plan': response}