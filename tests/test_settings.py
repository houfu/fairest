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

from fairest.core.settings import Settings
from fairest.plugins_core import BasicDocxModelRule


def test_settings_class():
    assert Settings()


def test_disabled_rules():
    test_settings = Settings()
    assert len(test_settings.disabled_rules) == 0
    test_settings = Settings(disable_rules=['BasicDocxModelRule'])
    assert BasicDocxModelRule in test_settings.disabled_rules
    assert len(test_settings.disabled_rules) == 1
    test_settings = Settings(enable_rules_only=['BasicDocxModelRule'])
    assert [BasicDocxModelRule] not in test_settings.disabled_rules


def test_from_yaml():
    # Test custom settings
    yaml_file = """
    disable_rules:
        - BasicDocxModelRule
    model_spacy: en_core_web_lg
    development: True
    rules_options:
        SentenceLengthRule:
            length: 50
    """
    test_settings = Settings.from_YAML(yaml_file)
    assert test_settings.disabled_rules == [BasicDocxModelRule]
    assert test_settings.model_spacy == 'en_core_web_lg'
    assert test_settings.development is True
    assert test_settings.rules_options == {
        'SentenceLengthRule': {'length': 50}
    }
    test_settings_copy = Settings.from_YAML(test_settings.to_YAML())
    assert test_settings.disabled_rules == test_settings_copy.disabled_rules
    assert test_settings.model_spacy == test_settings_copy.model_spacy
    assert test_settings.development is test_settings_copy.development
    assert test_settings.rules_options == test_settings_copy.rules_options
    test_settings = Settings.from_YAML('A: 1')
    assert test_settings.disabled_rules == []
    assert test_settings.model_spacy == 'en_core_web_sm'
    assert test_settings.development is False
    assert test_settings.rules_options == {}
    assert test_settings.to_YAML() == ''
