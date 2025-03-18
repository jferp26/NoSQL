from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
app = Flask(__name__)

client = MongoClient("mongodb://admin:admin123@localhost:27017/?authSource=admin")
db = client ["practica_flask"]
collection = db["personas"]

@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        nombre= request.form.get("nombre")
        if nombre:
            collection.insert_one({"nombre":nombre})
    personas=list(collection.find())
    return render_template("index.html", personas=personas)


@app.route("/delete/<id>")
def delete(id):
    collection.delete_one(({"_id": ObjectId(id)}))
    return redirect(url_for("index"))



@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    persona=collection.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        nuevo_nombre = request.form.get("nombre")
        if nuevo_nombre:
            collection.update_one({"_id": ObjectId(id)}, {"$set": {"nombre": nuevo_nombre}})
        return redirect(url_for("index"))
    return render_template("edit.html", persona=persona)



if __name__=="__main__":
    app.run(debug=True)