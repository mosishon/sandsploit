#CopyRight Apache-2.0
#Powered By Python 3.X
#Author : @Aμιρ-0x0 (AMJ)

import os
import sys 
import readline
import glob
import re


def lists(path):
    #apps = os.listdir("/usr/bin/")   
        
    commands = ['help','use','run','exit','banner','nano','update','upgrade','version','python','bash','su','sudo','cd','ls','listener','RSMaker','list']
    """
    Lists folder contents
    """
    if path.startswith(os.path.sep):
        # absolute path
        basedir = os.path.dirname(path)
        content = os.listdir(basedir)
        # add back the parent
        
        content = [os.path.join(basedir, d) for d in contents]
        contents = content + commands 
    else:
        # relative path
        content = os.listdir(os.curdir)
        contents = content + commands 
    return contents


def completer(text, state):

    options = [x for x in lists(text) if x.startswith(text)]
    return options[state]

readline.set_completer(completer)

readline.parse_and_bind('tab: complete')
readline.set_completer_delims(' \t\n`~!@#$%^&*()-=+[{]}\\|;:\'",<>?')
