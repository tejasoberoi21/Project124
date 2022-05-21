from flask import Flask, jsonify,request

App = Flask(__name__)

contacts = [
    {
    "id":1,
    "title":"test",
    "description":"testing flask",
    "done": False
    }
]

@App.route("/get_data")

def getTasks():
    return jsonify({
        "data":contacts
        })
@App.route("/post_data", methods = ["POST"])

def addTask():
    if(not request.json):
        return jsonify({
            "status": "error",
            "message":"provide data"
            },400)
    task = {
        "id":tasks[-1]["id"]+1,
        "Name":request.json["Name"],
        "Contact":request.json.get("Contact",""),
        "done":False
        }
    contacts.append(task)
    return jsonify({
        "status":"success",
        "message":"task added"
        })
if(__name__ == "__main__"):
    App.run(debug = True)



        
    


