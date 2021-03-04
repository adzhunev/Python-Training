import os
import json
import hcl
from contextlib import contextmanager

# executing command: radon cc Cognitive_complexity.py -s
# Cognitive complexity of the initial function is: F 9:0 file_handler - B (8)

cfn = [".json", ".template", ".yaml", ".yml"]
tf = ["tf"]

def _file_paths(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                yield file_path

def _handle_cfn(file_object):
    file_contents = file_object.read()
    if "AWSTemplateFormatVersion" in file_contents:
        data = json.dumps(file_contents)
        print(data)

def _handle_tf(file_object):
    obj  = hcl.load(file_object)
    data = json.dumps(obj)
    print(data)

def _null_handler(file_object):
    pass

@contextmanager
def _translate_error(from_error, to_error):
    try:
        yield
    except from_error as error:
        raise to_error(error)

_extension_handlers = {'.json': _handle_cfn,
            '.template': _handle_cfn,
            '.yaml': _handle_cfn,
            '.yml': _handle_cfn,
            '.tf': _handle_tf}

#main function
def file_handler(dir):
    for file_path in _file_paths(dir):
        base, extension = os.path.splitext(file_path)
        handler = _extension_handlers.get(extension, _null_handler)
        with open(file_path) as file_object:
            with _translate_error(ValueError, SystemExit):
                handler(file_object)

# Cognitive complexity after splitting to different functions
# Cognitive_complexity.py
#     F 12:0 _file_paths - A (4)
#     F 19:0 _handle_cfn - A (2)
#     F 40:0 _translate_error - A (2)
#     F 47:0 file_handler - A (2)
#     F 25:0 _handle_tf - A (1)
#     F 30:0 _null_handler - A (1)
