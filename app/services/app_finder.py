import os
import glob
import json


APP_DATABASE = "app/services/apps.json"



# Fixed important apps

PRIORITY_APPS = {


    "steam":

        r"C:\Program Files (x86)\Steam\steam.exe",



    "discord":

        r"C:\Users\harsh\AppData\Local\Discord\Update.exe",



    "daysgone":

        r"C:\Games\Days Gone\BendGame\Binaries\Win64\DaysGone.exe",



    "batman":

        r"C:\Games\Batman - Arkham Knight\Binaries\Win64\BatmanAK.exe",



    "thecrew2":

        r"C:\Games\The Crew 2\TheCrew2.exe",



    "edge":

        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",



    "microsoftedge":

        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

}





SEARCH_LOCATIONS = [


    r"C:\Program Files",


    r"C:\Program Files (x86)",


    r"C:\Windows\System32",


    os.path.expandvars(
        r"%LOCALAPPDATA%"
    ),


    os.path.expandvars(
        r"%APPDATA%"
    ),


    r"C:\Games",


    os.path.expandvars(
        r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs"
    ),


    os.path.expandvars(
        r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"
    )

]





def clean_name(name):

    return (

        name.lower()

        .replace(" ", "")

        .replace("-", "")

        .replace("_", "")

    )





def scan_apps():


    print("Scanning applications...")


    apps = {}



    for location in SEARCH_LOCATIONS:



        if not os.path.exists(location):

            continue



        for exe in glob.iglob(

            location + r"\**\*.exe",

            recursive=True

        ):



            try:



                if not os.path.isfile(exe):

                    continue



                filename = os.path.basename(exe)



                name = os.path.splitext(filename)[0]



                clean = clean_name(name)



                ignore = [

                    "uninstall",

                    "update",

                    "setup",

                    "crash",

                    "helper",

                    "report",

                    "installer"

                ]



                if any(

                    word in clean

                    for word in ignore

                ):

                    continue



                apps[clean] = exe



                folders = exe.split("\\")



                for folder in folders:



                    folder_clean = clean_name(folder)



                    if len(folder_clean) > 3:



                        if folder_clean not in apps:

                            apps[folder_clean] = exe



            except:


                pass





    os.makedirs(

        os.path.dirname(APP_DATABASE),

        exist_ok=True

    )




    with open(

        APP_DATABASE,

        "w"

    ) as file:



        json.dump(

            apps,

            file,

            indent=4

        )




    print(

        "Apps found:",

        len(apps)

    )



    return apps





def load_apps():


    if not os.path.exists(APP_DATABASE):

        return scan_apps()



    try:



        with open(

            APP_DATABASE,

            "r"

        ) as file:



            data = json.load(file)



            if not data:

                return scan_apps()



            return data



    except:



        print(

            "Database damaged. Rebuilding..."

        )



        return scan_apps()





def find_app(name):


    search = clean_name(name)



    # Priority apps first

    if search in PRIORITY_APPS:



        path = PRIORITY_APPS[search]



        if os.path.exists(path):

            return path





    apps = load_apps()





    # Exact match

    if search in apps:



        path = apps[search]



        if os.path.isfile(path):

            return path





    # Filename match

    for app, path in apps.items():



        filename = clean_name(

            os.path.splitext(

                os.path.basename(path)

            )[0]

        )



        if search == filename:



            if os.path.isfile(path):

                return path





    # Partial match

    for app, path in apps.items():



        filename = clean_name(

            os.path.splitext(

                os.path.basename(path)

            )[0]

        )



        if (

            search in filename

            and len(search) >= 4

        ):



            if os.path.isfile(path):

                return path





    return None