#!/usr/bin/env python3
import os 
import subprocess 
import sys 
import pwd 
import json 


def args(): 
    pass 



def load_envos(username): 

    # Set env vars before launching Blender
    os.environ["BLENDER_USE_USD"] = "1"
    os.environ["PYTHONPATH"] = f"/Users/{username}/Desktop/USD_Bridge/modules:" + os.environ.get("PYTHONPATH", "")
    os.environ["USD_PLUGIN_PATH"] = f"/Users/{username}/Desktop/USD_Bridge/plugins"

def launch_blender(BLENDER_PATH,BRIDGE_SCRIPT,args): 


    command = [

    BLENDER_PATH,
    "--python", BRIDGE_SCRIPT
    ]

    try: 
        # Launch in detached mode (no terminal blocking)
        subprocess.Popen(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
            start_new_session=True  # Fully detached from parent shell
        )
        print("Listening on post 5566")
    except: 
        pass 

if __name__=="__main__": 
    user_id = os.getuid()
    username = pwd.getpwuid(user_id).pw_name
    gather_args = args() 

    BLENDER_PATH = "/Applications/Blender.app/Contents/MacOS/Blender"
    BRIDGE_SCRIPT = f"/Users/{username}/Desktop/USD_Bridge/src/run_in_blender.py"

    load_envos(username) 

    launch_blender(BLENDER_PATH, BRIDGE_SCRIPT, gather_args)

