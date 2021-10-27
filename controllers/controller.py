# from flask import render_template 
from app import app
from models.calculator import Calculator


@app.route('/add/<num1>/<num2>')
def add(num1,num2):
    return Calculator.addition(num1,num2)

@app.route('/subtract/<num1>/<num2>')
def subtract(num1,num2):
    return Calculator.subtraction(num1,num2)

@app.route('/multiply/<num1>/<num2>')
def mult(num1,num2):
    return Calculator.multiplication(num1,num2)

@app.route('/divide/<num1>/<num2>')
def divide(num1,num2):
    return Calculator.division(num1,num2)