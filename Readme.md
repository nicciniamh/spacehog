# Spacehog
Python Script to find disk space 'hogs'


## Usage

 *spacehog* [-h] [--count number] [--ignore filename][--mounted] [--quiet] [dir] 
 
Program arguments

*--count*  number of directories to display (may be less if there arent that many)
 		
*--ignore* file with list of regular expressions (or plain text) of paths to ignore
 		
*--mounted* scan mounted filesystems. Default is to not traverse mounted file systems.

*--quiet* prevents scanning status messages. 

*[dir]* Optional directory to scan or current working directory if not specified.

# Description
*Spacehog* attempts to located files and directories under *dir* and calculate, based on file size, the usage and reports the top *count* directories.

This program is generally pretty quick depending on disk type and processor speed. 

## Excluding Directories
By default, *spacehog* looks for a file called .spacehog.ignore which is one or more lines of regular expressions, representing directories to exclude. To override this file, specify --ignore and the path of the ignore list. This file is either an absolute path or relative to the path being examined. If '--ignore none' is used, no ignore list will be used and all directories will be examined.

## Mounted File Systems
By default, *spacehog* will not traverse mounted filesystems. This is done using *os.path.ismount* and may fail on some systems (notably *MacOS* where some Volumes do not appear as mounts). To force *spacehog* to follow these mounts, use the --mounted flag. This may or may not work with NTFS volume mounted on a particular directory. 

## Quiet Mode
By default, *spacehog* displays it's progress/status when scanning directories. To prevent this, use gthe --quiet option. This is useful if you want a report generrated. 

### Sample Output
<pre>
Top 10 Space Hogging directories in /
   Size Path
======= ========
 10.1Gb webroot
  1.2Gb usr
351.4Mb var
181.8Mb lib
128.8Mb sbin
 75.3Mb boot
 31.2Mb etc
 21.0Mb bin
851.6kb home
167.0kb lib64
</pre>