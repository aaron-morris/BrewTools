from decimal import Decimal
from brew_tools import formatter

__author__ = 'morris7200@gmail.com'
__copyright_notice__ = """
    This file is part of BrewTools.

    BrewTools is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    BrewTools is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with BrewTools.  If not, see <http://www.gnu.org/licenses/>."""


def test__format_grain_bill__line():
    grain_bill_line = ('American Wheat', (7, Decimal('6.7')))
    formatted_grain_bill = formatter.format_grain_bill_line(grain_bill_line)

    assert formatted_grain_bill == 'American Wheat:  7 lbs, 6.7 oz'


def test__format_grain_bill__formats():

    grain_recipe = (
        ('American Wheat', .67, .68),
        ('American Pale (2-Row)', .33, .68)
    )
    formatted_grain_bill = formatter.format_grain_bill(
        (('American Wheat', (7, Decimal('6.7'))), ('American Pale (2-Row)', (3, Decimal('12.0')))))

    assert formatted_grain_bill == ('American Wheat:  7 lbs, 6.7 oz', 'American Pale (2-Row):  3 lbs, 12.0 oz')
