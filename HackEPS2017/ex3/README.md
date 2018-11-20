## Third Challenge

Teniendo en mente un teclado numérico de teléfono móvil. 
![teclado](http://challenge.semicinternet.com/reto-3/reto-3/220pxTelephonekeypad2.svg.png)

Al tener que comunicarse con nosotros, les ayudaremos a que sean un poco más modernos y vamos a hacer que nuestro programa codifique las abreviaturas más conocidas. Esta es la tabla de las que tenemos que interpretar:

```
que -> k
adios -> dw
que tal	-> ktal
tkm te quiero -> mucho
gracias	-> thx
besos y abrazos	-> xoxo
que carajo -> wtf

```
Debes tener en cuenta otra cosa, y es que a nuestros abuelos les cuesta bastante escribir y tienen una especial predilección por la tecla espacio, por lo tanto, es bastante probable que el texto de entrada tenga muchos espacios sobrantes entre palabras. Si nos encontramos más de un espacio entre dos palabras, sólo tienes que codificar uno. Si está al principio de la frase, debes ignorarlo todo.

Por ejemplo, la palabra hola la codificaremos con 446665552

```
HackEPS se traduciría en #44#2 22255#337 7777
```
Y para terminar, también nos han pedido otra pequeña ayuda. Tenemos que indicarles el movimiento a realizar con el dedo para que puedan encontrar la tecla siguiente de la forma más ágil posible para que no pierdan demasiado tiempo. Vamos a escribir el movimiento que deben realizar. Esto se explica mejor con un ejemplo:

HackEPS se traduce definitivamente en:
```
# arriba arriba izquierda izquierda 44 abajo abajo derecha derecha # arriba arriba arriba izquierda 2 222 abajo 55 abajo abajo derecha # arriba arriba arriba 33 abajo abajo izquierda izquierda 7 7777
```
