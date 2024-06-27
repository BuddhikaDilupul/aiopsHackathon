from datetime import datetime, timezone
from flask import Blueprint, jsonify, request
from pytz import timezone,utc
import logging
from app.services.count_service import create_count, get_latest_counter,get_latest_count
# from app.Auditorium import objectDetection
import logging

# Set up logging
logger = logging.getLogger(__name__)

# Create a Blueprint for the remediation routes
count_bp = Blueprint('count_bp', __name__)
@count_bp.route('/latest_counter', methods=['GET'])
def get_count():
    try:
        latest_counter = get_latest_counter()
        print(latest_counter)
        logger.info("Fetched all successfully")
        return jsonify(latest_counter), 200
    except Exception as e:
        logger.error(f"Error fetching problems: {str(e)}")
        return jsonify({"error": "Error fetching problems"}), 500
    
@count_bp.route('/counter', methods=['GET'])
def get_count_ui():
    try:
        latest_counter = get_latest_count()
        # print(latest_counter)
        logger.info("Fetched all successfully")
        return jsonify(latest_counter), 200
    except Exception as e:
        logger.error(f"Error fetching problems: {str(e)}")
        return jsonify({"error": "Error fetching problems"}), 500
    
@count_bp.route('/count', methods=['POST'])
def start():
    data = request.json
    count = data["people_count"]
    try:
        create_count(count)
        logger.info("Fetched all problems successfully")
        return jsonify("OK"), 200
    except Exception as e:
        logger.error(f"Error fetching problems: {str(e)}")
        return jsonify({"error": "Error fetching problems"}), 500
