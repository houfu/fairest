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
