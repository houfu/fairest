from typing import Optional

from fairest.core.plugins import collect_document_model_rules
from fairest.models import DocumentModel


def get_model(request) -> Optional[DocumentModel]:
    model_rules = collect_document_model_rules()
    result: Optional[DocumentModel] = None
    for rule_class in model_rules:
        rule = rule_class(request=request)
        if rule.check_document(request.request_body, result):
            result = rule.run_document_model_rule(request)
    return result
