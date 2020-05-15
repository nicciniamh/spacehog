![Spacehog](logo.png =480x336)
# Spacehog
Python Script to find disk space 'hogs'

## Installation
To install follow these steps:

    git clone https://github.com/nicciniamh/spacehog.git
    cp spacehog/spacehog ~/bin # or other directory on PAGH
    chmod 755 ~bin/spacehog

## Usage

 *spacehog* [-h] [--count number] [--ignore filename][--mounted] [--output filename] [--quiet] [dir] ... 
 
Program arguments

*--count*  number of directories to display (may be less if there arent that many)

*--ignore* file with list of regular expressions (or plain text) of paths to ignore
 		
*--mounted* scan mounted filesystems. Default is to not traverse mounted file systems.

*--output* filename. Write report to *filename*, implies --quiet as well.

*--quiet* prevents scanning status messages. 

*dir ..* one or more directories to scan. If not specified, current workng directory is used.

# Description
*Spacehog* attempts to located files and directories under *dir* and calculate, based on file size, the usage and reports the top *count* directories. Multiple directories may be specified. 

This program is generally pretty quick depending on disk type and processor speed. 

## Excluding Directories
By default, *spacehog* looks for a file called .spacehog.ignore which is one or more lines of regular expressions, representing directories to exclude. To override this file, specify --ignore and the path of the ignore list. This file is either an absolute path or relative to the path being examined. If '--ignore none' is used, no ignore list will be used and all directories will be examined.

## Mounted File Systems
By default, *spacehog* will not traverse mounted filesystems. This is done using *os.path.ismount* and may fail on some systems (notably *MacOS* where some Volumes do not appear as mounts). To force *spacehog* to follow these mounts, use the --mounted flag. This may or may not work with *NTFS* (Friends don't let friends use NTFS) volume mounted on a particular directory. 

## Quiet Mode
By default, *spacehog* displays it's progress/status when scanning directories. To prevent this, use gthe --quiet option. This is useful if you want a report generrated. 

## Examples
`spacehog --count=5 ~/Code` counts the top five directories in *~/Code*

`spacehog --count=20 --output=~/top20,txt /home/nicci` Produces a report of the top 20 disk hogs in */home/nicci*

`spacehog --ignore /home/nicci/ignorethese.txt /usr` Counts the top 10 disk consumers in /usr, ignoring paths in */home/nicci/ignorethese.txt*



### Sample Output

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

 
