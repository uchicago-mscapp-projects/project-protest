import sys
from .clean_data.compile_news_data import compile_news_data
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

if __name__ == "__main__":
    # CHECK IF WE COULD ADD BY DEFAULT THAT WE RUN EVERYTHING IF WE DON'T
    # SPECIFY ANY ARGUMENTS
    if len(sys.argv) == 1 :
        print("Not enough arguments. Send 'compile_news', 'create_dashboard',\
                or 'run_all'")

    elif len(sys.argv) == 2:
        if sys.argv[1] == "compile_news":
            compile_news_data()
        elif sys.argv[1] == "create_dashboard":
            execfile(os.path.join(current_dir, "html/dashboard.py"))
        elif sys.argv[1] == "run":
            compile_news_data()
            execfile(os.path.join(current_dir, "html/dashboard.py"))
        # print("Not enough arguments. Send 'compile_news', 'create_dashboard',\
        #         or 'run_all'")
    
    elif len(sys.argv) == 3:
        if sys.argv[1] == "compile_news" and sys.argv[2] == "collect_data":
            compile_news_data(True)
        elif sys.argv[1] == "create_dashboard":
            print("Too many arguments. Send just 'create_dashboard'")
        elif sys.argv[1] == "run" and sys.argv[2] == "collect_data":
            compile_news_data(collect_data = True)
            execfile(os.path.join(current_dir, "html/dashboard.py")) 
        else:
            print("Incorrect arguments. Send 'compile_news',  and/or\
                    'create_dashboard'")
    
    
    else:
        print("Too many arguments. Send 'compile_news', 'create_dashboard', or\
                'run_all'")
