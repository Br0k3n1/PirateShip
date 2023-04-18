import checker as c
from art import tprint
import threading
import sys
import os

os.system('cls' if os.name == 'nt' else 'clear')

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

if len(sys.argv) < 2:
    print(f"\nERROR: No Game Was Included")
    print("")
elif len(sys.argv) > 2:
    print(f"\nERROR: Just Include Game Name\n")
    print("")
else:
    funcs_names = ['crackhub', 'csrinru', 'darck', 'downloadha', 'elamigos', 'fitgirl', 'gload', 'gnarly', 'online_fix', 'ova', 'scene_crackhub', 'scnlog', 'steamrip']
    repack_funcs = [c.darck, c.elamigos, c.fitgirl, c.gnarly]
    DDS_funcs = [c.crackhub, c.csrinru, c.downloadha, c.gload, c.ova, c.scnlog, c.steamrip, c.scene_crackhub]
    misc_funcs = [c.online_fix]

    print("")

    threads_repack = []
    threads_dds = []
    threads_misc = []

    print(f"\n\033[1;31m{repack_title}\033[00m\n")

    for func in repack_funcs:
        t = threading.Thread(target=func, args=(sys.argv[1],))
        t.daemon = True
        threads_repack.append(t)
    for i in range(len(repack_funcs)):
        threads_repack[i].start()
    for i in range(len(repack_funcs)):
        threads_repack[i].join() 

    print(f"\n\033[1;34m{DDS_title}\033[00m\n") 

    for func in DDS_funcs:
        t = threading.Thread(target=func, args=(sys.argv[1],))
        t.daemon = True
        threads_dds.append(t)
    for i in range(len(DDS_funcs)):
        threads_dds[i].start()
    for i in range(len(DDS_funcs)):
        threads_dds[i].join() 
    
    print(f"\n\033[1;32m{misc_title}\033[00m\n")

    for func in misc_funcs:
        t = threading.Thread(target=func, args=(sys.argv[1],))
        t.daemon = True
        threads_misc.append(t)
    for i in range(len(misc_funcs)):
        threads_misc[i].start()
    for i in range(len(misc_funcs)):
        threads_misc[i].join() 

print("")
