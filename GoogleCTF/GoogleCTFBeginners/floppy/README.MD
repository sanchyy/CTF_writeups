# FLOPPY

```
file 4e69382f661878c7da8f8b6b8bf73a20acd6f04ec253020100dfedbd5083bb39

> 4e69382f661878c7da8f8b6b8bf73a20acd6f04ec253020100dfedbd5083bb39: Zip archive data, at least v2.0 to extract

```

you get a file called foo.ico

```
file foo.ico
> foo.ico: MS Windows icon resource - 1 icon, 32x32, 16 colors
```

the statement says that the '.ico file doesn't smile right' so let's take a look on it:

```
binwalk foo.ico

> 
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
765           0x2FD           Zip archive data, at least v2.0 to extract, compressed size: 123, uncompressed size: 136, name: driver.txt
956           0x3BC           Zip archive data, at least v2.0 to extract, compressed size: 214, uncompressed size: 225, name: www.com
1392          0x570           End of Zip archive

```
We see there is a driver.txt and a www.co files. we will unzip this

```
unzip foo.ico
cat driver.txt
>This is the driver for the Aluminum-Key Hardware password storage device.
     CTF{qeY80sU6Ktko8BJW}

In case of emergency, run www.com

```
