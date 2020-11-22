from fairest.core.plugins import flatten_rules, collect_all_rules
from fairest.models import BaseRule


def test_flatten_rules():
    result = flatten_rules([BaseRule()])
    assert len(result) == 1
    result = flatten_rules([BaseRule(), [BaseRule(), BaseRule()]])
    assert len(result) == 3


def test_collect_all_rules(mocker):
    patch_1 = mocker.patch('fairest.core.plugins.pm.hook.get_DocumentModelRules')
    patch_1.return_value = [BaseRule()]
    patch_2 = mocker.patch('fairest.core.plugins.pm.hook.get_DocumentRules')
    patch_2.return_value = []
    patch_3 = mocker.patch('fairest.core.plugins.pm.hook.get_SectionRules')
    patch_3.return_value = [BaseRule(), [BaseRule(), BaseRule()]]
    assert len(collect_all_rules()) == 4
