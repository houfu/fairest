#  Copyright (c) 2020. Ang Hou Fu
#
#  This file is part of Fairest.
#
#  Fairest is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  any later version.
#
#   Fairest is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Fairest.  If not, see <https://www.gnu.org/licenses/>.

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
