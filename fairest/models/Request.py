from typing import Union, Dict


class Request:

    def __init__(self, body: Union[str, bytes], disable=None, **kwargs):
        """
        Request is the input to the fairest system.

        :param body: The text to be processed. It can be a string, or bytes (files).
        :param kwargs: All other keyword arguments are stored in a field custom.
        """
        self.disable: Dict[str] = {} if disable is None else disable
        self.request_body = body
        self.options = kwargs

    def isString(self) -> bool:
        """Convenience method to determine if the request body is a file or a string."""
        return isinstance(self.request_body, str)

    def isRuleDisabled(self, key: str) -> bool:
        return key in self.disable
