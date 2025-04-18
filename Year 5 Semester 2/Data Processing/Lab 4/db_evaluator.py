import json
import datetime

import aiorun
from kstreams import create_engine, ConsumerRecord

import utils.consts as consts


stream_engine = create_engine(title="lab4-stream-engine")

total_capacity_in_preiod = 0
count_capacity = 0
count_capacity_in_period = 0
count_consumed = 0


@stream_engine.stream(topics=consts.TOPICS["total"], auto_offset_reset="earliest")
async def consume(cr: ConsumerRecord):
    global total_capacity_in_preiod
    global count_capacity
    global count_capacity_in_period
    global count_consumed

    payload = json.loads(cr.value.decode("utf-8"))

    if (
        datetime.datetime(day=1, month=1, year=2018)
        <= datetime.datetime.strptime(payload["date"], "%Y-%m-%d")
        <= datetime.datetime(day=31, month=12, year=2020)
    ):
        total_capacity_in_preiod += payload["solar_capacity"]

        if payload["solar_capacity"] < 10:
            count_capacity_in_period += 1

    if payload["solar_capacity"] < 10:
        count_capacity += 1

    count_consumed += 1
    print(f"Оброблено запис №{count_consumed}")


async def start():
    await stream_engine.start()


async def shutdown(loop):
    print(
        f"> Загалом вироблено енергії за 2018-2020 роки: {total_capacity_in_preiod}\n"
        + f"> Записів де об’єм виробленої сонячної енергії менше 10: {count_capacity}\n"
        + f"> Записів де об’єм виробленої сонячної енергії менше 10 за період 2018 та 2020 роки: {count_capacity_in_period}\n"
    )

    await stream_engine.stop()


if __name__ == "__main__":
    aiorun.run(start(), stop_on_unhandled_errors=True, shutdown_callback=shutdown)
