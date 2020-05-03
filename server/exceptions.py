# TsuserverDR, a Danganronpa Online server based on tsuserver3, an Attorney Online server
#
# Copyright (C) 2016 argoneus <argoneuscze@gmail.com> (original tsuserver3)
# Current project leader: 2018-20 Chrezm/Iuvee <thechrezm@gmail.com>
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
# along with this program. If not, see <http://www.gnu.org/licenses/>.

class TsuserverException(Exception):
    def __init__(self, message='', code=None):
        self.message = message
        if code:
            self.code = code

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        if self.message != other.message:
            return False
        return True

class ClientError(TsuserverException):
    class UnauthorizedError(TsuserverException):
        pass

class AreaError(TsuserverException):
    pass

class ArgumentError(TsuserverException):
    pass

class ServerError(TsuserverException):
    class ServerFileNotFoundError(TsuserverException):
        pass

    class MusicNotFoundError(TsuserverException):
        pass

    class MusicInvalid(TsuserverException):
        # Remove, kept for backwards compatibility
        pass

    class MusicInvalidError(TsuserverException):
        pass

    class YAMLNotFoundError(TsuserverException):
        pass

    class YAMLInvalidError(TsuserverException):
        pass

class PartyError(TsuserverException):
    pass

class PlayerGroupError(TsuserverException):
    class UserAlreadyPlayerError(TsuserverException):
        pass

    class UserAlreadyInvitedError(TsuserverException):
        pass

    class UserAlreadyLeaderError(TsuserverException):
        pass

    class UserInAnotherGroupError(TsuserverException):
        pass

    class UserInNoGroupError(TsuserverException):
        pass

    class UserNotInvitedError(TsuserverException):
        pass

    class UserNotPlayerError(TsuserverException):
        pass

    class UserNotLeaderError(TsuserverException):
        pass

    class GroupIsEmptyError(TsuserverException):
        pass

    class GroupIsFullError(TsuserverException):
        pass

    class GroupDoesNotTakeInvitationsError(TsuserverException):
        pass

    class ManagerTooManyGroupsError(TsuserverException):
        pass

    class ManagerDoesNotManageGroupError(TsuserverException):
        pass

    class ManagerInvalidIDError(TsuserverException):
        pass

class SteptimerError(TsuserverException):
    class TimerTooLowError(TsuserverException):
        pass

    class TimerTooHighError(TsuserverException):
        pass

    class InvalidMinTimerValueError(TsuserverException):
        pass

    class InvalidFiringIntervalError(TsuserverException):
        pass

    class InvalidTimestepLengthError(TsuserverException):
        pass

    class AlreadyStartedSteptimerError(TsuserverException):
        pass

    class NotStartedSteptimerError(TsuserverException):
        pass

    class AlreadyPausedSteptimerError(TsuserverException):
        pass

    class NotPausedSteptimerError(TsuserverException):
        pass

    class AlreadyTerminatedSteptimerError(TsuserverException):
        pass

    class ManagerTooManySteptimersError(TsuserverException):
        pass

    class ManagerDoesNotManageSteptimerError(TsuserverException):
        pass

    class ManagerInvalidIDError(TsuserverException):
        pass

class ZoneError(TsuserverException):
    class AreaConflictError(TsuserverException):
        pass

    class AreaNotInZoneError(TsuserverException):
        pass

    class WatcherConflictError(TsuserverException):
        pass

    class WatcherNotInZoneError(TsuserverException):
        pass

class GameError(TsuserverException):
    class UserAlreadyPlayerError(TsuserverException):
        pass

    class UserAlreadyInvitedError(TsuserverException):
        pass

    class UserAlreadyLeaderError(TsuserverException):
        pass

    class UserInAnotherGameError(TsuserverException):
        pass

    class UserInNoGameError(TsuserverException):
        pass

    class UserNotInvitedError(TsuserverException):
        pass

    class UserNotPlayerError(TsuserverException):
        pass

    class UserNotLeaderError(TsuserverException):
        pass

    class GameIsEmptyError(TsuserverException):
        pass

    class GameIsFullError(TsuserverException):
        pass

    class GameDoesNotTakeInvitationsError(TsuserverException):
        pass

    class ManagerTooManyGameError(TsuserverException):
        pass

    class ManagerDoesNotManageGameError(TsuserverException):
        pass

    class ManagerInvalidIDError(TsuserverException):
        pass