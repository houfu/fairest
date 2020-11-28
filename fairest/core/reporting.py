import logging
from typing import List, Union

from fairest.core.rules import collect_document_reporting_rules, collect_section_reporting_rules
from fairest.models import Report, DocumentModel, Request, Response

reporting_logger = logging.getLogger('fairest.reporting')


def run_reporting(document: DocumentModel, request: Request, response: Response) -> Response:
    reporting_logger.info('Collecting document reporting rules.')
    document_rules = collect_document_reporting_rules()
    reporting_logger.debug(f'Number of rules collected: {len(document_rules)}')
    for rule_type in document_rules:
        reporting_logger.info(f'Starting rule: {rule_type.get_rule_name()}')
        if not request.isRuleDisabled(rule_type.get_rule_name()):
            rule = rule_type(request=request)
            reports = rule.run_document_rule(request, document)
            add_report(reports, response)
        else:
            reporting_logger.info('Rule was disabled by Request. Pass.')
    reporting_logger.info('Collecting section reporting rules.')
    section_rules = collect_section_reporting_rules()
    reporting_logger.debug(f'Number of rules collected: {len(section_rules)}')
    for section in document:
        reporting_logger.info(f'Starting section: {section.get_text()}')
        for rule_type in section_rules:
            reporting_logger.info(f'Starting rule: {rule_type.get_rule_name()}')
            if not request.isRuleDisabled(rule_type.get_rule_name()):
                rule = rule_type(request=request)
                reports = rule.run_section_rule(request, document, section)
                add_report(reports, response)
            else:
                reporting_logger.info('Rule was disabled by Request. Pass.')
    return response


def add_report(reports: Union[Report, List[Report], None], response: Response):
    """Convenience function to add report to response with logging."""
    response.add_report(reports)
    if reports is not None:
        if type(reports) == list:
            reporting_logger.info(f'Added {len(reports)} reports.')
            for report in reports:
                reporting_logger.debug(f"Report: {report.title}, {report.rule_id}")
        else:
            reporting_logger.info(f'Added 1 report.')
            reporting_logger.debug(f"Report: {reports.title}, {reports.rule_id}")
    else:
        reporting_logger.info('No Reports added.')
