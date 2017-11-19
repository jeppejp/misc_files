import re

def is_valid_version(version):
    valid_version = "^[0-9]+\.[0-9]+\.[0-9]+$"
    return re.match(valid_version, version) != None

def is_valid_spec(specification):
    valid_spec = "^([0-9]+|\*)\.([0-9]+|\*)\.([0-9]+|\*)$"
    return re.match(valid_spec, specification) != None

def best_match(versions, spec):
    if not is_valid_spec(spec):
        raise Exception("Not valid specification [%s]"%(spec))

    spec_pattern = spec.replace("*", "[0-9]+")
    best = None
    for version in versions:
        if re.match(spec_pattern, version) != None:
            best = _max_version(best, version)
    return best

def _max_version(v1, v2):
    if v1 == None:
        return v2
    if v2 == None:
        return v1

    v1_spl = v1.split(".")
    v2_spl = v2.split(".")
    for i in [0,1,2]:
        if int(v1_spl[i]) > int(v2_spl[i]):
            return v1
        if int(v2_spl[i]) > int(v1_spl[i]):
            return v2

    # they are equal?
    return v1

