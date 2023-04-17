import checker as c
from colorama import Fore
from art import tprint
import threading
import sys

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

    print(Fore.RED)
    tprint("Repacks")
    print(Fore.RESET)

    for func in repack_funcs:
        t = threading.Thread(target=func, args=(sys.argv[1],))
        t.daemon = True
        threads_repack.append(t)
    for i in range(len(repack_funcs)):
        threads_repack[i].start()
    for i in range(len(repack_funcs)):
        threads_repack[i].join() 

    print(Fore.BLUE)
    tprint("DDS")
    print(Fore.RESET)

    for func in DDS_funcs:
        t = threading.Thread(target=func, args=(sys.argv[1],))
        t.daemon = True
        threads_dds.append(t)
    for i in range(len(DDS_funcs)):
        threads_dds[i].start()
    for i in range(len(DDS_funcs)):
        threads_dds[i].join() 
    
    print(Fore.GREEN)
    tprint("MISC")
    print(Fore.RESET)

    for func in misc_funcs:
        t = threading.Thread(target=func, args=(sys.argv[1],))
        t.daemon = True
        threads_misc.append(t)
    for i in range(len(misc_funcs)):
        threads_misc[i].start()
    for i in range(len(misc_funcs)):
        threads_misc[i].join() 

print("")
