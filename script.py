from Parser.compiler import Compiler

path = "./test.yaml"
content = open(path).read()
parser = Compiler(content)
parser.render()