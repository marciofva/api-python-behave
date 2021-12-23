import yaml
from datetime import datetime
from datetime import timedelta
import uuid


def load_yaml(yaml_path):
    with open(yaml_path) as stream:
        return yaml.safe_load(stream)


def get_current_date():
    s = datetime.now() - timedelta(seconds=1)
    dt = s.astimezone().isoformat()
    return dt


def get_future_date():
    s = datetime.now() + timedelta(weeks=24)
    dt = s.astimezone().isoformat()
    return dt


def get_base_header():
    base_header = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive'
    }
    return base_header


def get_header_json():
    base_header = {
        'Content-type': 'application/json',
        'Connection': 'keep-alive'
    }
    return base_header


def generate_random_id():
    uid = uuid.uuid4()
    return uid.hex[1:]


def generate_uuid():
    return str(uuid.uuid4())


def print_logs(response, context):
    print('\n\n', '-' * 130)
    print(f'>>> URL ({response.request.method}): {response.url}')
    print(">>> PAYLOAD: ", str(context.payload).replace("'", '"')) if response.request.method == "POST" else None
    print(f'>>> RESPONSE: {str(response.text).encode("ascii", "ignore").decode("ascii")}')
    print('-' * 130, '\n\n')
