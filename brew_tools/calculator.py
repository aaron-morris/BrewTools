""" This module contains calculation and conversion functions to support working with home brewing recipes.

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

from numbers import Number
from decimal import Decimal, ROUND_HALF_UP
from brew_tools import grains


def to_decimal(value, decimal_places=3):
    """ Convert the provided number value to a decimal with the specified number of decimal places.

    :param value: The number value to convert.
    :param decimal_places: The number of decimal places in the converted value.  (Default is 3)
    :return: The converted value.
    :raises:
        TypeError when either argument is not a valid numeric type.
        ValueError when decimal_places is less than zero.
    """

    if not isinstance(value, Number):
        raise TypeError('"value" argument must be a number.')

    if not isinstance(decimal_places, int):
        raise TypeError('"decimal_places" argument must be a non-negative integer')

    value = Decimal(value)

    if decimal_places > 0:
        precision_format = '.' + ('0' * (decimal_places - 1)) + '1'
    elif decimal_places == 0:
        precision_format = '1'
    else:
        raise ValueError('"decimal_places" argument must be a non-negative integer.')

    return Decimal(value.quantize(Decimal(precision_format), rounding=ROUND_HALF_UP))


def convert_sg_to_ppg(gravity):
    """ Convert a specific gravity value to a points/pound/gallon (ppg) value.
    Example:  Specific gravity of 1.035 = 35 ppg

    :param gravity: The gravity value to convert.
    :return: The calculated ppg value.
    """

    return int((to_decimal(gravity) - 1) * 1000)


def convert_lbs_to_lbs_ounces(lbs):
    """ Convert the provided float value representing pounds into a tuple representing pounds and ounces
     Example:  1.5 lbs == (1 lb, 8 oz)

    :param lbs:  The float representing pounds.
    :return:  The tuple representing lbs and ounces.
    """

    pounds = int(lbs)
    ounces = to_decimal((Decimal(lbs) - pounds) * 16, 1)
    return pounds, ounces


def calc_total_gravity_points(specific_gravity, gallons):
    """ Calculate the total gravity points from the provided SG and volume values.

    :param specific_gravity: The specific gravity.
    :param gallons: The total volume, in gallons.
    :return: The total number of gravity points based on the SG and volume.
    """

    return to_decimal(convert_sg_to_ppg(specific_gravity) * gallons)


def calc_expected_yield(max_yield, efficiency):
    """ Calculates the expected yield of a grain based on the maximum yield and the expected mash efficiency.

    :param max_yield:  The maximum possible yield in gravity points.
    :param efficiency: The expected conversion efficiency of the grain in the mash.
    :return:  The calculated expected yield.
    """

    return to_decimal(max_yield * efficiency)


def calc_grain_qty(total_gravity_points, grain_ratio, expected_yield):
    """ Calculates the necessary quantity of a grain based on its ratio within the recipe and its expected mash yield.

    :param total_gravity_points:
    :param grain_ratio:
    :param expected_yield:
    :return:
    """

    return to_decimal(total_gravity_points * Decimal(grain_ratio) / Decimal(expected_yield))


def calc_grain_bill(target_gravity, volume, grain_list):
    """ Calculate a recipe's grain bill based on the target gravity, target volume, and the recipe's grain list.

    :param target_gravity: The target original gravity.
    :param volume: The target post-boil volume.
    :param grain_list: The list of grains in the recipe as a tuple:  (grain_name, ratio, efficiency)
    :return:
    """

    total_gravity_points = calc_total_gravity_points(target_gravity, volume)

    return tuple(
        (grain,
         convert_lbs_to_lbs_ounces(
             calc_grain_qty(
                 total_gravity_points,
                 ratio,
                 calc_expected_yield(convert_sg_to_ppg(grains.max_gravities[grain]), efficiency))))
        for (grain, ratio, efficiency) in grain_list
    )


def calc_total_grain_weight(grain_bill):
    """ Calculates the total weight of a grain bill by summing the weights of the grains.

    :param grain_bill:  The grain bill to sum.
    :return:  The total sum of the individual grain weights
    """

    total_weight = Decimal('0')
    for (grain, weight) in grain_bill:
        total_weight += Decimal(weight)

    return to_decimal(total_weight)


def calc_mash_water_volume(water_grist_ratio, grains_weight):
    """  Calculates the volume of mash water necessary to achieve the target water-to_grist ratio

    :param water_grist_ratio:  The target ratio to achieve.
    :param grains_weight:  The amount of grains in the grist.
    :return:  The amount of water necessary to achieve the ratio.
    """
    
    return to_decimal(water_grist_ratio * grains_weight)