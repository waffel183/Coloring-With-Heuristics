from distutils.core import setup
import py2exe

setup(
    options = {
            "py2exe":{
                "dll_excludes": ["MSVCP90.dll", "libopenblas.BNVRK7633HSX7YVO2TADGR4A5KEKXJAW.gfortran-win_amd64.dll"]
            }
    },
    console=['BacktrackingSearch.py'])
