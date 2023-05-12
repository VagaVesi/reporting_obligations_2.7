import unittest
from datetime import datetime

from src.entity import Entity


class TestEntity(unittest.TestCase):

    def test_entity_create_empty(self):
        """Entity created"""
        simple_entity = Entity(datetime(2019, 9, 3))
        self.assertEqual(simple_entity.created_at, datetime(2019, 9, 3), 'incorrect creation date')

    def test_entity_add_one_fiscal_year_entry(self):
        """Entity default fiscal period is overwrited
        """
        simple_entity = Entity(datetime(2019, 9, 3))
        simple_entity.add_fiscal_year('01.01', '31.12', datetime(2019, 9, 3))
        self.assertEqual(simple_entity.created_at, datetime(2019, 9, 3), 'incorrect creation date')
        self.assertEqual(str(simple_entity.fiscalYears[-1]['report_period_start']), '01.01', 'incorrect FY start ')
        self.assertEqual(str(simple_entity.fiscalYears[-1]['report_period_end']), '31.12', 'incorrect FY end')
        self.assertEqual(simple_entity.fiscalYears[-1]['entry_start'], datetime(2019, 9, 3), 'incorrect entry start')
        self.assertEqual(simple_entity.fiscalYears[-1]['entry_end'], None, 'incorrect entry end')


if __name__ == '__main__':
    unittest.main(verbosity=2)
