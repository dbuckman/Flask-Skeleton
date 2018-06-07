import os, json

BASE_DIR = os.path.dirname(os.path.abspath("__file__"))

#Cross-Site Request Forgery
CSRF_ENABLED = True

# Generate a secret random key for the session
#SECRET_KEY = os.urandom(24)
# Or set a key for session (cookie) encryption
SECRET_KEY = "someRandomString"

STATIC_FOLDER = BASE_DIR + "/app/static"

# get service information if on Bluemix, or set them
if 'VCAP_SERVICES' in os.environ:
    VCAP_APPLICATION = json.loads(os.environ['VCAP_APPLICATION'])
    for uri in VCAP_APPLICATION["application_uris"]:
        # The deployment scripts I use adds a -new to the hostname that should be removed
        if "-new" in uri:
            BASE_URL = "https://" + str(uri.replace("-new", ""))
            break
        else:
            BASE_URL = "https://" + str(uri)
            break
    dbinfo = json.loads(os.environ['VCAP_SERVICES'])['elephantsql'][0]
    dbcred = dbinfo["credentials"]
    DB_URI = dbinfo['credentials']['uri']
else:
    #If there is no VCAP_SERVICES you are most likely running local
    VCAP_APPLICATION = "None"
    try:
        with open('local-vcap.json') as data_file:
            vcap = json.load(data_file)
        vcap = vcap['VCAP_SERVICES']
    except:
        print("Error!!! Can not load VCAP from OS ENV or local-vcap.json file")
        vcap = None
    try:
        with open('local-vcap-app.json') as data_file:
            VCAP_APPLICATION = json.load(data_file)
        for uri in VCAP_APPLICATION["application_uris"]:
            if "-new" in url:
                pass
            else:
                BASE_URL = "http://" + str(uri)
                break
    except:
        print("Error!!! Can not load VCAP from OS ENV or local-vcap-app.json file")
        print("Assumeing BASE_URL = 127.0.0.0:5000")
        BASE_URL = "https://127.0.0.1:5000"

    if vcap != None:
        #pull connection info from vcap file or comment and use a local sqlite DB
        dbinfo = vcap['elephantsql'][0]
        DB_URI = dbinfo['credentials']['uri']
    else:
        DB_URI = 'sqlite:///tmp.db'


