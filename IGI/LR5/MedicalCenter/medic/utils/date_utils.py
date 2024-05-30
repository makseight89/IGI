from datetime import datetime
import calendar
import tzlocal
from ..models import Favor


def get_user_time():
    user_timezone = tzlocal.get_localzone()
    current_date = datetime.now(user_timezone).date()
    current_date_formatted = current_date.strftime("%d/%m/%Y")

    calendar_text = calendar.month(
        datetime.now(user_timezone).year,
        datetime.now(user_timezone).month,
    )

    return {
        "user_timezone": user_timezone,
        "current_date_formatted": current_date_formatted,
        "calendar_text": calendar_text,
    }


def get_favor_time(favor: Favor):
    user_timezone = tzlocal.get_localzone()
    created_tz = favor.created_at.astimezone(user_timezone).strftime(
        "%d/%m/%Y - %H:%M:%S"
    )
    updated_tz = favor.updated_at.astimezone(user_timezone).strftime(
        "%d/%m/%Y - %H:%M:%S"
    )
    created_utc = favor.created_at.strftime("%d/%m/%Y - %H:%M:%S")
    updated_utc = favor.updated_at.strftime("%d/%m/%Y - %H:%M:%S")
    return created_tz, updated_tz, created_utc, updated_utc
