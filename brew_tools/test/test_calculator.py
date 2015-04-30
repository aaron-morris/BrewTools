""" This module contains PyTest unit tests for the 'calculator' module.

    (c) Aaron Morris, 2015
    morris7200@gmail.com

    Licensed under the GNU General Public License, v3

    GPL Notice:  This file is part of BrewTools.

    BrewTools is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    BrewTools is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with BrewTools.  If not, see <http://www.gnu.org/licenses/>
"""

import pytest
from decimal import Decimal
from brew_tools import calculator


def test__to_decimal__converts():
    # test with default arg value
    assert calculator.to_decimal(0.9876) == Decimal('0.988')
    assert calculator.to_decimal(1.001) == Decimal('1.001')
    assert calculator.to_decimal(99.12345) == Decimal('99.123')
    assert calculator.to_decimal(999.6789) == Decimal('999.679')

    # test with all arg values
    assert calculator.to_decimal(0.9876, 0) == Decimal('1')
    assert calculator.to_decimal(1.001, 2) == Decimal('1.00')
    assert calculator.to_decimal(99.12345, 4) == Decimal('99.1235')
    assert calculator.to_decimal(999.6789, 5) == Decimal('999.67890')


def test__to_decimal__raises_errors():
    pytest.raises(ValueError, calculator.to_decimal, 1.001, -1)
    pytest.raises(TypeError, calculator.to_decimal, 'hello', 1)
    pytest.raises(TypeError, calculator.to_decimal, 1.001, 1.2)
    pytest.raises(TypeError, calculator.to_decimal, 1.001, 'hello')


def test__convert_sg_to_ppg__converts():
    assert calculator.convert_sg_to_ppg(1.001) == 1
    assert calculator.convert_sg_to_ppg(1.050) == 50
    assert calculator.convert_sg_to_ppg(1.123) == 123


def test__convert_lbs_to_lbs_ounces__converts():
    assert calculator.convert_lbs_to_lbs_ounces(8.5) == (8, 8)
    assert calculator.convert_lbs_to_lbs_ounces(12.33) == (12, Decimal('5.3'))
    assert calculator.convert_lbs_to_lbs_ounces(0.67) == (0, Decimal('10.7'))


def test__calc_total_gravity_points__calculates():
    assert calculator.calc_total_gravity_points(1.001, 1) == 1
    assert calculator.calc_total_gravity_points(1.050, 2.5) == 125
    assert calculator.calc_total_gravity_points(1.123, 10) == 1230


def test__calc_expected_yield__calculates():
    assert calculator.calc_expected_yield(100, .7) == 70
    assert calculator.calc_expected_yield(35, 1) == 35
    assert calculator.calc_expected_yield(17, .1) == Decimal('1.7')


def test__calc_grain_qty__calculates():
    assert calculator.calc_grain_qty(300, .75, 25) == Decimal('9.000')
    assert calculator.calc_grain_qty(200, 1, 35) == Decimal ('5.714')


def test__calc_grain_bill__calculates():

    grain_recipe = (
        ('American Wheat', .67, .68),
        ('American Pale (2-Row)', .33, .68)
    )
    grain_bill = calculator.calc_grain_bill(1.052, 5.5, grain_recipe)

    wheat_weight = calculator.convert_lbs_to_lbs_ounces(calculator.to_decimal(52 * 5.5 * .67 / (38 * .68), 3))
    pale_weight = calculator.convert_lbs_to_lbs_ounces(calculator.to_decimal(52 * 5.5 * .33 / (37 * .68), 3))
    assert grain_bill == (('American Wheat', wheat_weight), ('American Pale (2-Row)', pale_weight))


def test__calc_total_grain_weight__calculates():
    grain_bill = (('grain1', 1.1), ('grain2', 2.2), ('grain3', 3.3))
    assert calculator.calc_total_grain_weight(grain_bill) == Decimal('6.6')

    grain_bill = (('grain1', 1.1234), ('grain2', 2.2345), ('grain3', 3.3456))
    assert calculator.calc_total_grain_weight(grain_bill) == Decimal('6.704')


def test__calc_mash_water_volume__calculates():
    assert calculator.calc_mash_water_volume(1.25, 7.75) == Decimal('9.688')
    assert calculator.calc_mash_water_volume(1.5, 8) == Decimal('12')


def test__calc_strike_temp__calculates():
    assert calculator.calc_strike_temp(1, 70, 104) == Decimal('110.8')
    assert calculator.calc_strike_temp(2, 70, 152) == Decimal('160.2')


def test__calc_infusion_volume__calculates():
    assert calculator.calc_infusion_volume(104, 140, 210, 8, 8) == Decimal('4.937')
    assert calculator.calc_infusion_volume(140, 158, 210, 12.9, 8) == Decimal('5.019')


def test__calc_grain_absorption__calculates():
    assert calculator.calc_grain_absorption(1, .08) == Decimal('.08')
    assert calculator.calc_grain_absorption(4.5, .2) == Decimal('0.9')