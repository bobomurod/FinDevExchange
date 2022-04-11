# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import asyncio
from api import run_api


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

async def main():
    await run_api()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
    event_loop.run_forever()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
