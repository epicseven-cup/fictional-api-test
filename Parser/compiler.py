import yaml
from yapf.yapflib.yapf_api import FormatCode
from Parser.path import Path


class Compiler:
	def __init__(self, path: str) -> None:
		yaml_data = yaml.safe_load(path)
		self.status_codes = {200}
		self.datas = self.parse_yaml_path(yaml_data)
		pass

	def parse_yaml_path(self, yaml_data):
		paths = yaml_data.get("paths", {})
		output = {}
		content = ""
		# Going through all the paths
		for endpoint in paths:
			# Going through each http request
			output[endpoint] = {}
			for request in paths[endpoint]:
				# Request type to respond
				output[endpoint][request] = {}
				respond = paths[endpoint][request]["respond"]
				status_code = int(paths[endpoint][request].get("status", "200"))
				code = Path(endpoint, status_code, request, respond).render()
				content = content + code
		return content
	def render(self):
		filename = "./template/template.app.py"
		header = open(filename).read()
		content = self.datas
		file_content = header + content
		style:str = "google" if open("yapf.config").read() == "" else open("yapf.config").read()
		format_content, status = FormatCode(file_content, style)
		if status:
			open("output/app.py", "w").write(format_content)
		else:
			open("output/app.py", "w").write("Error")