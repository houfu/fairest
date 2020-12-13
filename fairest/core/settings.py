from typing import List, Optional, Dict, Any, Union

import yaml

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

    @classmethod
    def from_YAML(cls, yaml_file):
        """Load settings from a yaml file. Input can be text or a file."""
        raw_settings = yaml.load(yaml_file, Loader=yaml.SafeLoader)
        return Settings(disable_rules=raw_settings.get('disable_rules'),
                        enable_rules_only=raw_settings.get('enable_rules'),
                        model_spacy=raw_settings.get('model_spacy', 'en_core_web_sm'),
                        development=raw_settings.get('development', False),
                        rules_options=raw_settings.get('rules_options')
                        )
