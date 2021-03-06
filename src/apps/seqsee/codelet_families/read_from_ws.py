# Copyright (C) 2011, 2012  Abhijit Mahabal

# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this
# program.  If not, see <http://www.gnu.org/licenses/>

from farg.codelet import CodeletFamily
from apps.seqsee.subspaces.choose_item_to_focus_on import SubspaceSelectObjectToFocusOn

class CF_ReadFromWS(CodeletFamily):
  @classmethod
  def Run(cls, controller):
    choice = SubspaceSelectObjectToFocusOn(controller)
    controller.stream.FocusOn(choice)
