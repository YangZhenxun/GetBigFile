#import pkg_resources
from importlib import metadata
from subprocess import call
import asyncio

packages = [dist for dist in metadata.packages_distributions().values()]
hhh = []
print(packages)

async def hh(dt):
    call("pip install --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple " + dt, shell=True)


async def amain():
    for package in packages:
        for dt in package:
            hhh.append(asyncio.create_task(hh(dt)))
    await asyncio.gather(*hhh)
asyncio.run(amain())
