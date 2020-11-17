from typing import List

from fairest.core.plugins import collect_document_reporting_rules, collect_section_reporting_rules
from fairest.models import Report, DocumentModel, Request, Response


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
    document_rules = collect_document_reporting_rules()
    for rule_type in document_rules:
        rule = rule_type(request=request)
        response.add_report(rule.run_document_rule(request, document))
    section_rules = collect_section_reporting_rules()
    for section in document:
        for rule_type in section_rules:
            rule = rule_type(request=request)
            response.add_report(rule.run_section_rule(request, document, section))
    return response
