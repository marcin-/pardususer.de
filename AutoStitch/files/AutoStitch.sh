#!/bin/bash
#
# ====================================================================================
# Starter file for MS Windows executables in a multi user operating system.
# (it's only useful, if you provide software packages for MS Windows applications)
#
# This script is made for work under Pardus GNU/Linux.
# But it should prinzipally work on other Linux distributions also.
# ====================================================================================
#
# Author:    Gürkan Zengin, áka "LinuxFanatic" <gurkan _AT_ pardususer _POINT_ de>
#
# Website:   PardusUser.de, do not hesitat to visit our portal at
#            http://www.pardususer.de/ :-)
#
# License:   GPLv2
#
# ====================================================================================
#

# For future use just modify variables below:
# VAR_WinExecAppName     --> Name of Application (usually it's also the same name under /opt/.../)
# VAR_WinExecName        --> Only filename of executable file
# VAR_WinExecStartParam  --> Do we need any parameters for starting? (if not, then leave it empty)

VAR_WinExecAppName="AutoStitch"

VAR_WinExecName="autostitch.exe"

VAR_WinExecStartParam="$(which wine) start /unix"





# At this point you don't have to change anything! ;-)
#========================================================================================================================#

# Check if application is started by normal user
if [ "$(id -u)" != "0" ]; then
	# Normal user, it's OK !
	# Check if application settings folder is already existing:
	if [ ! -d "$HOME/.$VAR_WinExecAppName" ]; then
		# No application settings in HOME found, so creating settings folder:
		mkdir -v "$HOME/.$VAR_WinExecAppName/"
		# Copy Application files recursively to settings folder in HOME:
		for DirectoryContent in $(ls "/opt/$VAR_WinExecAppName/"); do
			cp -Rv "/opt/$VAR_WinExecAppName/$DirectoryContent" "$HOME/.$VAR_WinExecAppName/"
		done
	else
		# It seems that application settings folder is existing ^^^
		# So check and sync content between Application files and settings folder in HOME, if needed:
		for DirectoryContent in $(ls "/opt/$VAR_WinExecAppName/"); do
			if [ ! -e "$HOME/.$VAR_WinExecAppName/$DirectoryContent" ]; then
				cp -Rv "/opt/$VAR_WinExecAppName/$DirectoryContent" "$HOME/.$VAR_WinExecAppName/"
			fi
		done
	fi
	# Modify file rights to 755 owner: read-write-execute, group: read-execute, others: read-execute
	chmod 0755 -Rv "$HOME/.$VAR_WinExecAppName/"
else
	# Application was stared with Root privileges --> Exit!!! (becuse security reasons)
	echo "Please don't start this software with Root rights!"
	exit 1
fi
cd "$HOME/.$VAR_WinExecAppName/"
exec $VAR_WinExecStartParam $VAR_WinExecName &
#========================================================================================================================#

exit 0