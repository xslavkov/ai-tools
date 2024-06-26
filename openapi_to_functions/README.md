# OPEN API  -> Function calling

Convert open api specification (swagger) to function calling specification. [Link to source.](https://cookbook.openai.com/examples/function_calling_with_an_openapi_spec)

>It doesn't always work. It sometimes fails on recursive issue. In such case it helped me to remove `paths` from open api specification that i was not interested in.

# Run

- `input.json` - download your OPEN API specification here
- `output.json` - function calling result will be prented here
- `openapi_to_functions.py`

```bash
# localy
$ python openapi_to_functions.py

# using pyhon docker

$ ../docker/python/run.sh openapi_to_functions.py
```
