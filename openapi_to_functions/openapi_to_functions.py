import jsonref
import json
from pprint import pp

def openapi_to_functions(openapi_spec):
    functions = []

    for path, methods in openapi_spec["paths"].items():
        for method, spec_with_ref in methods.items():
            # 1. Resolve JSON references.
            spec = jsonref.replace_refs(spec_with_ref)

            # 2. Extract a name for the functions.
            function_name = spec.get("operationId")

            # 3. Extract a description and parameters.
            desc = spec.get("description") or spec.get("summary", "")

            schema = {"type": "object", "properties": {}}

            req_body = (
                spec.get("requestBody", {})
                .get("content", {})
                .get("application/json", {})
                .get("schema")
            )
            if req_body:
                schema["properties"]["requestBody"] = req_body

            params = spec.get("parameters", [])
            if params:
                param_properties = {
                    param["name"]: param["schema"]
                    for param in params
                    if "schema" in param
                }
                schema["properties"]["parameters"] = {
                    "type": "object",
                    "properties": param_properties,
                }

            functions.append(
                {"type": "function", "function": {"name": function_name, "description": desc, "parameters": schema}}
            )

    return functions

with open('input.json', 'r') as f:
    openapi_spec = jsonref.loads(f.read()) # it's important to load with jsonref, as explained below

# print(openapi_spec)

functions = openapi_to_functions(openapi_spec)
# for function in functions:
#     pp(function)
#     print()

with open('output.json', 'w') as f:
    f.write('[' + (','.join(json.dumps(function) for function in functions)) + ']')
