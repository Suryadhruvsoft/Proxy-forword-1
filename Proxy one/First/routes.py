from flask import render_template, request
from First import app, db
from First.models import students
from requests import get
import requests
import json
# import Werkzeug

second_url = "http://127.0.0.1:8000"
@app.route('/<path:path>', methods=['GET', 'POST'])
def proxy(path):
      final_url = f'{second_url}{request.full_path}'
      headers = {k: v for k, v in request.headers}
      headers["Host"] = "127.0.0.1:8000"
      response = requests.request(request.method, final_url, headers=headers ,data=json.dumps(request.json))
      # print(request.method)
      # print("data:",headers)
      # print(request.headers.get("Host", ""))
      return response.content