import faust

import utils.consts as consts


app = faust.App("t3_brancher")


@app.agent(app.topic(consts.TOPICS["random"]))
async def process(stream):
    async for key, event in stream.items():
        if event["solar_capacity"] >= 400:
            topic = consts.TOPICS["b1"]
        elif event["solar_capacity"] >= 200:
            topic = consts.TOPICS["b2"]
        else:
            topic = consts.TOPICS["b3"]

        print(f"{topic = } | {event = }")

        await app.topic(topic).send(key=key, value=event)


if __name__ == "__main__":
    app.main()
