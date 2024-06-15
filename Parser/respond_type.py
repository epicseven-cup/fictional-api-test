import json
import xml
from enum import StrEnum

class RespondType(StrEnum):
	# Currently supported respond types
	text_html = 'text/html'
	text_plain = 'text/plain'
	text_xml = 'text/xml'
	application_json = 'application/json'
	pass

# Transform respond