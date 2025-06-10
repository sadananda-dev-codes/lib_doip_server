import asyncio
from doip_services.routine.doip_routine_functions import _check_memory_routine

print('Jai Sadananda Maharaj')

async def control_routine_services():

    print('entering control routine services')

    task = asyncio.create_task(_check_memory_routine())
    await asyncio.sleep(2)

    print(f"Task done  {task.done()}")
    print(f"Task cancelled  {task.cancelled()}")
    print('exiting control routine services')

    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Caught cancellation")

    print(f"Task done {task.done()}")
    print(f"Task cancelled {task.cancelled()}")

asyncio.run(control_routine_services())

