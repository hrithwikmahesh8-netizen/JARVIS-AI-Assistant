import psutil



PROCESS_NAMES = {


    "discord": [

        "Discord.exe",

        "Update.exe"

    ],



    "steam": [

        "steam.exe",

        "steamwebhelper.exe"

    ],



    "chrome": [

        "chrome.exe"

    ],



    "edge": [

        "msedge.exe"

    ],



    "batman": [

        "BatmanAK.exe"

    ],



    "daysgone": [

        "DaysGone.exe"

    ],



    "thecrew2": [

        "TheCrew2.exe"

    ]

}





def close_process(app_name):


    app_name = (

        app_name

        .lower()

        .replace(" ", "")

        .replace("-", "")

    )



    if app_name not in PROCESS_NAMES:


        return False





    closed = False





    for process in psutil.process_iter(

        ["name"]

    ):



        try:



            name = process.info["name"]



            if name in PROCESS_NAMES[app_name]:



                process.kill()



                closed = True



        except:



            pass





    return closed