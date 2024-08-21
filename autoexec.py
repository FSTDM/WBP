import importlib
#import machineid
import pathlib
import platform
import uuid
class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
class FSTDM:
    def INIT():
        FSTDM.Info = dotdict()
        Info = FSTDM.Info
#        Info.MachineId = machineid.id()
        Info.OsName = platform.system()
        Info.OsRelease = platform.release()
        Info.PythonVersion = platform.python_version()
        Info.PythonMagicNumber = int.from_bytes(importlib.util.MAGIC_NUMBER[:2],"little")
        Info.PathSep = importlib._bootstrap_external.path_separators[0]
        Info.CurrentPath = str(pathlib.Path().absolute())
        Info.UserPath = str(pathlib.Path.home())
FSTDM.INIT()
print(FSTDM.Info)
