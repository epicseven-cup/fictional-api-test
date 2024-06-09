import yaml
class Parser:
	def __init__(self, path:str) -> None:
		yaml_data = yaml.safe_load(path)
		paths = {}
		pass