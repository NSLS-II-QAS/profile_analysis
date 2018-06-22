import databroker
from PyQt5.QtWidgets import QApplication
import sys
from isstools.xview import XviewGui

import requests
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

db = databroker.Broker.named('qas')

# TODO : we shouldn't need this
QAS_MONO_PULSES_PER_DEGREE = 23600*400/360
app = QApplication(sys.argv)
xview_gui = XviewGui(QAS_MONO_PULSES_PER_DEGREE, db=db)

def xview():
    xview_gui.show()

xview()
