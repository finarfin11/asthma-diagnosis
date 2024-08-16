import re

def to_snake_case(text):
    ''' Takes string as an argument an converts it to snake_case '''
    pattern = re.compile(r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")
    return pattern.sub('_', text).lower()
   