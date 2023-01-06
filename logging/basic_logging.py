#logging module
import logging

#bydefault logging level set to Warning
logging.critical("critical")
logging.error("error")
logging.warning("warning")
logging.info("info")
logging.debug("debug")

###So what are logging levels and how many types have
#try running by changing log levels

logging.basicConfig(level=logging.CRITICAL)
logging.critical("critical")
logging.error("error")
logging.warning("warning")
logging.info("info")
logging.debug("debug")

logging.basicConfig(level=logging.ERROR)
logging.critical("critical")
logging.error("error")
logging.warning("warning")
logging.info("info")
logging.debug("debug")

logging.basicConfig(level=logging.WARNING)
logging.critical("critical")
logging.error("error")
logging.warning("warning")
logging.info("info")
logging.debug("debug")

logging.basicConfig(level=logging.INFO)
logging.critical("critical")
logging.error("error")
logging.warning("warning")
logging.info("info")
logging.debug("debug") 

logging.basicConfig(level=logging.DEBUG)
logging.critical("critical")
logging.error("error")
logging.warning("warning")
logging.info("info")
logging.debug("debug")

#conclusion: critical level has higer priority  and followed by error, warning , info and finally debug .

###end users dont want these level info and also they want a specific format of the log msg
#we have format attribute

logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(levelname)s - %(message)s')
logging.info("message1")
logging.info("message2")
logging.info("message3")



#lets try some more options
logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(levelname)s:%(filename)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
logging.info("message1")
logging.info("message2")
logging.info("message3")

#till if you observe messages are printing into console. now lets try populating these message into a file
logging.basicConfig\
    (level=logging.INFO,format='%(asctime)s:%(levelname)s:%(filename)s - \
    %(message)s',datefmt='%Y-%m-%d %H:%M:%S',filename='logging.log')
logging.info("message1")
logging.info("message2")
logging.info("message3")

#lets try these also %p %a %A in datefmt


































