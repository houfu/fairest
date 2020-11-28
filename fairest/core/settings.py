from typing import List, Dict, Any, Union

from fairest.core.rules import collect_all_rules
from fairest.models import RuleType, Request


class Settings:
    disable_rules: List[str] = []
    enable_rules_only: List[str] = []
    model_spacy: str = 'en_core_web_sm'
    development: bool = True
    rules_options: Dict[str, Any] = {}

    @property
    def disabled_rules(self) -> List[RuleType]:
        """Property to compile a list of disabled rules from the enable and disable rules settings."""
        all_rules = collect_all_rules()
        if len(self.enable_rules_only) > 0:
            return [rule for rule in all_rules if rule.get_rule_name() not in self.enable_rules_only]
        else:
            return [rule for rule in all_rules if rule.get_rule_name() in self.disable_rules]


def init_settings() -> Settings:
    return Settings()
