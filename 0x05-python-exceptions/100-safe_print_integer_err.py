import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err:
        sys.stderr.write(f"Unexpected {err=}")
        return False