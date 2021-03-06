#!/usr/bin/python3
'''
   Copyright 2017 Mirko Brombin (brombinmirko@gmail.com)

   This file is part of ElementaryPython.

    ElementaryPython is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    ElementaryPython is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ElementaryPython.  If not, see <http://www.gnu.org/licenses/>.
'''

import gi
from datetime import datetime
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
#Components
import headerbar as hb
import welcome as wl

API_KEY = "cb3a6fe9d9284af79a13661ff6191ea6"
headers = {'X-Auth-Token':API_KEY, 'X-Response-Control': 'minified'}
stylesheet = """
    @define-color colorPrimary #249C5F;
    @define-color textColorPrimary #f2f2f2;
    @define-color textColorPrimaryShadow #197949;
""";

class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Messages")

        hbar = hb.Headerbar()
        self.set_titlebar(hbar)

        self.welcome = wl.Welcome()

        self.add(self.welcome)

