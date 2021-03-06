from drf_yasg.utils import swagger_auto_schema

from demo_project.api.swagger.responses import generic_error_response, get_cars_200_response, get_trucks_200_response


def get_cars_auto_schema():
    return swagger_auto_schema(
        operation_id='get_cars',
        operation_summary='Lists cars',
        operation_description='Lists all cars available in this test-project',
        responses={
            '200': get_cars_200_response(),
            '400': generic_error_response('Bad input. Error: {e}.'),
            '401': generic_error_response('Bad credentials. Error: {e}.'),
            '500': generic_error_response('Unexpected error raised when ...'),
        },
    )


def get_other_cars_auto_schema():
    return swagger_auto_schema(
        operation_id='get_other_cars',
        operation_summary='Lists other cars',
        operation_description='Lists all other cars available in this test-project',
        responses={
            '200': get_cars_200_response(),
            '400': generic_error_response('Bad input. Error: {e}.'),
            '401': generic_error_response('Bad credentials. Error: {e}.'),
            '500': generic_error_response('Unexpected error raised when ...'),
        },
    )


def get_trucks_auto_schema():
    return swagger_auto_schema(
        operation_id='get_trucks',
        operation_summary='Lists trucks',
        operation_description='Lists all trucks available in this test-project',
        responses={
            '200': get_trucks_200_response(),
            '400': generic_error_response('Bad input. Error: {e}.'),
            '401': generic_error_response('Bad credentials. Error: {e}.'),
            '500': generic_error_response('Unexpected error raised when ...'),
        },
    )


def get_other_trucks_auto_schema():
    return swagger_auto_schema(
        operation_id='get_other_trucks',
        operation_summary='Lists other trucks',
        operation_description='Lists all other trucks available in this test-project',
        responses={
            '200': get_trucks_200_response(),
            '400': generic_error_response('Bad input. Error: {e}.'),
            '401': generic_error_response('Bad credentials. Error: {e}.'),
            '500': generic_error_response('Unexpected error raised when ...'),
        },
    )
