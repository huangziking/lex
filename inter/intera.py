# -*-coding:UTF-8-*-
#this is a inte token
import sys
sys.path.append("d:\\untitled2\\untitled\\inter\\intera.py")
INTEGER,PLUS,EOF='INTEGER','PLUS','EOF'
class Token(object):
    def __init__(self,type,value):
        self.type=type   #token typey :INTEGER PLUS EOF
        self.value=value
    def __str__(self):
        """
        String representation of the class instance.

        Examples:
            Token(INTEGER.3)
            Token(PLUS '+')
        """
        return 'Token({type},{value})'.format(
            type=self.type,
            value=repr(self.value)
        )
    def __repr__(self):
        return self.__str__()
class Interpreter(object):
    def __init__(self,text):
        self.text=text
        self.pos=0
        self.current_token=None

    def error(self):
        raise  Exception('Error parsing input')
    def get_next_token(self):
        """
        Lexical analyzer (also know as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens.One token at a time

        """
        text=self.text
        #is self.pos index past the end of the self.text?
        #if so then return EOF token beacuse there is no more apart into tokens. One token at a time .
        #test=len(text)-1
        if self.pos > len(text) - 1:
            #print(test)
            print(self.pos)
            return Token(EOF,None)
        #get a character at the position self.pos and decide
        #what token to create based on the single character
        current_char=text[self.pos]
        #if the character is a digit then convert it to
        #integer create an INTEGER token ,increment self.pos
        #index to point to the next character after the digit,
        #and return the INTEGET token
        if current_char.isdigit():
            token=Token(INTEGER,int(current_char))
            self.pos+=1
            return token
        if current_char=='+':
            token=Token(PLUS,current_char)
            self.pos +=1
            return token#返回记号
        self.error()
    def eat(self,token_type):
        #compare the current token type with the passed token
        #type and if they match then "eat" the current token
        #and assign the next token to the self.current_token
        #otherwise raise an exception
        if self.current_token.type==token_type:
            self.current_token=self.get_next_token()
        else:
            self.error()
    def expr(self):
        """exper -> INTEGER PLUS INTEGER"""
        #set current token to the first token taken from the input
        self.current_token=self.get_next_token()#返回记号
        #we expect the current token to be a single-digit integer
        left=self.current_token
        self.eat(INTEGER)
        #we expect the current token to be a '+'token
        op=self.current_token
        self.eat(PLUS)

        #we expect the current token to be a single-digit integer
        right=self.current_token
        self.eat(INTEGER)
        #after the above call the self.current_token is set to
        #EOF token
        #at this point INTERGER PLUS INTEGER sequence of tokens
        #has been successfully found and the method
        #return the result of adding two integers
        #effectively interpreting client input
        result=left.value+right.value
        return result
def main():
    while True:
            #To run under python3 reloace 'raw_input'
            #with 'input'
        try:
            text=input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter=Interpreter(text)#初始化
        result=interpreter.expr()#判断记号流
        print(result)
if __name__ == '__main__':
    main()

