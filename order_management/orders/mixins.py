from rest_framework import status
from rest_framework.response import Response

class BaseApiMixin:
    """
    JSend format responses
    https://github.com/omniti-labs/jsend
    """

    def success_response(self, data=None, status=status.HTTP_200_OK):
        """
        Type: success
        Description: All went well, and (usually) some data was returned.
        Required Keys: status, data
        """
        response_data = {"status": "success", "data": data}
        return Response(data=response_data, status=status)

    def fail_response(self, data=None, status=status.HTTP_400_BAD_REQUEST):
        """
        Type: fail
        Description: There was a problem with the data submitted,
        or some pre-condition of the API call wasn't satisfied
        Required Keys: status, data
        """
        response_data = {"status": "fail", "data": data}
        return Response(data=response_data, status=status)

    def error_response(
        self,
        message="",
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        code=None,
        data=None,
    ):
        """
        Type: error
        Description: An error occurred in processing the request,
        i.e. an exception was thrown
        Required Keys: status, message
        Optional Keys: code, data
        """
        response_data = {"status": "error", "message": message}
        if code:
            response_data["code"] = code
        if data:
            response_data["data"] = data
        return Response(response_data, status=status)

    def redirect_response(self, url="", status_code=status.HTTP_301_MOVED_PERMANENTLY):
        """
        Provide a redirect response with a given URL and status code
        """
        response = Response(status=status_code)
        response["Location"] = url
        return response
