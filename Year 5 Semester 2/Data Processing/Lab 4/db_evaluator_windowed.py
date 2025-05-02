import faust
from datetime import timedelta

import utils.consts as consts
from db_model import Solar

app = faust.App("lab4_t1-2_windowed_v12", store="memory://")

main_data_topic = app.topic(consts.topics.DB, value_type=Solar)

# Tumbling window table: sum of solar capacity per year, per 30-second window
capacity_by_year = app.Table(
    "capacity_by_year_windowed_v12",
    default=float,
    partitions=8,
).tumbling(timedelta(seconds=5), expires=timedelta(seconds=10))

# Tumbling window table: count of low capacity entries, per 30-second window
low_entries = app.Table(
    "low_entries_windowed_v12",
    default=int,
    partitions=8,
).tumbling(timedelta(seconds=5), expires=timedelta(seconds=10))


# Sum solar_capacity by year (2018–2020), grouped and windowed
@app.agent(main_data_topic)
async def sum_by_year(stream: faust.Stream):
    await main_data_topic.declare()
    async for event in stream.group_by(Solar.year):
        if 2018 <= int(event.year) <= 2020:
            capacity_by_year[event.year] += event.solar_capacity
            print(
                f"Windowed capacity for year {event.year}: {capacity_by_year[event.year].now()}"
            )


# Count entries with solar_capacity < 10, windowed
@app.agent(main_data_topic)
async def count_low_capacity(stream: faust.Stream):
    await main_data_topic.declare()
    async for event in stream:
        if float(event.solar_capacity) < 10:
            low_entries[0] += 1
            print(f"Low capacity count in current window: {low_entries[0].now()}")


if __name__ == "__main__":
    app.main()
