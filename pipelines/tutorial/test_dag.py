from datetime import datetime, timedelta
from textwrap import dedent

import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

from utils.callbacks import failure_callback, success_callback

