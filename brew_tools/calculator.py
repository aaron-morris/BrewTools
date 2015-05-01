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
    :return:  The tuple representing pounds and ounces.
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
    """ Calculates the expected mash yield of a grain based on the maximum yield and the expected mash efficiency.

    :param max_yield:  The maximum possible yield in gravity points.
    :param efficiency: The expected conversion efficiency of the grain in the mash.
    :return:  The calculated expected yield.
    """

    return to_decimal(max_yield * efficiency)


def calc_grain_qty(total_gravity_points, grain_ratio, expected_yield):
    """ Calculates the necessary quantity of a grain based on its ratio within the recipe and its expected mash yield.

    :param total_gravity_points:  The recipe's total number of gravity points.
    :param grain_ratio:  The ratio of gravity points provided by the grain compared to the total gravity points.
    :param expected_yield:  The expected yield of the grain in the mash.
    :return:  The grain's total recipe weight, in pounds.
    """

    return to_decimal(total_gravity_points * Decimal(grain_ratio) / Decimal(expected_yield))


def calc_grain_bill(target_gravity, volume, grain_list):
    """ Calculate a recipe's grain bill based on the target gravity, target volume, and the recipe's grain list.

    :param target_gravity: The target original gravity.
    :param volume: The target post-boil volume, in gallons.
    :param grain_list: The list of grains in the recipe as a tuple:  (grain_name, ratio, efficiency)
    :return:  The recipe's grain bill as a tuple: (grain_name, weight_in_pounds)
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
    :return:  The total sum of the individual grain weights, in pounds.
    """

    total_weight = Decimal('0')
    for (grain, weight) in grain_bill:
        total_weight += Decimal(weight)

    return to_decimal(total_weight)


def calc_mash_water_volume(water_grist_ratio, grains_weight):
    """  Calculates the volume of mash water necessary to achieve the target water-to_grist ratio

    :param water_grist_ratio:  The target ratio to achieve in quarts/pounds.
    :param grains_weight:  The amount of grains in the grist, in pounds.
    :return:  The amount of water necessary to achieve the ratio, in quarts.
    """
    
    return to_decimal(water_grist_ratio * grains_weight)


def calc_strike_temp(water_grist_ratio, initial_temp, target_temp):
    """ Calculates the necessary strike temperature of the mash water.

    :param water_grist_ratio: The water-to-grist ratio as quarts/pound.
    :param initial_temp: The current temperature of the grains (at room temperature), in degrees Fahrenheit.
    :param target_temp: The target temperature of the mash after the grains are added, in degrees Fahrenheit.
    :return:  The necessary temperature of the strike water to achieve the target temperature, in degrees Fahrenheit.
    """

    water_grist_ratio = Decimal(water_grist_ratio)
    initial_temp = Decimal(initial_temp)
    target_temp = Decimal(target_temp)
    thermodynamic_constant = Decimal('0.2')

    return to_decimal((thermodynamic_constant / water_grist_ratio) * (target_temp - initial_temp) + target_temp)


def calc_infusion_volume(initial_temp, target_temp, infusion_temp, water_in_mash, grain_in_mash):
    """ Calculates the volume of water necessary to increase the mash temperature to the target temperature.

    :param initial_temp:  The current temperature of the mash, in degrees Fahrenheit.
    :param target_temp:  The target temperature of the mash, in degrees Fahrenheit.
    :param infusion_temp:  The temperature of the infusion water being added to the mash, in degrees Fahrenheit.
    :param water_in_mash:  The amount of water in the mash, in quarts.
    :param grain_in_mash:   The amount of grains in the mash, in pounds.
    :return:  The amount of water (in quarts) to add to the mash to achieve the target temperature.
    """

    initial_temp = Decimal(initial_temp)
    target_temp = Decimal(target_temp)
    infusion_temp = Decimal(infusion_temp)
    water_in_mash = Decimal(water_in_mash)
    grain_in_mash = Decimal(grain_in_mash)
    thermodynamic_constant = Decimal('0.2')

    return to_decimal((target_temp - initial_temp) * (thermodynamic_constant * grain_in_mash + water_in_mash) / (infusion_temp - target_temp))


def calc_grain_absorption(grain_weight, absorption_rate):
    """ Calculates the approximate volume of water absorbed by the spent grains in the mash.

    :param grain_weight:  The weight of the grains in the mash.
    :param absorption_rate:  The rate of absorption, in gallons per pound.
    :return:  The volume of absorbed water, in gallons.
    """

    return to_decimal(Decimal(grain_weight) * Decimal(absorption_rate))


def calc_evaporation_loss(boil_length_minutes, evaporation_gph):
    """ Calculates the expected volume of water loss due to evaporation during the boil.

    :param boil_length_mins:  The duration of the boil, in minutes.
    :param evaporation_rate:   The expected rate of evaporation, in gallons-per-hour.
    :return:  The volume of expected water loss, in gallons.
    """

    return to_decimal(Decimal(boil_length_minutes) / 60 * Decimal(evaporation_gph))


def calc_shrinkage_loss(initial_volume):
    """ Calculates the expected volume of water loss due to shrinkage during wort cooling.

    :param initial_volume:  The initial volume of water, pre-cooling.
    :return:  The expected volume of water loss due to shrinkage.
    """

    constant_shrinkage_rate = Decimal(.04)
    return to_decimal(Decimal(initial_volume) * constant_shrinkage_rate)


def calc_required_water_volume(
        target_volume, grain_weight, absorption_rate, equipment_losses, boil_length_minutes, evaporation_gph, trub_loss):

    req_volume = Decimal(target_volume) + Decimal(trub_loss)
    req_volume = req_volume + calc_shrinkage_loss(req_volume)
    req_volume = req_volume + calc_evaporation_loss(boil_length_minutes, evaporation_gph)
    req_volume = req_volume + Decimal(equipment_losses)
    req_volume = req_volume + calc_grain_absorption(grain_weight, absorption_rate)

    return to_decimal(req_volume)