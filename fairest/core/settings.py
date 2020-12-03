from typing import List, Optional, Dict, Any, Union

from fairest.core.rules import collect_all_rules
from fairest.models import RuleClass, Request


class Settings:
    def __init__(self, disable_rules: Optional[List[str]] = None, enable_rules_only: Optional[List[str]] = None,
                 model_spacy: str = 'en_core_web_sm', development=True, rules_options: Optional[Dict[str, Any]] = None):

        if enable_rules_only is None:
            enable_rules_only = []
        if disable_rules is None:
            disable_rules = []

        def get_disabled_rules(enable, disable) -> List[RuleClass]:
            all_rules = collect_all_rules()
            if len(enable) > 0:
                return [rule for rule in all_rules if rule.get_rule_name() not in enable]
            else:
                return [rule for rule in all_rules if rule.get_rule_name() in disable]

        self.disabled_rules = get_disabled_rules(enable_rules_only, disable_rules)
        self.model_spacy = model_spacy
        self.development = development
        if rules_options is None:
            rules_options = {}
        self.rules_options = rules_options

    def create_request(self, body: Union[str, bytes], **kwargs) -> Request:
        return Request(body, self.disabled_rules, self.rules_options, **kwargs)
