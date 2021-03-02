from flask import Blueprint, request
from .utilities import get_formatted_info, make_json
api = Blueprint("api", __name__)

@api.route("get",methods=["GET"])
def get():
  entries = get_formatted_info()
  data = request.args.get("data")
  if str(data).capitalize() in entries or str(data).lower() == "all":
    if str(data) == "all":
      return make_json(entries["Gesamt"])
    else:
      return make_json(entries[data.capitalize()])
  else:
    print(f"Data: {data}, entries:\n{entries[str(data).capitalize()]}")
    return f"Data for {data} doesn't exist!\n"