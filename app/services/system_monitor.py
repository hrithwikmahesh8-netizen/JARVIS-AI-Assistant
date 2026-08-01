import psutil
import platform



def monitor_command(command):

    command = command.lower().strip()




    # =========================
    # BATTERY
    # =========================

    if "battery" in command:


        battery = psutil.sensors_battery()



        if battery:


            return (

                f"Your battery is at "
                f"{battery.percent} percent."

            )


        else:


            return (

                "I cannot detect the battery."

            )





    # =========================
    # CPU
    # =========================

    if (

        "cpu" in command

        or

        "processor" in command

    ):


        usage = psutil.cpu_percent(

            interval=1

        )


        return (

            f"CPU usage is {usage} percent."

        )





    # =========================
    # RAM
    # =========================

    if (

        "ram" in command

        or

        "memory" in command

    ):


        ram = psutil.virtual_memory()



        used = round(

            ram.used / (1024**3),

            2

        )



        total = round(

            ram.total / (1024**3),

            2

        )



        return (

            f"You are using {used} GB "

            f"of RAM out of {total} GB."

        )





    # =========================
    # STORAGE
    # =========================

    if (

        "storage" in command

        or

        "disk" in command

    ):


        disk = psutil.disk_usage(

            "C:\\"

        )



        used = round(

            disk.used / (1024**3),

            2

        )



        total = round(

            disk.total / (1024**3),

            2

        )



        return (

            f"You have used {used} GB "

            f"out of {total} GB storage."

        )





    # =========================
    # SYSTEM INFO
    # =========================

    if "system" in command:


        return (

            f"You are running "

            f"{platform.system()} "

            f"{platform.release()}."

        )





    return None