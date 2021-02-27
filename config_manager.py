import configparser
import ast

_config = configparser.ConfigParser() # reads the file
_config.read('config.ini')


def connect_db():
    connection_details = _config['DEFAULT']['connection']  # returns a string
    # we want to evaluate it to a dict
    return ast.literal_eval(connection_details)
