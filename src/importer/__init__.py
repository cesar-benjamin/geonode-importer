#########################################################################
#
# Copyright (C) 2022 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################
import os

project_dir = os.path.dirname(os.path.abspath(__file__))

# VERSION = ''
__version__ = '1.0.6-alpha2'
__author__ = "César Benjamin"
__email__ = "mathereall@gmail.com"
__url__ = "https://github.com/cesar-benjamin/geonode-importer"
default_app_config = "importer.apps.ImporterConfig"
