from rest_framework.views import exception_handler
from rest_framework.exceptions import NotAuthenticated, ValidationError, NotFound


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:

        if isinstance(exc, NotAuthenticated):
            response.data = {
                "success": False,
                "message": "Please log in to continue.",
                "errors": {}
            }

        elif isinstance(exc, ValidationError):
            response.data = {
                "success": False,
                "message": "Please correct the errors.",
                "errors": response.data
            }

        elif isinstance(exc, NotFound):
            response.data = {
                "success": False,
                "message": "The requested resource was not found.",
                "errors": {}
            }

        else:
            response.data = {
                "success": False,
                "message": "Something went wrong.",
                "errors": response.data
            }

    return response