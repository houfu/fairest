import fairest
from fairest.plugins_core.BasicDOCX import BasicDocxModelRule
from fairest.plugins_core.BasicText import BasicTextModelRule
from fairest.plugins_core.DocumentStatisticsRule import DocumentStatisticsRule
from fairest.plugins_core.SentenceLengthRule import SentenceLengthRule


@fairest.hook_impl(trylast=True)
def get_document_model_rules():
    return [BasicTextModelRule, BasicDocxModelRule]


@fairest.hook_impl
def get_document_rules():
    return [DocumentStatisticsRule]


@fairest.hook_impl
def get_section_rules():
    return [SentenceLengthRule]
