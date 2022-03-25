import pathlib, os, shutil, getpass, platform, random
from pathlib import Path
# os.getenv("HOME") + "/.librewolf/" + librewolf_instance +  "/favicons.sqlite"
#isFile = os.path.isfile(librewolf1)
root_enabled = False
os_supported = True
random_str = ''
if getpass.getuser() == "root":
    print("This script should NOT be run as root")
    if os.getenv("FORCE_ROOT") == "True":
        root_enabled = False
    else:
        root_enabled = True
if not platform.system() == "Linux":
    print("Your " + platform.system() + " system is not supported by this script!")
    os_supported = False

# Get file paths to the package managers
if os_supported == True:
    apt_exists = shutil.which("apt")
    pacman_exists = shutil.which("pacman")
    snap_exists = shutil.which("snap")
    flatpak_exists = shutil.which("flatpak")
    dnf_exists = shutil.which("dnf")
    yum_exists = shutil.which("yum")
    crew_exists = shutil.which("crew")
    yay_exists = shutil.which("yay")
    zypper_exists = shutil.which("zypper")


    # This is used to generate a gurantee non existant path
    for _ in range(10):
        random_num = random.randint(0, 77)
        random_str += (chr(random_num))
    dummy = shutil.which(random_str)

    # Run update programs
    if root_enabled == False:
        if not yay_exists == dummy: # Yay
            os.system(str(yay_exists) + " -Syu")
        elif not pacman_exists == dummy: # Pacman
            os.system("sudo " + str(pacman_exists) + " -Syu")
        elif not apt_exists == dummy: # Apt
            os.system("sudo " + str(apt_exists) + " update")
            os.system("sudo " + str(apt_exists) + " upgrade")
        elif not dnf_exists == dummy: # Dnf
            os.system("sudo " + str(dnf_exists) + " clean all")
            os.system("sudo " + str(dnf_exists) + " check-update")
            os.system("sudo " + str(dnf_exists) + " update")
        elif not crew_exists == dummy: # Chromebrew
            os.system(str(crew_exists) + " update'")
            os.system(str(crew_exists) + " upgrade'")
        elif not yum_exists == dummy: # Yum
            os.system("sudo " + str(yum_exists) + " clean all")
            os.system("sudo " + str(yum_exists) + " check-update")
            os.system("sudo " + str(yum_exists) + " update")
        elif not zypper_exists == dummy: # Yum
            os.system("sudo " + str(zypper_exists) + " ref")
            os.system("sudo " + str(zypper_exists) + " update")
        #
        if not flatpak_exists == dummy: # Flatpak
            os.system("sudo " + str(flatpak_exists) + " update")
        if not snap_exists == dummy: # Snap
            os.system("sudo " + str(snap_exists) + " refresh")
exit()
