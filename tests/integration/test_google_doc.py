import pytest

from IPYNBrenderer import render_google_doc
from IPYNBrenderer.custom_exception import InvalidGoogleDocidException

good_id_data = [
    ("https://drive.google.com/file/d/1OdJYEFftsw1ZjQjurHJQtmIYysfTkrrq/view?usp=sharing", "success"),
    ("https://docs.google.com/document/d/1uMWKQ4GfOk_vep3yIfQ3axKm2E-6XfYw-iSqsO5WE0M/edit?usp=sharing", "success"),
    ('https://docs.google.com/spreadsheets/d/186vEV4wIcqNzw8hgq1HD5AqPcWUusH8LTrtwKY-fMuY/edit?usp=sharing', "success"),
    ( "https://docs.google.com/presentation/d/101jrn2Nf2LqzYu2mlgIVdBhezKTYDfh1D5obmwydxo4/edit?usp=sharing", "success"),
]


bad_id_data = [
    ("https://drive.google.com/file/d/12NPraWCCNODn1lmfffp4ahoBjxPh9_-KaV0/view?usp=sharing"),
    ("https://drive.google.com/file/d/1L7Fh56-uJUc60S1lfff0Wd_NjWRGgvUCqAg/view?usp=sharing"),
    ('https://docs.google.com/spreadsheets/d/186IcqNzw8hgq1HD5AqPcWUusH8LTrtwKY-fMuY/edit?usp=sharing'),
    ("https://docs.google.com/presentation/d/10lkkkhjhhjj2mlgIVdBhezKTYDfh1D5obmwydxo4/edit?usp=sharing"),
]


@pytest.mark.parametrize("google_id, response", good_id_data)
def test_render_google_doc(google_id, response):
    assert render_google_doc(google_id) == response


@pytest.mark.parametrize("google_id", bad_id_data)
def test_render_doc_failed(google_id):
    with pytest.raises(InvalidGoogleDocidException):
        render_google_doc(google_id)
