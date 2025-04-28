import faust

import utils.consts as consts
from db_model import Solar


app = faust.App("lab4_t1-2_v12", consumer_auto_offset_reset="latest", store="memory://")
main_data_topic = app.topic(consts.topics.DB, value_type=Solar)
capacity_by_year = app.Table("capacity_by_year_v12", default=float, partitions=8)
low_entries = app.Table("low_entries_v12", default=int, partitions=8)


# sum of solar_capacity by year
@app.agent(main_data_topic)
async def sum_by_year(stream: faust.Stream):
    await main_data_topic.declare()
    event: Solar
    # async for event in stream.group_by(Solar.year):
    async for event in stream.group_by(Solar.year):
        if 2018 <= int(event.year) <= 2020:
            capacity_by_year[event.year] += event.solar_capacity
            print(f"{capacity_by_year[event.year] = }")


# count entries with solar_capacity < 10
@app.agent(main_data_topic)
async def count_low_capacity(stream: faust.Stream):
    await main_data_topic.declare()
    event: Solar
    # cant group by floats for some reason
    async for event in stream:
        if float(event.solar_capacity) < 10:
            low_entries[0] += 1
            print(f"{low_entries[0] = }")


if __name__ == "__main__":
    app.main()
