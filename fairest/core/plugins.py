from typing import List

import pluggy

from fairest import hook_specs, plugins_core
from fairest.models import DocumentModelRuleType, DocumentRuleType, SectionRuleType


def get_plugin_manager():
    plugin_manager = pluggy.PluginManager('fairest')
    plugin_manager.add_hookspecs(hook_specs)
    plugin_manager.load_setuptools_entrypoints("fairest")
    plugin_manager.register(plugins_core)
    return plugin_manager


pm = get_plugin_manager()


def flatten_rules(rules):
    """
    Convenience function to flatten lists which may contain lists of rules to a list with only rules.
    """
    result = []
    for rule in rules:
        if type(rule) is list:
            for sub_rule in rule:
                result.append(sub_rule)
        else:
            result.append(rule)
    return result


def collect_document_reporting_rules() -> List[DocumentRuleType]:
    return flatten_rules(pm.hook.get_DocumentRules())


def collect_section_reporting_rules() -> List[SectionRuleType]:
    return flatten_rules(pm.hook.get_SectionRules())


def collect_document_model_rules() -> List[DocumentModelRuleType]:
    return flatten_rules(pm.hook.get_DocumentModelRules())
