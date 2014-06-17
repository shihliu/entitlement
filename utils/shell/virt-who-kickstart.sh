#! /bin/sh
# Check RHEL build, when new compose arrives:
# make sure repo/distros exist, add repo/profiles/ and repo/kickstarts/libvirt/RHEL[5,6,7]/ 

source comment-line.sh






star_line "check git repo"

if ! [ -d repo ]; then
    star_line "git repo not exist, cloning now"
    #git clone git+ssh://git@qe-git.englab.nay.redhat.com/~/repo/virt-qe/repo
fi

git pull

git status

create_profiles
create_kickstarts

git add *** ***

git commit -m "sdfsadf"

git push

exit $?