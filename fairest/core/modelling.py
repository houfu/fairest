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


import logging
from typing import Optional

from fairest.core.rules import collect_document_model_rules
from fairest.models import DocumentModel

modelling_logger = logging.getLogger('fairest.modelling')


def get_model(request) -> Optional[DocumentModel]:
    modelling_logger.info('Collecting document modelling rules.')
    model_rules = collect_document_model_rules()
    modelling_logger.debug(f'Number of rules collected: {len(model_rules)}')
    result: Optional[DocumentModel] = None
    for rule_class in model_rules:
        modelling_logger.info(f'Starting rule: {str(rule_class)}')
        rule = rule_class(request=request)
        if rule.check_document(request.request_body, result):
            modelling_logger.info(f"Document has passed rule {str(rule_class)}'s check")
            result = rule.run_document_model_rule(request)
            modelling_logger.info(f"Result after running rule: {result}")
    modelling_logger.info(f"Finished running rules with final result: {result}")
    return result
