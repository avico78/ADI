from typing import Optional,Union,Dict

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from app_monitor.app_db import BaseMeta


import ormar 
import sqlalchemy
from sqlalchemy import DateTime
import datetime
import pydantic


class AdiAllRun(ormar.Model):
    class Meta(BaseMeta):
        tablename: str = "adi_all_run"

    run_id: int = ormar.Integer(primary_key=True)
    completed: bool = ormar.Boolean(default=False)
    name: str = ormar.String(max_length=100)
    start_run: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    end_run: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)


class AdiCustomer(ormar.Model):
    class Meta(BaseMeta):
        tablename: str = "adi_customer"

    adi_identifier: int = ormar.Integer(primary_key=True)
    customer_id: int = ormar.Integer()
    run_id: int = ormar.ForeignKey(AdiAllRun)
    status: str = ormar.String(max_length=100)
    completed: bool = ormar.Boolean(default=False)
    start_run: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    end_run: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)

class AdiRule(ormar.Model):
    class Meta(BaseMeta):
        tablename: str = "adi_rule"

    adi_identifier: int = ormar.Integer(primary_key=True)
    rule_id: int 
    start_run: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    end_run: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    status: str = ormar.String(max_length=100)    
    adi_customer: Optional[Union[AdiCustomer,Dict]] = ormar.ForeignKey(AdiCustomer)
