from typing import Union, Dict, Any, Optional


class Request:

    def __init__(self, body: Union[str, bytes], disable: Optional[Dict[str, Any]] = None, **kwargs):
        """
        Request is the input to the fairest system.

        :param body: The text to be processed. It can be a string, or bytes (files).
        :param kwargs: All other keyword arguments are stored in a field custom.
        """
        self.disable: Dict[str, Any] = {} if disable is None else disable
        self.request_body = body
        self.options = kwargs

    def is_string(self) -> bool:
        """Convenience method to determine if the request body is a file or a string."""
        return isinstance(self.request_body, str)

    def is_rule_disabled(self, key: str) -> bool:
        """Convenience method to determine if a rule is disabled by the Request. """
        return key in self.disable
