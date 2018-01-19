# A sample Flask endpoint that shows how to get and return data

mydata = {
    "data": {
        "Henry": "7084852945",
        "Helga": "3845943859",
        "Billy": "2845903384"
    }
}


# Example of REST-ish endpoint
@app.route("/numbers", methods=['GET', 'PUT', 'POST', 'DELETE'])
def numbers():
    if request.method == 'GET':
        return jsonify(mydata)
    elif request.method == 'POST':
        name = request.get_json()["name"]
        number = request.get_json()["number"]

        mydata["data"][name] = number
        return jsonify(mydata)
    elif request.method == 'PUT':
        name = request.get_json()["name"]
        number = request.get_json()["number"]

        if name in mydata["data"]:
            mydata["data"][name] = number
            return jsonify(mydata)
        else:
            return jsonify({"message":"Name doesn't exist!"})
    elif request.method == 'DELETE':
        name = request.get_json()["name"]

        if name in mydata["data"]:
            del mydata["data"][name]
            return jsonify(mydata)
        else:
            return jsonify({"message":"Name doesn't exist!"})
    else:
        return jsonify({"message": "Method not allowed!"})

