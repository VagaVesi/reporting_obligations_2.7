import datetime

from src.fiscal_day import make_fiscal_day_from_string


class Entity:
    """A collection of fiscal year entries and submitted reports

    fiscalYears - a dict containing:
    report_period_start -- FiscalDay
    report_period_end -- FiscalDay
    entry_start -- datetime.date
    entry_start -- datetime.date
    """

    def __init__(self, created_at):
        self.created_at = created_at
        self.fiscalYears = []
        self.reports = []

    def __str__(self):
        """Return entity fiscal years entries"""
        return str(self.fiscalYears)

    def add_fiscal_year(self, report_period_start_string, report_period_end_string, entry_start):
        """Add new valid reporting period entry and end last reporting period entry"""
        if self.fiscalYears.__len__() > 0:
            self.fiscalYears[-1]['entry_end'] = entry_start
        self.fiscalYears.append({
            'report_period_start': make_fiscal_day_from_string(report_period_start_string),
            'report_period_end': make_fiscal_day_from_string(report_period_end_string),
            'entry_start': entry_start,
            'entry_end': None
        })

    def add_fiscal_years(self, report_period_entries):
        """Add list of reporting periods."""
        sorted_entries = sorted(report_period_entries)
        for entry in sorted_entries:
            self.add_fiscal_year(entry.report_period_end, entry.entry_start)

    def add_report(self, xbrl_id, report_type, report_start, report_end):
        self.reports.append({
            'xbrl_id': xbrl_id,
            'report_type': report_type,
            'report_start': report_start,
            'report_end': report_end
        })


