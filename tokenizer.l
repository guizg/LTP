// Adapted from https://gist.github.com/codebrainz/2933703

D			[0-9]
L			[a-zA-Z_]
H			[a-fA-F0-9]
E			([Ee][+-]?{D}+)
P                       ([Pp][+-]?{D}+)
FS			(f|F|l|L)
IS                      ((u|U)|(u|U)?(l|L|ll|LL)|(l|L|ll|LL)(u|U))

%{
#include <stdio.h>
#include "y.tab.h"

void count(void);
%}

%%
"/*"			{ comment(); }
"//"[^\n]*              { /* consume //-comment */ }

"A"             { count(); return(A);}
"funcao"        { count(); return(FUNCAO);}
"ira"           { count(); return(IRA);}
"usar"          { count(); return(USAR);}
"esses"         { count(); return(ESSES);}
"argumentos"    { count(); return(ARGUMENTOS);}
"e"             { count(); return(E);}
"fazer"         { count(); return(FAZER);}
"o"             { count(); return(O);}
"O"             { count(); return(O);}
"retorno"       { count(); return(RETORNO);}
"dela"          { count(); return(DELA);}
"do"            { count(); return(DO);}
"tipo"          { count(); return(TIPO);}
"seguinte"      { count(); return(SEGUINTE);}
"auto"			{ count(); return(AUTO); }
"_Bool"			{ count(); return(BOOL); }
"break"			{ count(); return(BREAK); }
"case"			{ count(); return(CASE); }
"char"			{ count(); return(CHAR); }
"_Complex"		{ count(); return(COMPLEX); }
"const"			{ count(); return(CONST); }
"continue"		{ count(); return(CONTINUE); }
"default"		{ count(); return(DEFAULT); }
"do"			{ count(); return(DO); }
"dobro"		{ count(); return(DOBRO); }
"senao"			{ count(); return(SENAO); }
"enum"			{ count(); return(ENUM); }
"extern"		{ count(); return(EXTERN); }
"ponto_flutuante" { count(); return(PONTO_FLUTUANTE); }
"for"			{ count(); return(FOR); }
"goto"			{ count(); return(GOTO); }
"se"			{ count(); return(SE); }
"_Imaginary"	{ count(); return(IMAGINARY); }
"inline"		{ count(); return(INLINE); }
"inteiro"   	{ count(); return(INTEIRO); }
"longo"			{ count(); return(LONGO); }
"register"		{ count(); return(REGISTER); }
"restrict"		{ count(); return(RESTRICT); }
"return"		{ count(); return(RETURN); }
"curto"			{ count(); return(CURTO); }
"com_sinal"		{ count(); return(COM_SINAL); }
"tamanho_de"	{ count(); return(TAMANHO_DE); }
"static"		{ count(); return(STATIC); }
"struct"		{ count(); return(STRUCT); }
"switch"		{ count(); return(SWITCH); }
"typedef"		{ count(); return(TYPEDEF); }
"union"			{ count(); return(UNION); }
"sem_sinal"		{ count(); return(SEM_SINAL); }
"nada"			{ count(); return(NADA); }
"volatile"		{ count(); return(VOLATILE); }
"enquanto"			{ count(); return(ENQUANTO); }

{L}({L}|{D})*		{ count(); return(check_type()); }

0[xX]{H}+{IS}?		{ count(); return(CONSTANT); }
0[0-7]*{IS}?		{ count(); return(CONSTANT); }
[1-9]{D}*{IS}?		{ count(); return(CONSTANT); }
L?'(\\.|[^\\'\n])+'	{ count(); return(CONSTANT); }

{D}+{E}{FS}?		{ count(); return(CONSTANT); }
{D}*"."{D}+{E}?{FS}?	{ count(); return(CONSTANT); }
{D}+"."{D}*{E}?{FS}?	{ count(); return(CONSTANT); }
0[xX]{H}+{P}{FS}?	{ count(); return(CONSTANT); }
0[xX]{H}*"."{H}+{P}?{FS}?     { count(); return(CONSTANT); }
0[xX]{H}+"."{H}*{P}?{FS}?     { count(); return(CONSTANT); }


L?\"(\\.|[^\\"\n])*\"	{ count(); return(STRING_LITERAL); }

"..."			{ count(); return(ELLIPSIS); }
">>="			{ count(); return(RIGHT_ASSIGN); }
"<<="			{ count(); return(LEFT_ASSIGN); }
"+="			{ count(); return(ADD_ASSIGN); }
"-="			{ count(); return(SUB_ASSIGN); }
"*="			{ count(); return(MUL_ASSIGN); }
"/="			{ count(); return(DIV_ASSIGN); }
"%="			{ count(); return(MOD_ASSIGN); }
"&="			{ count(); return(AND_ASSIGN); }
"^="			{ count(); return(XOR_ASSIGN); }
"|="			{ count(); return(OR_ASSIGN); }
">>"			{ count(); return(RIGHT_OP); }
"<<"			{ count(); return(LEFT_OP); }
"some_um_a"			{ count(); return(INC_OP); }
"tire_um_de"			{ count(); return(DEC_OP); }
"->"			{ count(); return(PTR_OP); }
"e"			{ count(); return(AND_OP); }
"||"			{ count(); return(OR_OP); }
"<="			{ count(); return(LE_OP); }
">="			{ count(); return(GE_OP); }
"igual_a"			{ count(); return(EQ_OP); }
"diferente_de"			{ count(); return(NE_OP); }
";"			{ count(); return(';'); }
("{"|"<%")		{ count(); return('{'); }
("}"|"%>")		{ count(); return('}'); }
","			{ count(); return(','); }
":"			{ count(); return(':'); }
"="			{ count(); return('='); }
"("			{ count(); return('('); }
")"			{ count(); return(')'); }
("["|"<:")		{ count(); return('['); }
("]"|":>")		{ count(); return(']'); }
"."			{ count(); return('.'); }
"&"			{ count(); return('&'); }
"!"			{ count(); retur	n('!'); }
"~"			{ count(); return('~'); }
"menos"			{ count(); return('-'); }
"mais"			{ count(); return('+'); }
"vezes"			{ count(); return('*'); }
"dividido_por"			{ count(); return('/'); }
"resto_da_divisao_por"			{ count(); return('%'); }
"<"			{ count(); return('<'); }
">"			{ count(); return('>'); }
"^"			{ count(); return('^'); }
"|"			{ count(); return('|'); }
"?"			{ count(); return('?'); }

[ \t\v\n\f]		{ count(); }
.			{ /* Add code to complain about unmatched characters */ }

%%

int yywrap(void)
{
	return 1;
}


void comment(void)
{
	char c, prev = 0;
  
	while ((c = input()) != 0)      /* (EOF maps to 0) */
	{
		if (c == '/' && prev == '*')
			return;
		prev = c;
	}
	error("unterminated comment");
}


int column = 0;

void count(void)
{
	int i;

	for (i = 0; yytext[i] != '\0'; i++)
		if (yytext[i] == '\n')
			column = 0;
		else if (yytext[i] == '\t')
			column += 8 - (column % 8);
		else
			column++;

	ECHO;
}


int check_type(void)
{
/*
* pseudo code --- this is what it should check
*
*	if (yytext == type_name)
*		return TYPE_NAME;
*
*	return IDENTIFIER;
*/

/*
*	it actually will only return IDENTIFIER
*/

	return IDENTIFIER;
}