import time
import sys
import rich


rich.print("""[bold][white][+] - Welcome To The Rubi[cyan]X[white]gram
[white][+] - Coding time : [green]30/8/2024
[white][+] - [yellow]Developer [white]Library : [red]@StreamX
[white][+] - Library version : [blue]3.7.4
[white][+] - Support : [red]@Off_coder [white],[red] @StreamX [white]
[white][+] - Channel : [blue]https://rubika.ir/RubiXgram1  """)
def time_loading(duration):
    ami = "/—\\|"
    print("\n")
    for i in range(duration):
        for amir in ami:
            sys.stdout.write('\r' + ' Booting Rubi\033[96mX\033[00mgram ' + amir)
            sys.stdout.flush()
            time.sleep(0.08)

time_loading(3)
print("\n —————————————————————————————\n")