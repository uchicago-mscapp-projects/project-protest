import sys
from .clean_data.compile_news_data import compile_news_data
import os


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "compile_news":
            compile_news_data()
        elif sys.argv[1] == "create_dashboard":
            execfile(os.path.join(os.getcwd(), "html/dashboard.py"))
        elif sys.argv[1] == "run_all":
            compile_news_data(collect_data = True)
            execfile(os.path.join(os.getcwd(), "html/dashboard.py")) 
        else:
            print("Incorrect arguments. Send 'compile_news' and/or\
                    'create_dashboard'")
    
    elif len(sys.argv) == 1:
        print("Not enough arguments. Send 'compile_news', 'create_dashboard',\
                or 'run_all'")
    
    else:
        print("Too many arguments. Send 'compile_news', 'create_dashboard', or\
                'run_all'")
