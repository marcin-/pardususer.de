#!/bin/bash
#
# Starter file for Mobile Atlas Creator (mobac)
#
# Currently it seems that mobac is a "hard coded" software, which lacks support for a multi user system like GNU/Linux.
# The script below creates symlinks into the home directory of the user and starts mobac directly from the home directory.
# So we are goint to make a workaround ;-)
#

# Check if mobac is started by normal user
if [ "$(id -u)" == "0" ]; then
    # mobac was started with Root privileges --> Exit!!! (because of security reasons)
    echo "Please don't start this software with Root rights!"
    exit 1
fi

# normal user, OK
if [ ! -d "$HOME/.mobac" ]; then
    # No mobac settings (~/.mobac/) found, so creating settings folder:
    mkdir "$HOME/.mobac/"
    cp -Rf /opt/MobileAtlasCreator/* "$HOME/.mobac/"
else
    # Otherwise just "update" the content of .mobac/
    # At first check, if a release-info-file Named "PisiPackageRelease" is existing
    # INFO: PisiPackageRelease is a text file, which will be created automatically by actions.py routine durung build process ...
    #       PisiPackageRelease includes the release number of the PiSi package - this we need to compare/check, if the files
    #       under /opt/MobileAtlasCreator/ are newer then unter ~/.mobac/ ... ;-)
    if [ -f "$HOME/.mobac/PisiPackageRelease" ]; then
        # Okay there is a PisiPackageRelease, so compare the release number with /opt/MobileAtlasCreator/PisiPackageRelease
        if [ "$(cat $HOME/.mobac/PisiPackageRelease)" != "$(cat /opt/MobileAtlasCreator/PisiPackageRelease)" ]; then
            # It seems that both release numbers are different, so sync the files in $HOME/.mobac/ with the files in /opt/MobileAtlasCreator/
            cp -Rf /opt/MobileAtlasCreator/* "$HOME/.mobac/"
        fi
    else
        # No PisiPackageRelease found --> so sync the files in $HOME/.mobac/ with the files in /opt/MobileAtlasCreator/
        cp -Rf /opt/MobileAtlasCreator/* "$HOME/.mobac/"
    fi
fi


# Now when all done well, then we can start this Application! :-)

cd "$HOME/.mobac/"

exec sh start.sh &

exit 0