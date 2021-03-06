""" This module contains information about grain/fermentables used in calculations.

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


# gravity values were referenced from BYO magazine website: https://byo.com/resources/grains on 17 APR 2015
max_gravities = {
    'American Black Barley': 1.025,
    'American Black Patent': 1.026,
    'American Chocolate': 1.034,
    'American Crystal 10L': 1.034,
    'American Crystal 20L': 1.034,
    'American Crystal 30L': 1.034,
    'American Crystal 40L': 1.034,
    'American Crystal 60L': 1.034,
    'American Crystal 80L': 1.034,
    'American Crystal 90L': 1.034,
    'American Crystal 120L': 1.034,
    'American Dextrin': 1.033,
    'American Munich': 1.034,
    'American Pale (2-Row)': 1.037,
    'American Pale (6-Row)': 1.035,
    'American Roasted Barley': 1.025,
    'American Special Roast': 1.035,
    'American Victory': 1.034,
    'American Vienna': 1.035,
    'American Wheat': 1.038,
    'American White Wheat': 1.037,
    'Belgian Aromatic': 1.036,
    'Belgian Pale Ale': 1.038,
    'Belgian Biscuit': 1.035,
    'Belgian Candy Sugar': 1.036,
    'Belgian Caramel Pils': 1.030,
    'Belgian Caramunich': 1.033,
    'Belgian Caravienne': 1.034,
    'Belgian Chocolate': 1.033,
    'Belgian De-Bittered Black': 1.030,
    'Belgian Pale': 1.038,
    'Belgian Pilsen': 1.037,
    'Belgian Roasted Wheat': 1.036,
    'Belgian Special B': 1.030,
    'British Amber Malt 35L': 1.032,
    'British Amber Malt 65L': 1.032,
    'British Black Patent': 1.026,
    'British Brown': 1.032,
    'British Cara-Pils Dextrin': 1.033,
    'British Caramalt': 0.00,
    'British Chocolate': 1.034,
    'British Crystal': 1.034,
    'British Dark Crystal': 1.034,
    'British Lager': 1.038,
    'British Maris Otter Pale': 1.038,
    'British Mild Ale': 1.037,
    'British Oat': 1.034,
    'British Pale': 1.038,
    'British Pale Chocolate': 1.034,
    'British Peat Smoked': 1.034,
    'British Roasted Barley': 1.025,
    'British Toasted Pale': 1.038,
    'British Torrified Wheat': 1.036,
    'British Wheat': 1.038,
    'Brown Sugar': 1.046,
    'Brown Sugar (Dark)': 1.046,
    'Candi Sugar (Amber)': 1.036,
    'Candi Sugar (Dark)': 1.036,
    'Corn Sugar': 1.036,
    'Demerara Sugar': 1.041,
    'Dextrose (Glucose)': 1.037,
    'Dry Malt Extract': 1.044,
    'Flaked Barley': 1.032,
    'Flaked Maize': 1.037,
    'Flaked Oats': 1.033,
    'Flaked Rye': 1.036,
    'Flaked Wheat': 1.036,
    'Franco-Belges Kiln Coffee': 0.00,
    'Gambrinus Honey Malt': 1.034,
    'German Aciduated (Sauer)': 1.033,
    'German CaraWheat': 1.035,
    'German CaraAmber': 1.033,
    'German CaraAroma': 1.034,
    'German Carafa I': 1.038,
    'German Carafa II': 1.038,
    'German Carafa III': 1.038,
    'German CaraFoam': 1.033,
    'German CaraHell': 1.034,
    'German CaraMunich I': 1.034,
    'German CaraMunich II': 1.034,
    'German CaraMunich III': 1.034,
    'German CaraRed': 1.033,
    'German Chocolate Rye': 1.030,
    'German Chocolate Wheat': 1.038,
    'German Dark Munich': 1.034,
    'German Dark Wheat': 1.039,
    'German Kolsch': 1.034,
    'German Light Munich': 1.034,
    'German Light Wheat': 1.039,
    'German Melanoidin': 1.033,
    'German Rauch Smoked': 1.037,
    'German Rye': 1.029,
    'German Vienna': 1.035,
    'Grits': 1.037,
    'Honey': 1.032,
    'Invert Sugar': 1.046,
    'Lactose': 1.043,
    'Liquid Malt Extract': 1.036,
    'Lyle\'s Golden Syrup': 1.036,
    'Maple Sap': 1.009,
    'Maple Syrup': 1.030,
    'Molasses': 1.036,
    'Rice Solids': 1.040,
    'Scotmalt Golden Promise': 1.038,
    'Treacle': 1.036,
    'White Table Sugar': 1.046
}