
HISTFILE = '.jep'

import traceback
import jep
from jep import *

try:
    import readline

    try:
        import os
        HISTFILE = '%s/.jep' % (os.environ['HOME'])
        if(not os.access(HISTFILE, os.W_OK)):
            os.open(HISTFILE, os.O_CREAT)
        readline.read_history_file(HISTFILE)
    except:
        traceback.print_exc()
        pass
except:
    print """
    No readline available.
    You may want to set the LD_PRELOAD environment variable, see the
    README file for details. Ignore this if you're running on Windows.

    i.e.: export LD_PRELOAD=/usr/lib/libpython2.3.so.1.0 """


PS1 = ">>> "
PS2 = "... "


def prompt(jep):
    line = raw_input(PS1)
    while(1):
        ran = True
        try:
            ran = jep.eval(line)
        except:
            traceback.print_exc()

        try:
            if(ran):
                line = raw_input(PS1)
            else:
                line = raw_input(PS2)
        except(EOFError):
            break


if(__name__ == '__main__'):
    Jep = findClass('jep.Jep')
    jep = Jep(True)
    
    try:
        prompt(jep)
    except:
        pass

    print ''
    jep.close()

    if('readline' in dir()):
        readline.write_history_file(HISTFILE)
