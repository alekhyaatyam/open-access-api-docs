from flask import Flask, jsonify, request, Response
from flasgger import Swagger
import dicttoxml
import yaml
import os

app = Flask(__name__)

# Load OpenAPI YAML
yaml_path = os.path.join(os.path.dirname(__file__), "openapi.yaml")
with open(yaml_path, "r") as f:
    swagger_template = yaml.safe_load(f)

# ✅ Initialize Flasgger with OpenAPI 3 template
swagger = Swagger(app, template=swagger_template)

# Sample data
articles = [
    {"id": 1, "title": "Climate Change and Renewable Energy", "authors": ["Alice Johnson", "Mark Lee"], "journal": "Open Access Energy Journal", "year": 2023},
    {"id": 2, "title": "AI in Healthcare", "authors": ["John Doe", "Jane Smith"], "journal": "PLOS One", "year": 2024}
]

@app.route("/api/articles", methods=["GET"])
def get_articles():
    fmt = request.args.get("format", "json").lower()
    if fmt == "xml":
        xml_data = dicttoxml.dicttoxml(articles, custom_root='articles', attr_type=False)
        return Response(xml_data, mimetype="application/xml")
    return jsonify(articles)

if __name__ == "__main__":
    app.run(debug=True)
