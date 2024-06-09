import os.path

from Parser.request_type import RequestType
from Parser.respond_type import RespondType


class Path:
	def __init__(self, path_data) -> None:
		# Currently this is assuming that each path only have one request type and one respond type
		self.path = path_data.get("path", "")
		self.request_type = RequestType(path_data.get("request_type", []))
		self.respond_type = RespondType(path_data.get("respond_type", []))
		pass
	def respond(self) -> str:
		# This respond method should just return what the user citied, if user did not define a structure to the request
		# This should use the default pre-define json/return data type
		# The naming convseration for this path return type in the user's end should be in $project_root/respond/{api_path}.{request_type}.{respond_type}.ub
		expect_path = f"./respond/{self.path}.{self.request_type}.{self.respond_type}.ub"

		file_exist = os.path.isfile(expect_path)
		current_respond = ""
		if file_exist:
			current_respond = open(expect_path).read()
		else:
			default_path = f"./default/respond/{self.respond_type}.ub"
			current_respond = open(default_path).read()

		# Reformat the response if needed
		pass
