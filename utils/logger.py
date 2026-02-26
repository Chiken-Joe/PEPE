import logging
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api")

def log_request(response: requests.Response, *args, **kwargs):
    logger.info(f"Request: {response.request.method} {response.request.url}")
    if response.request.body:
        logger.info(f"Request body: {response.request.body}")
    logger.info(f"Response status: {response.status_code}")
    logger.info(f"Response body: {response.text}")