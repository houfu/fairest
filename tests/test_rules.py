from fairest.core.rules import flatten_rules, collect_all_rules, get_options_list
from fairest.models import BaseRule
from fairest.plugins_core import SentenceLengthRule


def test_flatten_rules():
    result = flatten_rules([BaseRule()])
    assert len(result) == 1
    result = flatten_rules([BaseRule(), [BaseRule(), BaseRule()]])
    assert len(result) == 3


def test_collect_all_rules(mocker):
    patch_1 = mocker.patch('fairest.core.rules.pm.hook.get_document_model_rules')
    patch_1.return_value = [BaseRule]
    patch_2 = mocker.patch('fairest.core.rules.pm.hook.get_document_rules')
    patch_2.return_value = []
    patch_3 = mocker.patch('fairest.core.rules.pm.hook.get_section_rules')
    patch_3.return_value = [BaseRule, [BaseRule, BaseRule]]
    assert len(collect_all_rules()) == 4


def test_get_options_list(mocker):
    patch = mocker.patch('fairest.core.rules.collect_all_rules')
    patch.return_value = [BaseRule, SentenceLengthRule]
    result = get_options_list()
    assert list(result.keys()) == ['BaseRule', 'SentenceLengthRule']
    assert result['BaseRule'] == []
    assert len(result['SentenceLengthRule']) == len(SentenceLengthRule.describe_properties())
