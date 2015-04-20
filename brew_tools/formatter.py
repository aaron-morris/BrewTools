""" This module contains formatting functions for outputting data from the calculator.

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


def format_grain_bill_line(grain_bill_line):
    """ Formats a single line in a grain bill as follows:  Name:  1bs, oz
    Example:  'American Wheat:  1 lbs, 8 oz'

    :param grain_bill_line: A tuple of grain bill info:  (Name, (lbs, oz))
    :return:  A formatted string containing the grain info.
    """

    grain, lbs_ounces = grain_bill_line
    lbs, ounces = lbs_ounces

    return '{}:  {} lbs, {} oz'.format(grain, lbs, ounces)


def format_grain_bill(grain_bill):
    """ Formats a grain bill as tuple of formatted strings, one per line in the grain bill.

    :param grain_bill:  The grain bill information.
    :return:  The tuple of formatted grain bill strings
    """

    return tuple(format_grain_bill_line(grain_bill_line) for grain_bill_line in grain_bill)
