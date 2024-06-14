# This will write the docker file for the user

# Getting the openapi spec and parse it
import yaml
import pprint

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


path = "openapi.yaml"

content = open(path).read()
specs = yaml.safe_load(content)
# pprint.pp(specs)


# Within the path routes the keys of the path routes are the endpoints that are trying to be hit
endpoints = {}
for endpoint in specs.get("paths", []):
    request_types = set(specs["paths"][endpoint].keys())
    endpoints[endpoint] = request_types
app_name = "Hello"
flask = (f"import flask\n"
         f"app = flask('{app_name}')\n")
for end in endpoints:
    requests = endpoints[end]
    for r in requests:
        sr = r.lower()
        if sr == "get":
            flask = flask + create_get_routes(end)
        elif sr == "post":
            flask = flask + create_post_routes(end)
        elif sr == "put":
            flask = flask + create_put_routes(end)
        elif sr == "delete":
            flask = flask + create_delete_routes(end)

with open("app.py", "w") as file:
    file.write(flask)




