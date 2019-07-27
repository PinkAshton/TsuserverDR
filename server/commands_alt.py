# tsuserver3, an Attorney Online server
#
# Copyright (C) 2016 argoneus <argoneuscze@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
This module holds all the commands that are either deprecated or are meant to
act as aliases for existing commands in commands.py
"""

def do_command(command, client, arg):
    """
    Wrapper function for alt/deprecated commands.
    """
    source = client.server.commands
    adapted_command = 'ooc_cmd_{}'.format(command)
    function = getattr(source, adapted_command)
    function(client, arg)

def ooc_cmd_allow_iniswap(client, arg):
    """
    Deprecated for /can_iniswap.
    """
    do_command('can_iniswap', client, arg)

def ooc_cmd_delete_areareachlock(client, arg):
    """
    Deprecated for /passage_clear.
    """
    do_command('passage_clear', client, arg)

def ooc_cmd_restore_areareachlock(client, arg):
    """
    Deprecated for /passage_restore.
    """
    do_command('passage_restore', client, arg)

def ooc_cmd_toggle_areareachlock(client, arg):
    """
    Deprecated for /can_passagelock.
    """
    do_command('can_passagelock', client, arg)

def ooc_cmd_toggleglobal(client, arg):
    """
    Deprecated for /toggle_global.
    """
    do_command('toggle_global', client, arg)

def ooc_cmd_toggle_rollp(client, arg):
    """
    Deprecated for /can_rollp.
    """
    do_command('can_rollp', client, arg)

def ooc_cmd_toggle_rpgetarea(client, arg):
    """
    Deprecated for /can_rpgetarea.
    """
    do_command('can_rpgetarea', client, arg)

def ooc_cmd_toggle_rpgetareas(client, arg):
    """
    Deprecated for /can_rpgetareas.
    """
    do_command('can_rpgetareas', client, arg)