import pprint
from typing import TextIO

import flask

from Parser.request_type import RequestType
from Parser.respond_type import RespondType


def create_get_routes(end, respond):
	return (f"@app.get('{end}')\n"
	        f"def respond_get{end.replace("/", "_")}():\n"
	        f"\treturn {respond}\n")


def create_post_routes(end, respond):
	return (f"@app.post('{end}')\n"
	        f"def respond_get{end.replace("/", "_")}():\n"
	        f"\treturn {respond}\n")


def create_put_routes(end, respond):
	return (f"@app.put('{end}')\n"
	        f"def respond_get{end.replace("/", "_")}():\n"
	        f"\treturn {respond}\n")


def create_delete_routes(end, respond):
	return (f"@app.delete('{end}')\n"
	        f"def respond_get{end.replace("/", "_")}():\n"
	        f"\treturn {respond}\n")


def transform_request(request: RequestType, path: str, respond: str):
	match request.name:
		case "get":
			return create_get_routes(path, respond)
		case "post":
			return create_post_routes(path, respond)
		case "put":
			return create_put_routes(path, respond)
		case "delete":
			return create_delete_routes(path, respond)


def transform_respond(respond_type: RespondType, status_code: int, file: TextIO) -> str:
	ub_respond: str = file.read()
	respond_content = ""
	match respond_type.name:
		case "text_html":
			# Since htmls can already be written in strings returning the string will be just fine
			respond_content = f"'{ub_respond}'"
		case "text_plain":
			respond_content = f"'{ub_respond}'"
		case "text_xml":
			respond_content = f"'{ub_respond}'"
		case "application_json":
			respond_content = f"json.loads(json.dumps({ub_respond}))\n"
	return f'flask.Response(response = {respond_content}, status = {status_code}, mimetype="", content_type="{RespondType[respond_type.name]}")'
