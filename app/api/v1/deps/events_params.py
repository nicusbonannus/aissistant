from datetime import date, datetime, timedelta

from pydantic import BaseModel, Field
from pydantic.v1 import root_validator


class RequestByDateRangeParams(BaseModel):
    start: datetime = Field(
        default_factory=lambda: datetime.combine(date.today(), datetime.min.time())
    )
    end: datetime = Field(
        default_factory=lambda: datetime.combine(date.today(), datetime.min.time())
        + timedelta(days=1)
    )

    @root_validator
    def check_dates(cls, values):
        start = values.get("start")
        end = values.get("end")
        if start > end:
            raise ValueError("Start date must be before end date")
        if (end - start).days < 0:
            raise ValueError("The date range must be at least for one day")
        if (end - start).days > 7:
            raise ValueError("You cannot analyze more than 7 days")
        return values
