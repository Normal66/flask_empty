import json
import datetime
from flask import (current_app, Blueprint, request, jsonify,)
from .models import Melbet
from app.database import db
import logging

logger = logging.getLogger(__name__)

main_bp = Blueprint('main_bp', __name__, template_folder='templates',  static_folder='static', url_prefix='/api')


@main_bp.route('/db-init', methods=['GET'])
def db_init():
    return jsonify({'status': 'OK'})
