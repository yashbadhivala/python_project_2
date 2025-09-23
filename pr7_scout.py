
def dir_info(module_obj):
    return [x for x in dir(module_obj) if not x.startswith("__")]
