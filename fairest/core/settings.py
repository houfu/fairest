from typing import List, Optional, Dict, Any, Union

import yaml

from fairest.core.rules import collect_all_rules
from fairest.models import RuleClass, Request

RULES_OPTIONS = 'rules_options'

DEVELOPMENT = 'development'

MODEL_SPACY = 'model_spacy'

ENABLE_RULES = 'enable_rules'

DISABLE_RULES = 'disable_rules'

default_model_spacy = 'en_core_web_sm'


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
        return Settings(disable_rules=raw_settings.get(DISABLE_RULES),
                        enable_rules_only=raw_settings.get(ENABLE_RULES),
                        model_spacy=raw_settings.get(MODEL_SPACY, default_model_spacy),
                        development=raw_settings.get(DEVELOPMENT, False),
                        rules_options=raw_settings.get(RULES_OPTIONS)
                        )

    def to_YAML(self) -> str:
        """Returns the current settings in a YAML format for convenient persistence"""
        raw_settings = {}
        if len(self.disabled_rules) > 0:
            raw_settings[DISABLE_RULES] = [rule_class.get_rule_name() for rule_class in self.disabled_rules]
        if self.model_spacy is not default_model_spacy:
            raw_settings[MODEL_SPACY] = self.model_spacy
        if self.development:
            raw_settings[DEVELOPMENT] = self.development
        if self.rules_options:
            raw_settings[RULES_OPTIONS] = self.rules_options
        return yaml.dump(raw_settings) if raw_settings != {} else ""
