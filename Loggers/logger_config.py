import logging

logging.basicConfig(
    filename="Loggers/debugging.log",
    level = logging.DEBUG,
    filemode= "w"
)

for noisy_logger in ['httpx', 'httpcore', 'groq', 'urllib3', 'asyncio']:
    logging.getLogger(noisy_logger).setLevel(logging.ERROR)

logger = logging.getLogger("project_logger")
