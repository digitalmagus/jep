from distutils import sysconfig
from commands.util import is_osx, is_windows
import os

def get_python_libs():
    """
    Get the shared library names for embedding jep.

    See python-config
    """
    if is_windows():
	    return ['python' + sysconfig.get_config_var('VERSION')]

    return ['python' + sysconfig.get_config_var('VERSION'), 'dl']

def get_python_linker_args():
    if is_osx() or is_windows():
        return []
    return ['-L{0}'.format(sysconfig.get_config_var('LIBDIR'))]
	

def get_python_include():
    if is_windows():
        return ['{0}\\Lib\\site-packages\\numpy\\core\\include\\'.format(os.environ.get('PYTHONHOME'))]
    return []