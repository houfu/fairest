import fairest
from fairest.plugins_core.BasicDOCX import BasicDocxModelRule
from fairest.plugins_core.BasicText import BasicTextModelRule


@fairest.hook_impl(trylast=True)
def get_DocumentModelRules():
    return [BasicTextModelRule, BasicDocxModelRule]
