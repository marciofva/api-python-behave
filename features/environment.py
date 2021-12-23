from services.helpers.utils import load_yaml
from services.rest_service import Rest_Service
import os


def before_all(context):
    context.behave_env = str(os.environ.get("ENV")).upper()
    print(f'>>>> ENVIRONMENT: {context.behave_env}\n')


def before_scenario(context, scenario):
    context.token = "Bearer " + Rest_Service().get_token(context)


def before_feature(context, feature):
    env = 'DEVELOP' if context.behave_env not in ['LOCAL', 'DEVELOP', 'PRODUCTION'] else context.behave_env

    context.credentials = load_yaml(os.getcwd() + "/configs/env_" + env.lower() + ".yaml")['ROOT_PATH']
