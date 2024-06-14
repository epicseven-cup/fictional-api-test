from Parser.parser import Parser
path = "./test.yaml"
content = open(path).read()
parser = Parser(content)
parser.render()