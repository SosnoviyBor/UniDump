import json
import datetime

import aiorun
from kstreams import create_engine, ConsumerRecord

import consts


stream_engine = create_engine(title="lab3-stream-engine")


@stream_engine.stream(topics="lab3-total", auto_offset_reset="earliest")
async def consume(cr: ConsumerRecord):
    payload = json.load(cr.value)

    # filter by date
    if (
        datetime.datetime(day=1, month=1, year=2018)
        <= datetime.datetime.strptime(payload["date"], "%Y-%m-%d")
        <= datetime.datetime(day=31, month=12, year=2020)
    ):
        await stream_engine.send(consts.TOPICS["by year"], value=cr.value)

    # separate by capacity
    if payload["solar_capacity"] < 10:
        await stream_engine.send(consts.TOPICS["capacity <10"], value=cr.value)
    elif 10 < payload["solar_capacity"] < 100:
        await stream_engine.send(consts.TOPICS["capacity 10-100"], value=cr.value)
    elif payload["solar_capacity"] > 100:
        await stream_engine.send(consts.TOPICS["capacity >100"], value=cr.value)


async def start():
    await stream_engine.start()


async def shutdown(loop):
    await stream_engine.stop()


if __name__ == "__main__":
    aiorun.run(start(), stop_on_unhandled_errors=True, shutdown_callback=shutdown)
