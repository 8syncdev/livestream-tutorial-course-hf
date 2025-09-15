from faststream import FastStream
from faststream.kafka import KafkaBroker


broker = KafkaBroker("localhost:9092")

app = FastStream(broker=broker)

from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(..., examples="user0001")
    user_id: int = Field(..., examples=1)


@broker.subscriber("in_topic")
@broker.publisher("out_topic")
async def handle_msg(data: User) -> str:
    return f'User: {data.username}, id: {data.user_id}'


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.serve())