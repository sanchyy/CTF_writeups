# Glory of the Garden



## Procedure

![garden]()

When I first see a photo in a forensics CTF problem I think about metadata, strings, etc. 
In this case I started trying to see if there is something hidden in this image strings, typing: `strings garden.jpg`. We'll get an output like this:

```
...
V8L;
<]zV&
ZqKvu
7g4js'
wae:uc(>YwG
6	`A
xhS~
wM=GV
gDau%~
,~J|
u)(])F
={~5
h--@3
cZi-
M(.I
]hWP&
jc#k
=7g&
mjx/
s\]|."Ue
\qZf
Here is a flag "picoCTF{more_than_m33ts_the_3y3f089EdF0}"
```

So, he've just found it easier than we thought

## Flag

`picoCTF{more_than_m33ts_the_3y3f089EdF0}`
