import logging
from typing import List

from fairest.core.plugins import collect_document_reporting_rules, collect_section_reporting_rules
from fairest.models import Report, DocumentModel, Request, Response

reporting_logger = logging.getLogger('fairest.reporting')


def flatten_reports(reports) -> List[Report]:
    """
    Convenience function to flatten lists which may contain lists of reports to a list with only reports.
    """
    result = []
    for report in reports:
        if type(report) is list:
            for sub_report in report:
                result.append(sub_report)
        else:
            result.append(report)
    return result


def run_reporting(document: DocumentModel, request: Request, response: Response) -> Response:
    reporting_logger.info('Collecting document reporting rules.')
    document_rules = collect_document_reporting_rules()
    reporting_logger.debug(f'Number of rules collected: {len(document_rules)}')
    for rule_type in document_rules:
        reporting_logger.info(f'Starting rule: {str(rule_type)}')
        rule = rule_type(request=request)
        reports = rule.run_document_rule(request, document)
        add_report(reports, response)
    reporting_logger.info('Collecting section reporting rules.')
    section_rules = collect_section_reporting_rules()
    reporting_logger.debug(f'Number of rules collected: {len(section_rules)}')
    for section in document:
        reporting_logger.info(f'Starting section: {section.get_text()}')
        for rule_type in section_rules:
            reporting_logger.info(f'Starting rule: {str(rule_type)}')
            rule = rule_type(request=request)
            reports = rule.run_section_rule(request, document, section)
            add_report(reports, response)
    return response


def add_report(reports, response):
    response.add_report(reports)
    if reports is not None:
        if type(reports) == list:
            reporting_logger.info(f'Added {len(reports)} reports.')
            for report in reports:
                reporting_logger.debug(f"Report: {report.title}, {report.rule_id}")
        else:
            reporting_logger.info(f'Added 1 report.')
            reporting_logger.debug(f"Report: {reports.title}, {reports.rule_id}")
