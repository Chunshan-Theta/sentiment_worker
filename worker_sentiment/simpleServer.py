import os
from util.aredis_queue import QueueRespondsTask
import asyncio
import logging
from util import Job
from sentiment import senti_level

ban_word_list = []
with open("./ban.txt") as f:
    for line in f.readlines():
        line = line.replace("\n","")
        ban_word_list.append(line)

def sentience_process(sentience):
    banToken = False
    for word in ban_word_list:
        if word in sentience:
            banToken = True

    if banToken:
        return (sentience, 0)
    else:
        return (sentience, senti_level(sentience))




async def main():
    async def __main_task__(job_obj: Job, QRTask):
        job_obj.content["result"] = []
        for s in job_obj.content["texts"]:
            job_obj.content["result"].append(sentience_process(s))
        #
        await QRTask.to_master(job_obj.to_json(), job_obj.request_id)


    QRTask1 = QueueRespondsTask(task_name)
    while True:
        logging.warning("get work....")
        task = await QRTask1.get_content()
        logging.warning(f"get QRTask1 work -> {task}")
        if task is not None:
            #
            obj = task.get("obj", None)
            request_id = task.get("request_id", None)
            job_obj = Job(request_id=request_id, content=obj)

            #
            await __main_task__(job_obj, QRTask1)


        #
        await asyncio.sleep(1)


task_name = os.getenv("task_name", "sentiment")
asyncio.run(main())
