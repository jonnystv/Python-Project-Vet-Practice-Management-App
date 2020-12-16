from flask import Flask, render_template, Blueprint, redirect, request

from models.animal import Animal
from models.vet import Vet

import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route("/")
def animals():
    animals = animal_repository.select_all()
    return render_template("index.html", animals = animals)

@animals_blueprint.route("/animals/")
def animals_page():
    animals = animal_repository.select_all_animals()
    return render_template("/animals/index.html", animals = animals)

@animals_blueprint.route("/animals/new")
def new_animal():
    return render_template("/animals/new.html")

@animals_blueprint.route("/animals/", methods=["POST"])
def add_animal():
    name = request.form["name"]
    type = request.form["type"]
    dob = request.form["dob"]
    age = request.form["age"]
    notes = request.form["notes"]
    owner = request.form["owner"]
    owner_tel = request.form["owner_tel"]
    owner_email = request.form["owner_email"]
    vet_id = request.form["vet_id"]
    vet = vet_repository.select(vet_id)
    new_animal = Animal(name, type, dob, age, notes, owner, owner_email, owner_tel, vet)
    animal_repository.save(new_animal)
    return redirect("/animals")