from enum import StrEnum


class RequestType(StrEnum):
	GET = "get"
	POST = "post"
	PUT = "put"
	DELETE = "delete"
	pass


def create_get_routes(end, respond):
	return (f"@app.get('{end}')\n"
	        f"def respond_get_{end.replace("/", "")}():\n"
	        f"\t{respond}")


def create_post_routes(end, respond):
	return (f"@app.post({end.replace("/", "")})()\n"
	        f"def respond_post_{end}:\n"
	        f"\t{respond}")


def create_put_routes(end, respond):
	return (f"@app.put({end})\n"
	        f"def respond_put_{end.replace("/", "")}():\n"
	        f"\t{respond}")


def create_delete_routes(end, respond):
	return (f"@app.delete({end})\n"
	        f"def respond_delete_{end.replace("/", "")}():\n"
	        f"\t{respond}")


def transform_request(request: RequestType, path: str, respond:str):
	match request.name:
		case "get":
			return create_get_routes(path, respond)
		case "post":
			return create_post_routes(path, respond)
		case "put":
			return create_put_routes(path, respond)
		case "delete":
			return create_delete_routes(path, respond)
