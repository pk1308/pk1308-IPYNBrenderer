import pytest

from IPYNBrenderer import is_valid_id
from IPYNBrenderer.custom_exception import InvalidURLException

good_id_data = [
    ("1OdJYEFftsw1ZjQjurHJQtmIYysfTkrrq", True),
    ("1uMWKQ4GfOk_vep3yIfQ3axKm2E-6XfYw-iSqsO5WE0M", True),
    ("186vEV4wIcqNzw8hgq1HD5AqPcWUusH8LTrtwKY-fMuY", True),
    ("101jrn2Nf2LqzYu2mlgIVdBhezKTYDfh1D5obmwydxo4", True),
]


bad_id_data = [
    ("1OdJYEFftsw1ZjQjurHJQtmIYysfTkrrsssssq", False),
    ("1uMWKQ4GfOk_vep3yIfQ3axKm2E-6XfYw-jjjjsO5WE0M", False),
    ("186vEV4wIcqNzw8hgq1HD5AqPcWUusH8LTrtw-fMuY", False),
    ("101jrn2Nf2LqzYu2mlgIVdBhezKTYmwydxo4", False),
]


@pytest.mark.parametrize("google_id, response", good_id_data)
def test_is_vakid_id(google_id, response):
    assert is_valid_id(google_id) == response


@pytest.mark.parametrize("google_id, response", bad_id_data)
def test_is_vakid_id_failed(google_id, response):
    assert is_valid_id(google_id) == response
