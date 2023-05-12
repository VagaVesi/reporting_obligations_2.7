# coding=utf-8
# This is a sample Python script.
from datetime import datetime

from src.entity import Entity
from src.fiscal_day import FiscalDay

entity_2 = Entity(datetime(2019, 9, 3))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(FiscalDay(12, 1))
    print(entity_2)

