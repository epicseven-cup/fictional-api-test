import yaml

from Parser.path import Path


class Parser:
	def __init__(self, path:str) -> None:
		yaml_data = yaml.safe_load(path)
		print(yaml_data)
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
				print(output)
				print("test: ", type(list(paths[endpoint][request].keys())[0]))
				for status_code in paths[endpoint][request]:
					print(output[endpoint][request])
					if status_code in self.status_codes:
						respond = paths[endpoint][request][status_code]["respond"]
						print(respond)
						code = Path(endpoint, request, respond).render()
						print(code)
						content = content + code
		print(content)
		return content
	def render(self):
		filename = "./template/template.app.py"
		header = open(filename).read()
		content = self.datas
		print(content)
		file_content = header + content
		open("app.py", "w").write(file_content)