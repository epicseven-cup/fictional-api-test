Terms:
- ub -> Universal Bytes
- path -> the endpoint of that api service
- request_type -> the HTTP type of that request the service expect
- respond_type -> the respond type (data) that the web service expect

compiles yaml to a simple flask application with custom / default respond

Run script.py for a quick demo, the output file is in output/app.py

yapf.config is used to configure coding style being output by the compiler
test.yaml is being used for testing


Currently support these default format:
    - application_json
    - text_html
    - text_plain
    - text_xml

custom return respond:
- respond/{self.path}.{self.request_type}.{self.respond_type}.ub"