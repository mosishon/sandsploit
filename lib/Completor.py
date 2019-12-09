
import os
import sys 
import readline
import glob
import re


def lists(path):
    apps = os.listdir("/usr/bin/")   
        
    commands = ['help','use','run','exit','banner','nano','update','upgrade','version','python','bash','su','sudo','systemctl','cd','ls','listener','generate','list','RSMaker']
    """
    Lists folder contents
    """
    if path.startswith(os.path.sep):
        # absolute path
        basedir = os.path.dirname(path)
        content = os.listdir(basedir)
        # add back the parent
        
        content = [os.path.join(basedir, d) for d in contents]
        contents = content + commands + apps
    else:
        # relative path
        content = os.listdir(os.curdir)
        contents = content + commands + apps
    return contents


def completer(text, state):

    options = [x for x in lists(text) if x.startswith(text)]
    return options[state]

readline.set_completer(completer)

readline.parse_and_bind('tab: complete')
readline.set_completer_delims(' \t\n`~!@#$%^&*()-=+[{]}\\|;:\'",<>?')
