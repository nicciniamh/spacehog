<img src="logo.png" style="height: 333; width: 640">
# Spacehog
Python Script to find disk space 'hogs'

## Requirements
* Python3
* *psutils (pip3 install psutils)
## Installation
To install follow these steps:

    git clone https://github.com/nicciniamh/spacehog.git
    cp spacehog/spacehog ~/bin # or other directory on PAGH
    chmod 755 ~bin/spacehog

## Usage

 *spacehog* [-h] [--count number] [--ignore filename][--mounted] [--showfs] [--output filename] [--quiet] [dir] ... 
 
### Program arguments

*--count*  number of directories to display (may be less if there arent that many)

*--ignore* file with list of regular expressions (or plain text) of paths to ignore
 		
*--mounted* scan mounted filesystems. Default is to not traverse mounted file systems.

*--output* filename. Write report to *filename*, implies --quiet as well.

*--quiet* prevents scanning status messages.

*--showfs* Show filesystem information. 

*dir ..* one or more directories to scan. If not specified, current workng directory is used.

# Description
*Spacehog* attempts to located files and directories under *dir* and calculate, based on file size, the usage and reports the top *count* directories. Multiple directories may be specified.

To create a report, use the --output file.ext option to write a report to file.ext. Reports are written with a timestamp in the banner.

To include filesystem information (free space, total space and percent free) use the --showfs option.  

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

      Top 10 Space Hogging directories in /Users/nicci
         Size Path
      ======= ====================================
       96.5Gb Pictures
       11.9Gb Music
        6.5Gb Library
      614.6Mb src
      504.4Mb Applications
      489.7Mb DAW data
      272.4Mb node_modules
      199.4Mb line6
      182.6Mb iCloud Drive (Archive) - 2
       61.5Mb Creative Cloud Files (archived) (2)
      
      	117.1Gb in 10 directories (85218 files)
      	/dev/disk0s2:	465.0Gb bytes total, 311.6Gb bytes free (67% free)
      		dir(s): /Users/nicci
 
Copyright &copy; 2020 Nicole Stevens. Code may be freely used. Please keep my copyright intact. 

For license see LICENSE. 
