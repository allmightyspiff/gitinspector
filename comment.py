# coding: utf-8
#
# Copyright © 2012 Ejwa Software. All rights reserved.
#
# This file is part of gitinspector.
#
# gitinspector is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gitinspector is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with gitinspector. If not, see <http://www.gnu.org/licenses/>.

__comment_begining__ = {"java": "/*", "c": "/*", "cpp": "/*", "h": "/*", "hpp": "/*", "py": "\"\"\"", "glsl": "/*",
                        "rb": "=begin", "js": "/*", "sql": "/*", "xml": "<!--"}

__comment_end__ = {"java": "*/", "c": "*/", "cpp": "*/", "h": "*/", "hpp": "*/", "py": "\"\"\"", "glsl": "*/",
                   "rb": "=end", "js": "*/", "sql": "*/", "xml": "-->"}

__comment__ = {"java": "//", "c": "//", "cpp": "//", "h": "//", "hpp": "//", "py": "#", "glsl": "//",
               "rb": "#", "js": "//", "sql": "--"}

def is_comment_begining(extension, string):
	if __comment_begining__.get(extension, None) != None:
		return string.strip().startswith(__comment_begining__[extension])
	else:
		return False

def is_comment_end(extension, string):
	if __comment_end__.get(extension, None) != None:
		return string.strip().endswith(__comment_end__[extension])
	else:
		return False

def is_comment(extension, string):
	if __comment__.get(extension, None) != None:
		return string.strip().startswith(__comment__[extension])
	else:
		return False
