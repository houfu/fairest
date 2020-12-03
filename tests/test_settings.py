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
