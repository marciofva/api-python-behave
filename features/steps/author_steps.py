from behave import given, when, then
from hamcrest import equal_to, assert_that
from services.helpers.utils import load_yaml
from services.rest_service import Rest_Service
import os


@given('this author template "{request_template}"')
def step_impl(context, request_template):
    context.payload = load_yaml(os.getcwd() + '/data/author.yaml')[request_template]


@when('I send create author request')
def step_impl(context):
    response = Rest_Service().create_author(context)
    context.status_code = response.status_code
    context.response = response.json()


@given(u'the author id "{author_id}"')
def step_impl(context, author_id):
    context.author_id = author_id


@when('I send retrieve author request')
def step_impl(context):
    response = Rest_Service().get_author(context)
    context.status_code = response.status_code
    context.response = response.json()


@then('I receive status code equals to "{expected_status_code}"')
def step_impl(context, expected_status_code):
    assert_that(context.status_code, equal_to(int(expected_status_code)), "status code")
