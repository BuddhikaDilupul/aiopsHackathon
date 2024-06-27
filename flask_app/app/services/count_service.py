from datetime import datetime, timedelta

from pytz import timezone
from app import db
from sqlalchemy.exc import SQLAlchemyError
import logging
from app.models.count_model import Counter

logger = logging.getLogger(__name__)
ist_timezone = timezone('Asia/Kolkata')
def create_count(data):
    print(data)
    try:
        for item in data:
            print(item)
            area = item["area"]
            count = item["count"]
            new_Counter = Counter(
                    count=count,
                    area= area,
                    time= datetime.now(ist_timezone).strftime('%Y-%m-%d %H:%M:%S'),
                )
            db.session.add(new_Counter)
            db.session.commit()
            logger.info("Created successfully")
        return None
    except SQLAlchemyError as e:
        db.session.rollback()
        logger.error(f"Error saving: {str(e)}")
        return {"error": str(e)}

def get_latest_counter():
    try:
        latest_count_X = db.session.query(Counter).filter_by(area='X').order_by(Counter.time.desc()).first()
        # latest_countsX['X'] = latest_count_X.count if latest_count_X else None        print(latest_counter)
        latest_count_Y = db.session.query(Counter).filter_by(area='Y').order_by(Counter.time.desc()).first()
        # latest_countsY['Y'] = latest_count_X.count if latest_count_X else None        print(latest_counter)
        return [{"area":"X","count":latest_count_X.count},{"area":"Y","count":latest_count_Y.count}]
    except Exception as e:
        print(f"Error fetching the latest counter: {e}")
        return None

def get_latest_count():
    try:
        latest_counts = {"X": [], "Y": []}
        now_ist = datetime.now(ist_timezone)

        # Calculate the time 5 minutes ago
        five_minutes_ago_str = now_ist - timedelta(minutes=5)

        # Format the time as a string (if needed)
        five_minutes_ago = five_minutes_ago_str.strftime('%Y-%m-%d %H:%M:%S')

        print(five_minutes_ago,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        # Query to get the records from the last 5 minutes
        latest_count_X = db.session.query(Counter).filter(
        Counter.area == 'X',
        Counter.time >= five_minutes_ago).order_by(Counter.time.desc()).all()
        if latest_count_X:
            for record in latest_count_X:
                latest_counts["X"].append({
                    "id": record.id,
                    "area": record.area,
                    "count": record.count,
                    "time": record.time.strftime('%Y-%m-%d %H:%M:%S')
                })

        # Get the last 60 records for area 'Y'
        latest_count_Y =  db.session.query(Counter).filter(
        Counter.area == 'Y',
        Counter.time >= five_minutes_ago).order_by(Counter.time.desc()).all()
        if latest_count_Y:
            for record in latest_count_Y:
                latest_counts["Y"].append({
                    "id": record.id,
                    "area": record.area,
                    "count": record.count,
                    "time": record.time.strftime('%Y-%m-%d %H:%M:%S')
                })

        return latest_counts
    except Exception as e:
        print(f"Error fetching the latest counter: {e}")
        return None
