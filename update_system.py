import pathlib, os, shutil, getpass
from pathlib import Path
# os.getenv("HOME") + "/.librewolf/" + librewolf_instance +  "/favicons.sqlite"
#isFile = os.path.isfile(librewolf1)
root_enabled = True
if not getpass.getuser() == "root":
    print("This script requires root permissions to run")
    root_enabled = False

# Get file paths to the package managers
apt_exists = shutil.which("apt")
pacman_exists = shutil.which("pacman")
snap_exists = shutil.which("snap")
flatpak_exists = shutil.which("flatpak")
dnf_exists = shutil.which("dnf")
yum_exists = shutil.which("yum")

# this only exists to provide a gurantee non existant path, which is needed in order to properly detect if the actual package managers exist
dummy = shutil.which("tgaaoiwaga52agaskgawn/joaguiahdnsllaigwhi")

# print(dummy)
# print(str(flatpak_exists))

# Run update programs
if root_enabled == True:
    if not pacman_exists == dummy: # Pacman
        os.system(str(pacman_exists) + " -Syu")
    elif not apt_exists == dummy: # Apt
        os.system(str(apt_exists) + " update")
        os.system(str(apt_exists) + " upgrade")
    elif not dnf_exists == dummy: # Dnf
        os.system(str(dnf_exists) + " clean all")
        os.system(str(dnf_exists) + " check-update")
        os.system(str(dnf_exists) + " update")
    elif not yum_exists == dummy: # Yum
        os.system(str(yum_exists) + " clean all")
        os.system(str(yum_exists) + " check-update")
        os.system(str(yum_exists) + " update")
    if not flatpak_exists == dummy: # Flatpak
        os.system(str(flatpak_exists) + " update")
    if not snap_exists == dummy: # Snap
        os.system(str(snap_exists) + " refresh")
