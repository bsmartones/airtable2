"""
Usage - Text Column is not empty:

>>> airtable.get_all(formula="NOT({COLUMN_A}='')")

Usage - Text Column contains:

>>> airtable.get_all(formula="FIND('SomeSubText', {COLUMN_STR})=1")

Args:
    formula (``str``): A valid Airtable formula.
"""


def field_equals_value(field_name, field_value):
    """
    Creates a formula to match cells from from field_name and value
    """
    if isinstance(field_value, str):
        field_value = "'{}'".format(field_value)

    formula = "{{{name}}}={value}".format(name=field_name, value=field_value)
    return formula


def EQUAL(left, right):
    # if isinstance(field_value, str):
    # field_value = "'{}'".format(field_value)
    # formula = "{{{name}}}={value}".format(name=field_name, value=field_value)
    return "{}={}".format(left, right)


def IF(logical, value1, value2):
    return "IF({}, {}, {})".format(logical, value1, value2)


def AND(*args):
    return "AND({})".formate(",".join(args))


def FIND(find, where, start_from=None):
    ...
    # FIND(stringToFind, whereToSearch,[startFromPosition])
    # airtable.get_all(formula="FIND('SomeSubText', {COLUMN_STR})=1")
    # return "FIND('SomeSubText', {COLUMN_STR})=1"