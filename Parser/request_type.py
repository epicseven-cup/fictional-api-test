from enum import StrEnum

class RequestType(StrEnum):
	get = "get"
	post = "post"
	put = "put"
	delete = "delete"
	pass