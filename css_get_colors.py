#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- mode: Python -*-

"""
  ===========================================================================

  Copyright (C) 2017 Emvivre

  This file is part of CSS_GET_COLORS.

  CSS_GET_COLORS is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  CSS_GET_COLORS is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with CSS_GET_COLORS.  If not, see <http://www.gnu.org/licenses/>.

  ===========================================================================
*/
"""

import requests
from lxml import html

r = requests.get('https://www.w3schools.com/cssref/css_colors.asp')
colors = html.fromstring(r.text).cssselect('.w3-table-all tr')
colors = colors[1:]
for c in colors:
    (_, color_name, color_hex, _, _, _, _) = c.text_content().split('\r\n')
    color_hex = color_hex[1:]
    (r, g, b) = (int(color_hex[:2], 16), int(color_hex[2:4], 16), int(color_hex[4:6], 16))
    s = '%-25s #%s \x1b[48;2;%s;%s;%sm                        \x1b[0m' % (color_name, color_hex, r, g, b)
    print s.encode('utf-8')

