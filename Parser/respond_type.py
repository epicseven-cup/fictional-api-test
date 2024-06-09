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
def transform(respond_type:RespondType, ub_respond:str) -> str:
	match respond_type:
		case "text_html":
			# Since htmls can already be written in strings returning the string will be just fine
			return ub_respond
		case "text_plain":
			return ub_respond
		case "text_xml":
			return ub_respond
		case "application_json":
			return f"json.loads({ub_respond})"