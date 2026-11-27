# Python - Almost a circle

## Task 0. If it's not tested it doesn't work

All files, classes and methods are unit tested and PEP 8 validated.

- Directory: `tests/`
- Usage: `python3 -m unittest discover tests`

## Task 1. Base

Write the first class Base in models/base.py. It has a private class attribute __nb_objects = 0 and a constructor def __init__(self, id=None): that assigns id if it is not None, otherwise increments __nb_objects and assigns the new value to id.

- File: `models/base.py`
- Tests: `tests/test_models/test_base.py`
