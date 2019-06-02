# CompiladorGraicer
Repositório para o compilador da matéria Lógica da Computação

Diagrama Sintático atual:

![diagrama](https://github.com/guizg/CompiladorGraicer/blob/master/diagramaSintatico.jpeg)

comandos = “Begin”, “\n”, comando, “\n”, { comando, “\n” }, “End” ;
comando = atribuição | print | comandos ;
atribuição = identificador, “=”, expressão ;
expressão = termo, { (“+” | “-”), termo } ;
termo = fator, { (“*” | “/”), fator } ;
fator = (“+” | “-”), fator | número | “(”, expressão, “)” | identificador ;
identificador = letra, { letra | digito | “_” } ;
número = dígito, { dígito } ;
letra = ( a | ... | z | A | ... | Z ) ;
dígito = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
