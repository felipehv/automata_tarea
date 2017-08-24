# Tarea 1 Introduccion a la linguistica computacional.

## Requisitos
* Python >= 3.4

## Funcionamiento
* La programación de este autómata está basado en estados, tal como se vio en clases.
* Los estados representados son 6, desde q0 hasta q5.

## Estados
* q0: verifica solo el primer caracter, si es mayúscula pasa al estado q1, sino falla.
* q1: verifica el segundo caracter, la primera letra del apellido, si es minuscula pasa a q2, falla en caso contrario. 
* q2: verifica los caracteres pertenecientes al apellido, luego del primero de este. Si es minúscula, se mantiene en el estado q2 y pasa al siguiente caracter, si es mayúscula pasa al estado q3, si es un número pasa al estado q4.
* q3: verifica
* q4: 
* q5: 
