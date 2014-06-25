install
url --url=http://download.englab.nay.redhat.com/pub/rhel/released/RHEL-6/6.5/Server/x86_64/os/
text
reboot
lang en_US.UTF-8
keyboard us
key --skip
network --bootproto dhcp
rootpw redhat
firewall --disabled
selinux --enforcing
timezone --utc Asia/Shanghai
firstboot --disable
bootloader --location=mbr --append="console=tty0 console=ttyS0,115200"
zerombr
clearpart --all --initlabel
part /boot --fstype=ext4 --size=500
part swap --size=2000
part / --fstype=ext4 --grow --size=5000
xconfig --startxonboot
poweroff

%packages
@base
@client-mgmt-tools
@core
@debugging
@basic-desktop
@desktop-debugging
@desktop-platform
@directory-client
@fonts
@general-desktop
@graphical-admin-tools
@input-methods
@internet-browser
@java-platform
@legacy-x
@network-file-system-client
@perl-runtime
@print-client
@remote-desktop-clients
@server-platform
@server-policy
@x11
mtools
pax
python-dmidecode
oddjob
wodim
sgpio
genisoimage
device-mapper-persistent-data
abrt-gui
samba-winbind
certmonger
pam_krb5
krb5-workstation
libXmu
perl-DBD-SQLite