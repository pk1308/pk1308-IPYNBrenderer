import pytest

from IPYNBrenderer import render_google_doc
from IPYNBrenderer.custom_exception import InvalidGoogleDocidException

good_id_data = [
    ("1OdJYEFftsw1ZjQjurHJQtmIYysfTkrrq", "success"),
    ("1uMWKQ4GfOk_vep3yIfQ3axKm2E-6XfYw-iSqsO5WE0M", "success"),
    ("186vEV4wIcqNzw8hgq1HD5AqPcWUusH8LTrtwKY-fMuY", "success"),
    ("101jrn2Nf2LqzYu2mlgIVdBhezKTYDfh1D5obmwydxo4", "success"),
]


bad_id_data = [
    ("1OdJYEFftsw1ZjQjurHJQtmIYysfTkrrsssssq"),
    ("1uMWKQ4GfOk_vep3yIfQ3axKm2E-6XfYw-jjjjsO5WE0M"),
    ("186vEV4wIcqNzw8hgq1HD5AqPcWUusH8LTrtw-fMuY"),
    ("101jrn2Nf2LqzYu2mlgIVdBhezKTYmwydxo4"),
]


@pytest.mark.parametrize("google_id, response", good_id_data)
def test_render_google_doc(google_id, response):
    assert render_google_doc(google_id) == response


@pytest.mark.parametrize("google_id", bad_id_data)
def test_render_doc_failed(google_id):
    with pytest.raises(InvalidGoogleDocidException):
        render_google_doc(google_id)
