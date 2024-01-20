import os
import sys
class APP:
    def INIT(CFG):
        os.system('COLOR 0F')
        os.system('CLS')
        print("Loaded ProCan pre-alpha A000\n\n----------------------------------------------\n||THIS MODULE IS IN VERY EARLY DEVELOPEMENT||\n||USE AT YOUR OWN RISK                     ||\n----------------------------------------------")
        MEM = CFG
        print("Initialised ProCan to " + MEM)
    def CRASHPROTOCOL(Error,CLI1,CLI2):
        os.system('CLS')
        os.system('COLOR B2')
        print("This App Has Crashed\n\n\nError Code: " + Error + "\n\nMore Information:\n" + CLI1 + "\n" + CLI2 + "\n\n\nPress any key to restart...")
        os.system('pause>nul')
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    def BLANK():
        return 0

class LIST:
    def SHORTLIST(LINAME,LI1,LI2,LI3,LI4,LI5):
        if LINAME == " ":
            APP.CRASHPROTOCOL("LINAME_ERROR","New Short List has crashed","due to an Illegal List name")
        (LINAME) = (LI1,LI2,LI3,LI4,LI5)
