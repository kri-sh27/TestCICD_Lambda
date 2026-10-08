# from extra_utils import get_lambda_message

from src.lambda_function import lambda_handler


def test_lambda_function():
    # from lambda_function import lambda_handler
    event = {}
    context = {}
    response = lambda_handler(event, context)
    assert response['statusCode'] == 200
    assert 'String from another module' in response['body']