import urllib.request
import warnings

from ensure import ensure_annotations
from IPython import display

from IPYNBrenderer.custom_exception import InvalidGoogleDocidException
from IPYNBrenderer.logger import logger

warnings.filterwarnings("ignore")


@ensure_annotations
def is_valid_id(GOOGLE_DOC_ID: str) -> bool:
    try:
        GOOGLE_DOC_URL = (
            f"https://drive.google.com/file/d/{GOOGLE_DOC_ID}/view?usp=sharing"
        )
        response_status = urllib.request.urlopen(GOOGLE_DOC_URL).getcode()
        assert response_status == 200
        logger.debug(f"response_status: {response_status}")
        return True
    except Exception as e:
        logger.exception(e)
        return False


@ensure_annotations
def render_google_doc(
    GOOGLE_DOC_ID: str, width: str = "640", height: str = "600"
) -> str:
    try:
        if is_valid_id(GOOGLE_DOC_ID):
            iframe = f"""<iframe 
            src="https://drive.google.com/file/d/{GOOGLE_DOC_ID}/preview" 
            width={width} height={height} 
            allow="autoplay"></iframe>"""
            response = display.HTML(iframe)
            display.display(response)
            return "success"
        else:
            raise InvalidGoogleDocidException
    except Exception as e:
        raise e
