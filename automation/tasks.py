import asyncio  # Import asyncio

async def MyFunc(consumer_instance):

    await consumer_instance.send_alert("started...")

    await asyncio.sleep(3)  # Use asyncio.sleep instead of time.sleep
    await consumer_instance.send_alert("anotherFunc has been completed.")

    await asyncio.sleep(5)  # Use asyncio.sleep instead of time.sleep
    await consumer_instance.send_alert("anotherFunc2 has been completed.")
    
    await asyncio.sleep(3)  # Use asyncio.sleep instead of time.sleep
    await consumer_instance.send_alert("anotherFunc3 has been completed.")
