#  Copyright (c) 2021.  Ang Hou Fu
#
#  This software is licensed under the The MIT License.
#  You should have received a copy of the license terms with the software.
#  Otherwise, you can find the text here: https://opensource.org/licenses/MIT
#
#
#  This software is licensed under the The MIT License.
#  You should have received a copy of the license terms with the software.
#  Otherwise, you can find the text here: https://opensource.org/licenses/MIT
#

from typing import Union, Dict, Any, Optional, List

from .Rule import RuleClass


class Request:
    def __init__(self, body: Union[str, bytes], disable: Optional[List[RuleClass]] = None,
                 rules_options: Optional[Dict[str, Any]] = None, **kwargs):
        """
        Request is the input to the fairest system.

        :param body: The text to be processed. It can be a string, or bytes (files).
        :param kwargs: All other keyword arguments are stored in a field custom.
        """
        self.disable = [] if disable is None else disable
        self.request_body = body
        self.rules_options = rules_options if rules_options is not None else {}
        self.options = kwargs

    def is_string(self) -> bool:
        """Convenience method to determine if the request body is a file or a string."""
        return isinstance(self.request_body, str)

    def is_rule_disabled(self, key: Union[str, RuleClass]) -> bool:
        """Convenience method to determine if a rule is disabled by the Request. """
        if isinstance(key, str):
            return key in [rule.get_rule_name() for rule in self.disable]
        else:
            return key in self.disable
