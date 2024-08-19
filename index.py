import pathlib
from pathlib import Path
import platform
from platform import python_version
import uuid

_FSTDM_INFO_ = {}
_FSTDM_INFO_["PythonVersion"] = python_version()
_FSTDM_INFO_["OSName"] = platform.system()
_FSTDM_INFO_["OSRelease"] = platform.release()
_FSTDM_INFO_["OSUserPath"] = Path.home()
_FSTDM_INFO_["OSCurrentPath"] = pathlib.Path().resolve()
_FSTDM_INFO_["OSUuidNode"] = hex(uuid.getnode())[2:]

for item in _FSTDM_INFO_.items():
    print("{} :\t{}".format(item[0],item[1]))


