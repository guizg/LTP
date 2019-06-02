from Tokenizer import Tokenizer
from Token import Token
from PrePro import PrePro
from Node import *

class Parser:
    def parseProgram():
        children = []
        while Parser.tokens.actual.type == 'A':
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'FUNÇÃO':
                raise Exception("Cade o FUNÇÃO amigao? Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type == 'SEM':
                Parser.tokens.selectNext()
                children.append(Parser.parseSubDec())
            else:
                children.append(Parser.parseFuncDec())

            while Parser.tokens.actual.type == "BREAK":
                Parser.tokens.selectNext()

        children.append(Call("PRINCIPAL", []))

        return Program("program", children)

    def parseSubDec():
        
        if Parser.tokens.actual.type != 'RETORNO':
            raise Exception("Cade o RETORNO amigao? Line: {0}".format(str(Parser.line)))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'ID':
            raise Exception("Cade o ID amigao? Line: {0}".format(str(Parser.line)))
        name = Parser.tokens.actual.value
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'RECEBE':
            raise Exception("Cade o RECEBE amigao? Line: {0}".format(str(Parser.line)))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'OS':
            raise Exception("Cade o OS amigao? Line: {0}".format(str(Parser.line)))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'ARGUMENTOS':
            raise Exception("Cade o ARGUMENTOS amigao? Line: {0}".format(str(Parser.line)))
        Parser.tokens.selectNext()

        sub_children = []

        if Parser.tokens.actual.type != 'OPEN_PAR':
            raise Exception("Cade o '(' amigao? Line: {0}".format(str(Parser.line)))
        Parser.tokens.selectNext()

        first = True
        while Parser.tokens.actual.type != 'CLOSE_PAR':
            if first == False:
                if Parser.tokens.actual.type != 'COMMA':
                    raise Exception("Tava esperando uma vírgula aqui. Line: "+str(Parser.line))
                Parser.tokens.selectNext()
            if Parser.tokens.actual.type != 'ID':
                raise Exception("Tava esperando um ID aqui. Line: "+str(Parser.line))
            id = Id(Parser.tokens.actual.value, [])
            Parser.tokens.selectNext()
            
            if Parser.tokens.actual.type != 'COMO':
                raise Exception("Cade o COMO amigao? Line: "+str(Parser.line))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'UM':
                raise Exception("Cade o UM amigao? Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            sub_children.append(VarDec("vardec", [id, Parser.parseType()]))

            first = False

        if Parser.tokens.actual.type != 'CLOSE_PAR':
            raise Exception("Cade o ')' amigao? Line: {0}".format(str(Parser.line)))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'E':
            raise Exception("Cade o E amigao? Line: {0}".format(str(Parser.line)))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'FAZ':
            raise Exception("Cade o FAZ amigao? Line: {0}".format(str(Parser.line)))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'TWO_DOTS':
            raise Exception("Cade o : amigao? Line: {0}".format(str(Parser.line)))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'BREAK':
            raise Exception("Faltou quebrar a linha. Line: "+str(Parser.line))
        Parser.line += 1
        Parser.tokens.selectNext()

        children = []

        while Parser.tokens.actual.type != 'FIM':
            children.append(Parser.parseStatement())
            Parser.line +=1
            Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'FIM':
            raise Exception("Cade o FIM amigao? Line: "+str(Parser.line))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'DA':
            raise Exception("Cade o DA amigao? Line: {0}".format(str(Parser.line)))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'FUNÇÃO':
            raise Exception("Cade o FUNÇÃO amigao? Line: "+str(Parser.line))
        Parser.tokens.selectNext()
        
        stmts = Program("statements", children)

        sub_children.append(stmts)

        return SubDec(name, sub_children)

    def parseFuncDec():

        if Parser.tokens.actual.type != 'ID':
            raise Exception("Cade o ID amigao? Line: {0}".format(str(Parser.line)))
        name = Parser.tokens.actual.value
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'COMMA':
            raise Exception("Cade o COMMA amigao? Line: "+str(Parser.line))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'QUE':
            raise Exception("Cade o QUE amigao? Line: "+str(Parser.line))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'RECEBE':
            raise Exception("Cade o RECEBE amigao? Line: "+str(Parser.line))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'OS':
            raise Exception("Cade o OS amigao? Line: "+str(Parser.line))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'ARGUMENTOS':
            raise Exception("Cade o ARGUMENTOS amigao? Line: "+str(Parser.line))
        Parser.tokens.selectNext()

        func_children = []

        if Parser.tokens.actual.type != 'OPEN_PAR':
            raise Exception("Cade o '(' amigao? Line: {0}".format(str(Parser.line)))
        Parser.tokens.selectNext()

        first = True
        while Parser.tokens.actual.type != 'CLOSE_PAR':
            if first == False:
                if Parser.tokens.actual.type != 'COMMA':
                    raise Exception("Tava esperando uma vírgula aqui. Line: "+str(Parser.line))
                Parser.tokens.selectNext()
            if Parser.tokens.actual.type != 'ID':
                raise Exception("Tava esperando um ID aqui. Line: "+str(Parser.line))
            id = Id(Parser.tokens.actual.value, [])
            Parser.tokens.selectNext()
            
            if Parser.tokens.actual.type != 'COMO':
                raise Exception("Cade o COMO amigao? Line: "+str(Parser.line))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'UM':
                raise Exception("Cade o UM amigao? Line: "+str(Parser.line))
            Parser.tokens.selectNext()

            func_children.append(VarDec("vardec", [id, Parser.parseType()]))

            first = False

        if Parser.tokens.actual.type != 'CLOSE_PAR':
            raise Exception("Cade o ')' amigao? Line: {0}".format(str(Parser.line)))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'E':
            raise Exception("Cade o E amigao? Line: {0}".format(str(Parser.line)))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'RETORNA':
            raise Exception("Cade o RETORNA amigao? Line: "+str(Parser.line))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'UM':
            raise Exception("Cade o UM amigao? Line: "+str(Parser.line))
        Parser.tokens.selectNext()

        func_children.insert(0, Parser.parseType())

        if Parser.tokens.actual.type != 'COMMA':
            raise Exception("Cade o COMMA amigao? Line: "+str(Parser.line))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'FAZ':
            raise Exception("Cade o FAZ amigao? Line: "+str(Parser.line))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'TWO_DOTS':
            raise Exception("Cade o : amigao? Line: "+str(Parser.line))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'BREAK':
            raise Exception("Faltou quebrar a linha. Line: "+str(Parser.line))
        Parser.line += 1
        Parser.tokens.selectNext()

        children = []

        while Parser.tokens.actual.type != 'FIM':
            children.append(Parser.parseStatement())
            Parser.line +=1
            Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'FIM':
            raise Exception("Cade o FIM amigao? Line: "+str(Parser.line))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'DA':
            raise Exception("Cade o DA amigao? Line: "+str(Parser.line))
        Parser.tokens.selectNext()

        if Parser.tokens.actual.type != 'FUNÇÃO':
            raise Exception("Cade o FUNÇÃO amigao? Line: {0}".format(str(Parser.line)))
        Parser.tokens.selectNext()
        
        stmts = Program("statements", children)

        func_children.append(stmts)

        return FuncDec(name, func_children)
    

    def parseStatement():

        if Parser.tokens.actual.type == 'COLOQUE':
            Parser.tokens.selectNext()
            if Parser.tokens.actual.value != '{':
               raise Exception("Excpected a '{' here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()
            exp = Parser.parseRelExpression()
            if Parser.tokens.actual.value != '}':
               raise Exception("Excpected a '}' here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'NA':
               raise Exception("Excpected a NA here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'VARIÁVEL':
               raise Exception("Excpected a VARIÁVEL here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'ID':
               raise Exception("Excpected a ID here. Line: {0}".format(str(Parser.line)))
            iden = Id(Parser.tokens.actual.value, [])
            Parser.tokens.selectNext()
            return Assignment("=", [iden, exp])


        if Parser.tokens.actual.type == 'IMPRIMA':
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'NA':
               raise Exception("Excpected a NA here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'TELA':
               raise Exception("Excpected a TELA here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.value != '{':
               raise Exception("Excpected a '{' here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            exp = Parser.parseRelExpression()

            if Parser.tokens.actual.value != '}':
               raise Exception("Excpected a '}' here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            return Print("print", [exp])

        if Parser.tokens.actual.type == 'ENQUANTO':
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'A':
               raise Exception("Excpected a A here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'CONDIÇÃO':
               raise Exception("Excpected a CONDIÇÃO here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.value != '{':
               raise Exception("Excpected a '{' here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            exp = Parser.parseRelExpression()

            if Parser.tokens.actual.value != '}':
               raise Exception("Excpected a '}' here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'FOR':
               raise Exception("Excpected a FOR here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'VERDADEIRA':
               raise Exception("Excpected a VERDADEIRA here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'COMMA':
               raise Exception("Excpected a COMMA here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'FAÇA':
               raise Exception("Excpected a FAÇA here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'TWO_DOTS':
               raise Exception("Excpected a : here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'BREAK':
                raise Exception("Faltou quebrar a linha. Line: "+str(Parser.line))
            Parser.line += 1
            Parser.tokens.selectNext()

            staments = []

            while Parser.tokens.actual.type != 'FIM':
                staments.append(Parser.parseStatement())
                Parser.line +=1
                Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'FIM':
                raise Exception("Cade o FIM amigao? Line: "+str(Parser.line))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'DO':
               raise Exception("Excpected a DOM here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'ENQUANTO':
               raise Exception("Excpected a ENQUANTO here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()


            return WhileNode("while", [exp, Program("program_while", staments)])

        if Parser.tokens.actual.type == 'SE':
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'A':
               raise Exception("Excpected a A here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'CONDIÇÃO':
               raise Exception("Excpected a CONDIÇÃO here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.value != '{':
               raise Exception("Excpected a '{' here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            children = [Parser.parseRelExpression()]

            if Parser.tokens.actual.value != '}':
               raise Exception("Excpected a '}' here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'FOR':
               raise Exception("Excpected a FOR here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'VERDADEIRA':
               raise Exception("Excpected a VERDADEIRA here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'COMMA':
               raise Exception("Excpected a COMMA here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'FAÇA':
               raise Exception("Excpected a FAÇA here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'TWO_DOTS':
               raise Exception("Excpected a : here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'BREAK':
                raise Exception("Faltou quebrar a linha. Line: "+str(Parser.line))
            Parser.line += 1
            Parser.tokens.selectNext()

            staments = []

            while Parser.tokens.actual.type != 'FIM' and Parser.tokens.actual.type != 'SENÃO':
                staments.append(Parser.parseStatement())
                Parser.line +=1
                Parser.tokens.selectNext()
            
            children.append(Program("program_if", staments))

            if Parser.tokens.actual.type == "SENÃO":
                Parser.tokens.selectNext()

                if Parser.tokens.actual.type != 'COMMA':
                    raise Exception("Excpected a COMMA here. Line: {0}".format(str(Parser.line)))
                Parser.tokens.selectNext()

                if Parser.tokens.actual.type != 'FAÇA':
                    raise Exception("Excpected a FAÇA here. Line: {0}".format(str(Parser.line)))
                Parser.tokens.selectNext()

                if Parser.tokens.actual.type != 'TWO_DOTS':
                    raise Exception("Excpected a : here. Line: {0}".format(str(Parser.line)))
                Parser.tokens.selectNext()

                if Parser.tokens.actual.type != 'BREAK':
                    raise Exception("Faltou quebrar a linha. Line: "+str(Parser.line))
                Parser.line += 1
                Parser.tokens.selectNext()
                
                staments_else = []

                while Parser.tokens.actual.type != 'FIM':
                    staments_else.append(Parser.parseStatement())
                    Parser.line +=1
                    Parser.tokens.selectNext()
            
                children.append(Program("program_else", staments_else))
            
            if Parser.tokens.actual.type != 'FIM':
                raise Exception("Cade o FIM amigao? Line: "+str(Parser.line))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'DO':
                raise Exception("Cade o DO amigao? Line: "+str(Parser.line))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'CONDICIONAL':
               raise Exception("Excpected a CONDICIONAL here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            return IfNode("if", children)

        if Parser.tokens.actual.type == 'DIMENSIONE':
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'A':
               raise Exception("Excpected a A here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'VARIÁVEL':
               raise Exception("Excpected a VARIÁVEL here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()


            if Parser.tokens.actual.type != 'ID':
                raise Exception("Tava esperando um ID aqui. Line: "+str(Parser.line))
            id = Id(Parser.tokens.actual.value, [])
            Parser.tokens.selectNext()
            
            if Parser.tokens.actual.type != 'COMO':
                raise Exception("Cade o COMO amigao? Line: "+str(Parser.line))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'UM':
               raise Exception("Excpected a UM here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            return VarDec("vardec", [id, Parser.parseType()])

        if Parser.tokens.actual.type == 'CHAME':
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'A':
               raise Exception("Excpected a A here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'FUNÇÃO':
               raise Exception("Excpected a FUNÇÃO here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'ID':
                raise Exception("Cade o ID amigao? Line: {0}".format(str(Parser.line)))
            name = Parser.tokens.actual.value
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'COM':
               raise Exception("Excpected a COM here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'OS':
               raise Exception("Excpected a OS here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'ARGUMENTOS':
               raise Exception("Excpected a ARGUMENTOS here. Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            children = []

            if Parser.tokens.actual.type != 'OPEN_PAR':
                raise Exception("Cade o '(' amigao? Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            first = True
            while Parser.tokens.actual.type != 'CLOSE_PAR':
                if first == False:
                    if Parser.tokens.actual.type != 'COMMA':
                        raise Exception("Tava esperando uma vírgula aqui. Line: "+str(Parser.line))
                    Parser.tokens.selectNext()

                children.append(Parser.parseRelExpression())

                first = False

            if Parser.tokens.actual.type != 'CLOSE_PAR':
                raise Exception("Cade o ')' amigao? Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            return Call(name, children)
        
        return NoOp('', [])

    def parseType():
        if Parser.tokens.actual.type == "INTEIRO":
            Parser.tokens.selectNext()
            return Type('INTEGER', [])
        if Parser.tokens.actual.type == "BOOLEANO":
            Parser.tokens.selectNext()
            return Type('BOOLEAN', [])
        raise Exception(f"Type {Parser.tokens.actual.type} not reconhecated. Line: {Parser.line}")
        
            
    def parseRelExpression():
        exp = Parser.parseExpression()

        if Parser.tokens.actual.type == 'EQUAL':
            Parser.tokens.selectNext()
            return BinOp("=", [exp, Parser.parseExpression()])
        
        if Parser.tokens.actual.type == 'BIGGER':
            Parser.tokens.selectNext()
            return BinOp(">", [exp, Parser.parseExpression()])
        
        if Parser.tokens.actual.type == 'SMALLER':
            Parser.tokens.selectNext()
            return BinOp("<", [exp, Parser.parseExpression()])
        
        return exp

        

    def parseExpression():
        result = Parser.parseTerm()

        while(Parser.tokens.actual.type == 'PLUS' or Parser.tokens.actual.type == 'MINUS' or Parser.tokens.actual.type == 'OR'):
            if(Parser.tokens.actual.type == 'PLUS'):
                actual = Parser.tokens.selectNext()
                child1 = Parser.parseTerm()
                result = BinOp("+", [result, child1])
            elif(Parser.tokens.actual.type == 'MINUS'):
                actual = Parser.tokens.selectNext()
                child1 = Parser.parseTerm()
                result = BinOp("-", [result, child1])
            elif(Parser.tokens.actual.type == 'OU'):
                actual = Parser.tokens.selectNext()
                child1 = Parser.parseTerm()
                result = BinOp("or", [result, child1])
        
        return result

    def parseTerm():
        result = Parser.parseFactor()

        while(Parser.tokens.actual.type == 'DIV' or Parser.tokens.actual.type == 'MULT' or Parser.tokens.actual.type == 'AND'):
            if(Parser.tokens.actual.type == 'MULT'):
                actual = Parser.tokens.selectNext()
                child1 = Parser.parseFactor()
                result = BinOp("*", [result, child1])
                
            elif(Parser.tokens.actual.type == 'DIV'):
                actual = Parser.tokens.selectNext()
                child1 = Parser.parseFactor()
                result = BinOp("/", [result, child1])
            
            elif(Parser.tokens.actual.type == 'E'):
                actual = Parser.tokens.selectNext()
                child1 = Parser.parseFactor()
                result = BinOp("and", [result, child1])

        return result

    def parseFactor():
        actual = Parser.tokens.actual
        result = 0

        if actual.type == 'INT':
            result = IntVal(actual.value, [])
            actual = Parser.tokens.selectNext()
            return result

        if actual.type == 'ID':
            name = actual.value
            actual = Parser.tokens.selectNext()
            result = Id(name, [])
            return result


        if actual.type == 'RESULTADO':
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'DA':
                raise Exception("Cade o DA amigao? Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'FUNÇÃO':
                raise Exception("Cade o FUNÇÃO amigao? Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'ID':
                raise Exception("Cade o ID amigao? Line: {0}".format(str(Parser.line)))
            name = Parser.tokens.actual.value
            actual = Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'COM':
                raise Exception("Cade o COM amigao? Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'OS':
                raise Exception("Cade o OS amigao? Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'ARGUMENTOS':
                raise Exception("Cade o ARGUMENTOS amigao? Line: {0}".format(str(Parser.line)))
            actual = Parser.tokens.selectNext()

            if Parser.tokens.actual.type != 'OPEN_PAR':
                raise Exception("Cade o '(' amigao? Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            children = []

            first = True
            while Parser.tokens.actual.type != 'CLOSE_PAR':
                if first == False:
                    if Parser.tokens.actual.type != 'COMMA':
                        raise Exception("Tava esperando uma vírgula aqui. Line: "+str(Parser.line))
                    Parser.tokens.selectNext()

                children.append(Parser.parseRelExpression())

                first = False

            if Parser.tokens.actual.type != 'CLOSE_PAR':
                raise Exception("Cade o ')' amigao? Line: {0}".format(str(Parser.line)))
            Parser.tokens.selectNext()

            return Call(name, children)


        if actual.type == 'PLUS':
            actual = Parser.tokens.selectNext()
            child = Parser.parseFactor()
            return UnOp("+", [child])

        if actual.type == 'MINUS':
            actual = Parser.tokens.selectNext()
            child = Parser.parseFactor()
            return UnOp("-", [child])

        if actual.type == 'NOT':
            actual = Parser.tokens.selectNext()
            child = Parser.parseFactor()
            return UnOp("not", [child])
        

        if actual.type == 'VERDADEIRO' or actual.type == 'FALSO':
            res = Boolean(actual.value, [])
            actual = Parser.tokens.selectNext()
            return res
        
            

        if actual.type == 'OPEN_PAR':
            actual = Parser.tokens.selectNext()
            result = Parser.parseRelExpression()
            if Parser.tokens.actual.type == 'CLOSE_PAR':
                actual = Parser.tokens.selectNext()
                return result
            else:
                raise Exception("You did not fechate the parentesis! Line: {0}".format(str(Parser.line)))   

        
        raise Exception("Unexpected token '{0}'. Line: {1}".format(Parser.tokens.actual, str(Parser.line)))    


    def run(code):
        Parser.tokens = Tokenizer(PrePro.filter(code))
        Parser.line = 0
        Parser.tokens.selectNext()

        while Parser.tokens.actual.type == "BREAK":
            Parser.tokens.selectNext()

        res = Parser.parseProgram()

        while Parser.tokens.actual.type == "BREAK":
            Parser.tokens.selectNext()

        if Parser.tokens.actual.type == "EOF":
            return res
        else:
            raise Exception("Unexpected token '{0}'. Line: {1}".format(Parser.tokens.actual.type, str(Parser.line)))   