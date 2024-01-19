import checker as c
from art import tprint
import threading
import sys
import os

os.system('cls' if os.name == 'nt' else 'clear')

startup_pic = r"""
        ███████████████████████████
        ███████▀▀▀░░░░░░░▀▀▀███████
        ████▀░░░░░░░░░░░░░░░░░▀████
        ███│░░░░░░░░░░░░░░░░░░░│███
        ██▌│░░░░░░░░░░░░░░░░░░░│▐██
        ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
        ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
        ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
        ██▌░│██████▌░░░▐██████│░▐██
        ███░│▐███▀▀░░▄░░▀▀███▌│░███
        ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
        ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
        ████▄─┘██▌░░░░░░░▐██└─▄████
        █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
        ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
        █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
        ███████▄░░░░░░░░░░░▄███████
        ██████████▄▄▄▄▄▄▄██████████
        ███████████████████████████
""".center(50)

repack_title = r"""
  ____  _____ ____   _    ____ _  __
 |  _ \| ____|  _ \ / \  / ___| |/ /
 | |_) |  _| | |_) / _ \| |   | ' / 
 |  _ <| |___|  __/ ___ \ |___| . \ 
 |_| \_\_____|_| /_/   \_\____|_|\_\                                                          
"""

DDS_title = r"""
  ____  ____  ____  
 |  _ \|  _ \/ ___| 
 | | | | | | \___ \ 
 | |_| | |_| |___) |
 |____/|____/|____/                     
"""

misc_title = r"""
  __  __ ___ ____   ____ 
 |  \/  |_ _/ ___| / ___|
 | |\/| || |\___ \| |    
 | |  | || | ___) | |___ 
 |_|  |_|___|____/ \____|
"""

if len(sys.argv) > 2:
    print(f"\nERROR: Just Include Game Name\n")
    print("")
else: 
    if len(sys.argv) < 2:
        print(startup_pic)
        print('\n')
        game_name = input("     Enter The Name of Your Desired Game: ")
        print("")
    else:
        game_name = sys.argv[1]
    
    os.system('cls' if os.name == 'nt' else 'clear')

    funcs_names = ['csrinru', 'darck', 'downloadha', 'elamigos', 'fitgirl', 'gload', 'online_fix', 'ova', 'steamrip']
    repack_funcs = [c.darck, c.elamigos, c.fitgirl, c.dodi]
    DDS_funcs = [c.csrinru, c.downloadha, c.gload, c.ova, c.steamrip, c.scnlog]
    misc_funcs = [c.online_fix]

    print("")

    threads_repack = []
    threads_dds = []
    threads_misc = []

    print(f"\n\033[1;31m{repack_title}\033[00m\n")

    for func in repack_funcs:
        t = threading.Thread(target=func, args=(game_name,))
        t.daemon = True
        threads_repack.append(t)
    for i in range(len(repack_funcs)):
        threads_repack[i].start()
    for i in range(len(repack_funcs)):
        threads_repack[i].join() 

    print(f"\n\033[1;34m{DDS_title}\033[00m\n") 

    for func in DDS_funcs:
        t = threading.Thread(target=func, args=(game_name,))
        t.daemon = True
        threads_dds.append(t)
    for i in range(len(DDS_funcs)):
        threads_dds[i].start()
    for i in range(len(DDS_funcs)):
        threads_dds[i].join() 
    
    print(f"\n\033[1;32m{misc_title}\033[00m\n")

    for func in misc_funcs:
        t = threading.Thread(target=func, args=(game_name,))
        t.daemon = True
        threads_misc.append(t)
    for i in range(len(misc_funcs)):
        threads_misc[i].start()
    for i in range(len(misc_funcs)):
        threads_misc[i].join() 

print("")
