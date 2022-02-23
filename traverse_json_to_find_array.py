def get_array_fieldlist(tdata):
    array_fieldlist = []

    # functions to identify [] and extract those out
    def find_arrays(data, prefix=None):
        # traverse through the json file,
        # if dict then go down another level,
        # if list then add to list of arrays,
        # else ignore
        for field in data:
            # print(prefix)
            previous_prefix = prefix
            if isinstance(data[field], dict):
                prefix = '.'.join([prefix, field]) if prefix is not None else field
                find_arrays(data[field], prefix)
            elif isinstance(data[field], list):
                prefix = '.'.join([prefix, field]) if prefix is not None else field
                array_fieldlist.append(prefix)
            else:
                pass
            prefix = previous_prefix

    find_arrays(tdata, None)
    return array_fieldlist
