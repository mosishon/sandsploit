import readline
import glob
import re


def lists(path):        
    commands = COMMANDS = ['help','author','run','exit','info','show_options','set']
    return commands


def completer(text, state):

    options = [x for x in lists(text) if x.startswith(text)]
    return options[state]

readline.set_completer(completer)

readline.parse_and_bind('tab: complete')
readline.set_completer_delims(' \t\n`~!@#$%^&*()-=+[{]}\\|;:\'",<>?')

#def ssfpromot(name,author,info,help,options,run,host):
    
    


