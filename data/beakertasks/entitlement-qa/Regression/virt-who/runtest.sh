#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /distribution/entitlement-qa/Regression/virt-who
#   Description: Run virt-who testing
#   Author: gao shang <sgao@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2014 Red Hat, Inc.
#
#   This program is free software: you can redistribute it and/or
#   modify it under the terms of the GNU General Public License as
#   published by the Free Software Foundation, either version 2 of
#   the License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be
#   useful, but WITHOUT ANY WARRANTY; without even the implied
#   warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#   PURPOSE.  See the GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program. If not, see http://www.gnu.org/licenses/.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Include Beaker environment
. /usr/bin/rhts-environment.sh || exit 1
. /usr/share/beakerlib/beakerlib.sh || exit 1

PACKAGE="entitlement-qa"

# decide if we're running standalone or in a Beaker instance
if test -z $JOBID ; then
        echo "Variable JOBID not set, assuming standalone"
        SERVERS="server-vm.example.com"
        CLIENTS="client-vm.example.com"
else
        echo "Variable JOBID set, we're running inside Beaker"
fi

rlJournalStart
    rlPhaseStartSetup
        rlRun "rm -rf ~/.ssh/known_hosts"
        rlRun "cat > /root/get-libvirt-repo.sh <<EOF
#!/usr/bin/expect 
spawn git clone git@qe-git.englab.nay.redhat.com:~/repo/hss-qe/entitlement/libvirt-test-API
expect \"yes/no\"
send \"yes\r\"
expect \"password:\"
send \"redhat\r\"
expect \"Resolving deltas: 100%\"
sleep 30
expect eof
EOF"
        rlRun "chmod 777 /root/get-libvirt-repo.sh"
        rlRun "cd /root/"
        rlRun "/root/get-libvirt-repo.sh" 0 "Git clone libvirt-test-API"
        rlRun "sleep 60"
    rlPhaseEnd

    rlPhaseStartTest
        rlRun "cd /root/libvirt-test-API"
        rlRun "echo \"Clients: $CLIENTS\""
        rlRun "echo \"Servers: $SERVERS\""
        rlRun "python excute/virtlab.py --handleguest=$HANDLEGUEST --samhostname=$SAMHOSTNAME --confile=$CONFILE --copyimages=$COPYIMAGES --samhostip=$SAMHOSTIP --targetmachine_ip=$CLIENTS --targetmachine_hostname=$CLIENTS --beaker=yes"
        #temporary method to show result
        for logfile in `ls -t -r result/default`
        do
            rlRun "cat result/default/$logfile"
        done
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "echo cleanup"
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
