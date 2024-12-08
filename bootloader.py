# !!!!! Old Loader !!!!!

# import time
# import sys
# import rich


# rich.print("""[bold][white][+] - Welcome To The Rubi[cyan]X[white]gram
# [white][+] - Coding time : [green]30/8/2024
# [white][+] - [yellow]Developer [white]Library : [red]@StreamX
# [white][+] - Library version : [blue]6.7.11
# [white][+] - Support : [red]@Off_coder [white],[red] @StreamX [white]
# [white][+] - Channel : [blue]https://rubika.ir/RubiXgram1  """)
# def time_loading(duration):
#     ami = "/—\\|"
#     print("\n")
#     for i in range(duration):
#         for amir in ami:
#             sys.stdout.write('\r' + ' Booting Rubi\033[96mX\033[00mgram ' + amir)
#             sys.stdout.flush()
#             time.sleep(0.08)

# time_loading(3)
# print("\n —————————————————————————————\n")

from rich.console import Console
from rich.spinner import Spinner
import time

console = Console()
spinner = Spinner("dots")

with console.status("[bold white]Booting [bold cyan]RubiXgram :butterfly:") as status:
    console.print(spinner)
    time.sleep(1.2)
