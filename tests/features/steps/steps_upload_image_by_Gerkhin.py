import logging
import os
import json
from behave import given, when, then
from src.controllers.pet_controller import PetController

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@given('the pet ID is {pet_id}')
def step_given_pet_id(context, pet_id):
    context.pet_id = int(pet_id)

@given('the metadata is "{metadata}"')
def step_given_metadata(context, metadata):
    context.metadata = metadata

@given('the image path is "{image_path}"')
def step_given_image_path(context, image_path):
    context.image_path = image_path

@when('I upload the image')
def step_when_upload_image(context):
    response = PetController.upload_image(context.pet_id, context.metadata, context.image_path)
    context.response = response
    responseJason = response.json()
    jasonData = json.dumps(responseJason, indent=30)
    # Use logging instead of print
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: " + jasonData)

@then('the response status code should be {status_code}')
def step_then_status_code(context, status_code):
    assert context.response.status_code == int(status_code), \
        f"Expected status code {status_code}, got {context.response.status_code}"
    # Use logging instead of print
    logger.info(f"Verified Status Code: {context.response.status_code}")

@then('the response code should be {response_code}')
def step_then_response_code(context, response_code):
    jsonData = context.response.json()
    assert jsonData['code'] == int(response_code), \
        f"Expected response code {response_code}, got {jsonData['code']}"
    # Use logging instead of print
    logger.info(f"Verified Response Code: {jsonData['code']}")
