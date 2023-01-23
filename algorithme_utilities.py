def list_is_empty(arr):
    if isinstance(arr, list) and len(arr) > 0:
        return False
    return True

def replace_dash(string = str):
    return string.replace("-", "_")
