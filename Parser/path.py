import os.path
from Parser.helper import transform_request, transform_respond
from Parser.request_type import RequestType
from Parser.respond_type import RespondType


class Path:
	def __init__(self, pathName:str, status_code, request:str, respond:str) -> None:
		# Currently this is assuming that each path only have one request type and one respond type
		self.path = pathName
		self.status_code = status_code
		self.request_type = RequestType(request)
		self.respond_type = RespondType(respond)
		self.respond = self.respond()
		self.code = self.render()
		pass
	def render(self) -> str:
		return transform_request(self.request_type, self.path, self.respond)
	def respond(self) -> str:
		# This respond method should just return what the user citied, if user did not define a structure to the request
		# This should use the default pre-define json/return data type
		# The naming convseration for this path return type in the user's end should be in $project_root/respond/{api_path}.{request_type}.{respond_type}.ub
		expect_path = f"respond/{self.path}.{self.request_type}.{self.respond_type}.ub"

		file_exist = os.path.isfile(expect_path)
		default_path = f"respond/default/{self.respond_type.name}.ub"
		current_respond = open(default_path)
		if file_exist:
			current_respond = open(expect_path)
		return transform_respond(self.respond_type, self.status_code, current_respond)