from gs_versions import *


def test_valid_version():
    assert is_valid_version("1.2.3")
    assert is_valid_version("0.1.000")
    assert is_valid_version("999.888.000")
    assert not is_valid_version("v1.2.3")
    assert not is_valid_version("V1.2.3")
    assert not is_valid_version("1.2.3-xx")
def test_valid_spec():
    assert is_valid_spec("1.2.3")
    assert is_valid_spec("1.2.*")
    assert is_valid_spec("*.*.*")
    assert not is_valid_spec("ab.1.2")
    assert not is_valid_spec("*/.1.4")
    assert not is_valid_spec("0.4.4+")



def test_best_match():
    versions = []
    versions.append("1.0.0")
    versions.append("1.0.1")
    versions.append("1.1.0")
    versions.append("1.1.5")
    versions.append("5.22.0")
    versions.append("5.1.4")
    versions.append("5.119.3")
    versions.append("20.2.1")
    versions.append("20.11.9")
    versions.append("20.0.0")

    #versions, spec
    assert "20.11.9" == best_match(versions, "*.*.*")
    assert "5.119.3" == best_match(versions, "5.*.*")
    assert "1.1.5" == best_match(versions, "1.*.*")
    assert "1.0.1" == best_match(versions, "1.0.*")
