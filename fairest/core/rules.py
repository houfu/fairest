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

from itertools import chain
from typing import List, Dict

import pluggy

from fairest import hook_specs, plugins_core
from fairest.models import DocumentModelRuleClass, DocumentRuleClass, SectionRuleClass, RuleClass, RuleProperty


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
            result.extend(rule)
        else:
            result.append(rule)
    return result


def collect_document_reporting_rules() -> List[DocumentRuleClass]:
    return flatten_rules(pm.hook.get_document_rules())


def collect_section_reporting_rules() -> List[SectionRuleClass]:
    return flatten_rules(pm.hook.get_section_rules())


def collect_document_model_rules() -> List[DocumentModelRuleClass]:
    return flatten_rules(pm.hook.get_document_model_rules())


def collect_all_rules() -> List[RuleClass]:
    return flatten_rules(chain(
        pm.hook.get_document_model_rules(),
        pm.hook.get_document_rules(),
        pm.hook.get_section_rules()
    ))


def get_options_list() -> Dict[str, List[RuleProperty]]:
    result = dict()
    for rule in collect_all_rules():
        result[rule.get_rule_name()] = rule.describe_properties()
    return result
