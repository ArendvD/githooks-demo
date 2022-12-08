# The code in this file is poorly formatted. It is valid code and will work as intended, but does not follow
# conventions and therefore looks bad. "black" is a python package that formats code, ensuring a clean and
# consistent code style. It will fix issues related to spacing, indentation and line length.

# This code can be fixed by either:
# - "black demos/demo_black.py"
# - "pre-commit run --files demos/demos_black.py"
# - "pre-commit install", followed by "git add demos/demos_black.py" and "git commit"

import pandas as pd







def a(
    some_random_int:int
):
    
    
    b  = a+1
    return b
def d():
    my_long_string = "This string concatentation is a bit too long. " + "It will go over the set line length " + "Right about here."
    
    my_random_df_to_show_this_works_with_functions = pd.DataFrame({"a": [1,2,3], "b": [4,5,6]}).filter(items=["b"]).dropna().to_csv()
    
    return my_long_string, \
        my_random_df_to_show_this_works_with_functions


def f():
    
    my_list = [1,
               2,
               3
               ]
    
    return my_list
