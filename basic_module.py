import instaloader
import os
import os.path


OUTPUT_RESULT = "/output"
USER = "sf_bp16"
PROFILE = ""


# function to create output dir
def createOutputDir():
    path = os.getcwd()
    path = path + OUTPUT_RESULT

    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Succesfully created the directory %s" % path)

# function to create ouput file
def createOutputFile(list_name):
    file = open(f"output/compare.txt", "a+")
    for i in list_name:
        file.write(i + '\n')

    file.close()

# function to get list of all followings by profile name
def getListFollowings(name):
    profile = instaloader.Profile.from_username(L.context, name)
    followings = []
    for i in profile.get_followees():
        followings.append(i.username)
    followings.sort()
    return followings

def getListCompareUsers(name1, name2):
    followings1 = getListFollowings(name1)
    followings2 = getListFollowings(name2)
    s1 = set(followings1)
    s2 = set(followings2)
    s3 = s1 & s2
    return s3

###         MAIN LOGIC         ###
if os.path.exists(OUTPUT_RESULT):
    print("Output folder already exists")
else:
    createOutputDir()

L = instaloader.Instaloader()
L.interactive_login(USER)

done_list = getListCompareUsers("saygashkina_victoria","zolotovvva")
createOutputFile(done_list)

print("Successfully exited from writing.")
