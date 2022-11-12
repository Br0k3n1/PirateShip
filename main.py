import checker as c
import threading
import sys

if len(sys.argv) < 2:
    print(f"\nERROR: No Game Was Included")
if len(sys.argv) > 2:
    print(f"\nERROR: Just Include Game Name\n")
else:
    funcs_names = ['crackhub', 'csrinru', 'darck', 'downloadha', 'elamigos', 'fitgirl', 'gload', 'gnarly', 'online_fix', 'ova', 'rlsbb', 'scene_crackhub', 'scnlog', 'scooter', 'steamrip']
    funcs = [c.crackhub, c.csrinru, c.darck, c.downloadha, c.elamigos, c.fitgirl, c.gload, c.gnarly, c.online_fix, c.ova, c.rlsbb, c.scene_crackhub, c.scnlog, c.scooter, c.steamrip]

    print("")

    threads = []

    for func in funcs:
        t = threading.Thread(target=func, args=(sys.argv[1],))
        t.daemon = True
        threads.append(t)
    for i in range(len(funcs)):
        threads[i].start()
    for i in range(len(funcs)):
        threads[i].join() 
