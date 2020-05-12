# Insp3ctor problem

 we've recevied this url `https://2019shell1.picoctf.com/problem/11196/`.  

## 1st part of the flag

 First of all we take a look at the source code (with `ctrl + u`)  
 Taking a look at the html file we see this commented line `<!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->`

## 2nd Part
 
 We see it includes a css file called `mycss.css`, so we're gonna take a look at it's source code again.
 Taking a look we'll se a new line comented `/* You need CSS to make pretty pages. Here's part 2/3 of the flag: t3ct1ve_0r_ju5t */`

## 3rd part

 The last one is continuing the same procedure with the js file and we will see a new commented line:
 `/* Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?9df7e69a} */`

## Flag

`picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?9df7e69a}`
