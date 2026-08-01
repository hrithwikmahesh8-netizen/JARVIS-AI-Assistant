import os



def power_command(command):

    command = command.lower().strip()




    # =========================
    # SHUTDOWN
    # =========================

    if "shutdown" in command:


        os.system(

            "shutdown /s /t 5"

        )


        return "Shutting down the system."





    # =========================
    # RESTART
    # =========================

    if "restart" in command:


        os.system(

            "shutdown /r /t 5"

        )


        return "Restarting the system."





    # =========================
    # CANCEL SHUTDOWN
    # =========================

    if "cancel shutdown" in command:


        os.system(

            "shutdown /a"

        )


        return "Shutdown cancelled."





    # =========================
    # LOCK PC
    # =========================

    if "lock" in command:


        os.system(

            "rundll32.exe user32.dll,LockWorkStation"

        )


        return "Locking the system."





    # =========================
    # SLEEP
    # =========================

    if "sleep" in command:


        os.system(

            "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"

        )


        return "Entering sleep mode."





    return None