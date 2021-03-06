import ctypes as ctypes
from ctype import wintypes s wintypes
import os
import sys



kernel32 = ctypes.WinDLL('kernel32',use_last_error=True)
advapi32 = ctypes.WinDLL('advapi32',use_last_error=True)

ERROR_INVALID_FUNCTION = 0x0001
ERROR_FILE_NOT_FOUND = 0x0002
ERROR_PATH_NOT_FOUND = 0x0003
ERROR_ACCESS_DENIED = 0x0005
ERROR_SHARING_VIOLATION = 0x0020

SE_FILE_OBJECT = 1
OWNER_SECURITY_INFORMATION = 0x00000001
GROUP_SECURITY_INFORMATION = 0x00000002
DACL_SECURITY_INFORMATION = 0x00000004
SACL_SECURITY_INFORMATION = 0x00000008
LABEL_SECURITY_INFROMATION = 0x00000010

_DEFAULT_SECURITY_INFORMATION = (OWNER_SECURITY_INFORMATION |
        GROUP_SECURITY_INFORMATION | DACL_SECURITY_INFORMATION |
        LABEL_SECURITY_INFROMATION)

LPDWORD = ctypes.POINTER(wintypes.DWORD)
SE_OBJECT_TYPE = wintypes.DWORD
SECURITY_INFORMATION = wintypes.DWORD

class SID_NAME_USE(wintypes.DWORD):
    _sid_types = dict(enumerate('''
    User Group Domain Alias WellKnownGroup DeletedAccount
    invalid Unknown Computer Label'''.split(),1))

    def __init__(self,value=None):
        if value is not None:
            if value not in self.sid_types:
                raise ValueError('invalid SID type')
            wintype.DWORD.__init__(value)
    def __str__(self):
        if self.value not in self._sid_types:
            raise ValueError('invalid SID type')
        return self._sid_types[self.value]
    
    def __repr__(self):
        return 'SID_NAME_USE(%s)' % self.value

PSID_NAME_USE = ctypes.POINTER(SID_NAME_USE)

class PLOCAL(wintypes.LPVOID):
    _need_free = False
    def __init__(self, value=None, needs_free=False):
        super(PSID, self).__init__
