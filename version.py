def verInfo():
    VERSIONINFO = {
    "Version Number": "0.0.2",
    "Author": "ComputerCrash0",
    "Completed Date" : "September 5, 2020",
    "Updated Date" : "October, 18, 2020"
    }

    for key, value in VERSIONINFO.items():
        print(f'{key}:{value}')


verInfo()