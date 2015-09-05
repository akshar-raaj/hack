import logging
import log_child

#logging.basicConfig(filename='example.log',level=logging.DEBUG)
#logging.debug('debugger')
#logging.info('loog file %s', "blog")
#log_child.do_something()
#logging.warning("I warned you")

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
formatter = logging.Formatter("%(name)s %(levelname)s %(message)s")
ch.setFormatter(formatter)

logger.addHandler(ch)

logger.info("This is some info")
from cel_task import add
res = add(3, 4)
print res