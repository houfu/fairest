from typing import Union


class Request:

    def __init__(self, body: Union[str, bytes], **kwargs):
        """
        Request is the input to the fairest system.

        :param body: The text to be processed. It can be a string, or bytes (files).
        :param kwargs: All other keyword arguments are stored in a field custom.
        """
        self.request_body = body
        self.options = kwargs

    def isString(self):
        """Convenience method to determine if the request body is a file or a string."""
        return isinstance(self.request_body, str)
