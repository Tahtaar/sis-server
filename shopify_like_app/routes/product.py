from flask import Blueprint, request, jsonify
from models import db, Product
from flask_jwt_extended import jwt_required

product_bp = Blueprint('product', __name__)

@product_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = [{'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description} for product in products]
    return jsonify(product_list), 200

@product_bp.route('/', methods=['POST'])
@jwt_required()
def add_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    
    new_product = Product(name=name, price=price, description=description)
    db.session.add(new_product)
    db.session.commit()
    
    return jsonify({'message': 'Product added successfully'}), 201
