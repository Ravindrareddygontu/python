'''1. LoggingToPrompt'''

##from logging import*
##debug("this is a debug")
##info("this is a info")
##warning("this is a warning")
##error("this is a warning")
##critical("this is a critical")

'''2. LogginToFile'''
##from logging import*
##basicConfig(filename="logfile.log")
##warning("this is a warning")
##error("this is a error")
##critical("this is a critical")

'''3. ChangeLevel'''
##from logging import *
##basicConfig(filename="logfile2303.log", level=DEBUG)
##debug("This is Debug")
##info("This is Info")
##warning("This is Warning")
##error("This is Error")
##critical("This is Critical")

'''4.ChangeFileMod'''
##from logging import *
##basicConfig(filename="logfile303.log", level=DEBUG, filemode='w')
##debug("This is Debug")
##info("This is Info")
##warning("This is Warning")
##error("This is Error")
##critical("This is Critical")

'different functions of logging'
##import logging
##logging.warning('watch out!1')
##logging.error('error have occured')
##logging.info('this is info')
##logging.critical('you must had to see it')
