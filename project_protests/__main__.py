##################################################
# Author: Josemaria Macedo Carrillo              #
# Task: Run package from command line            #
# Last updated: 03-07-23                         #
##################################################

import sys
from project_protests.newspaper.compile_news_data import compile_news_data
import os
from  project_protests.html.dashboard import app
import random

current_dir = os.path.dirname(os.path.realpath(__file__))
port = random.randint(5000, 10000)

if __name__ == "__main__":

    if len(sys.argv) == 1 :
        app.run_server(port=port,debug = True)

    elif len(sys.argv) == 2:
        if sys.argv[1] == "compile_news":
            compile_news_data()
        elif sys.argv[1] == "run":
            compile_news_data()
            app.run_server(port=port,debug = True)
        else:
            print("Incorrect arguments. Send 'compile_news' or 'run'.")
    
    elif len(sys.argv) == 3:
        if sys.argv[1] == "compile_news" and sys.argv[2] == "collect_data":
            compile_news_data(True)
        elif sys.argv[1] == "run" and sys.argv[2] == "collect_data":
            compile_news_data(collect_data = True)
            app.run_server(port=port,debug = True)
        else:
            print("Incorrect arguments. Send 'compile_news' or 'run' as first\
                    argument and 'collect_data' as second argument.")

    else:
        print("Too many arguments. Sen no arguments, or send 'compile_news' or\
                'run'")
