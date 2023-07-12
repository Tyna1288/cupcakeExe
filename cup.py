"""Cupcake application."""

from models import db, connect_db, Cupcake
from flask import Flask, render_template, request, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234567@localhost:5433/cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
with app.app_context():
    connect_db(app)


@app.route('/')
def home_page():
    return render_template('cupcake.html')


@app.route("/api/cupcakes")
def cupcake_list():
    """Return all cupcakes in the order {cupcakes: [{id, flavor, rating, size, image}, ...]}"""

    cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)


@app.route("/api/cupcakes", methods=["POST"])
def add_new_cupcake():
    """Add new cupcake """

    data = request.json

    cupcake = Cupcake(
        flavor=data['flavor'],
        rating=data['rating'],
        size=data['size'],
        image=data['image'] or None)

    db.session.add(cupcake)
    db.session.commit()

    # POST requests will return HTTP status of 201 CREATED
    return (jsonify(cupcake=cupcake.to_dict()), 201)


@app.route("/api/cupcakes/<int:cupcake_id>")
def show_cupcake(cupcake_id):
    """Return data on a cupcake."""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.to_dict())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def edit_cupcake(cupcake_id):
    """Edit cupcake and return updated cupcake data."""

    data = request.json

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.to_dict())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """Delete cupcake and return confirmation message."""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")

