import datetime


class FiscalDay:
    """Class for financial report start and end date in format DD-MM"""
    def __init__(self, day, month):
        """Construct financial report date (day: int, month: int)"""
        self.date = datetime.date(2, month, day)

    def __repr__(self):
        """Return financial report date with leading zeros.
        >>> FiscalDay(1.1) -> '01.01'
        >>> FiscalDay(28.2) -> '28.02'
        >>> FiscalDay(31.12) -> '31.12'
        """
        return ('0' if self.date.day < 10 else '') + str(self.date.day) + '.' \
            + ('0' if self.date.month < 10 else '') + str(self.date.month)


def make_fiscal_day_from_string(date_string):
    """Return from string FiscalDay """
    date_parts = date_string.split('.')
    return FiscalDay(int(date_parts[0]), int(date_parts[1]))
