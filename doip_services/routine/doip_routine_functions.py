import asyncio

async def _check_memory_routine():

    '''
    RID = 0x021201
    time = 5seconds
    long
    response =  0x7101021201 9a d2 72 e7
    '''

    try:
        await asyncio.sleep(5)
    except asyncio.CancelledError:
        raise asyncio.CancelledError

async def _on_demand_self_test_routine():

    '''
    short
    RID = 0x0202
    time = 2 seconds
    response = 7101020222
    '''

    try:
        await asyncio.sleep(2)
    except asyncio.CancelledError:
        raise asyncio.CancelledError

async def _programming_preconditions_routine():

    '''
    RID = 0x0203
    time = 3
    short
    response = 710102031001
    '''

    try:
        await asyncio.sleep(3)
    except asyncio.CancelledError:
        raise asyncio.CancelledError

async def _check_upload_precondition_routine():

    '''
    RID = 0x05947600
    time = 8
    long
    response = 71010594763285
    '''

    try:
        await asyncio.sleep(8)
    except asyncio.CancelledError:
        raise asyncio.CancelledError

async def _complete_and_compatibility_check_routine():

    '''
    RID = 03 01 40 00 01 00  ### 40 00 01 00 is an address of the SBL
    time = 15
    response 71 01 03 01 10 ###
    long
    '''

    try:
        await asyncio.sleep(15)
    except asyncio.CancelledError:
        raise asyncio.CancelledError