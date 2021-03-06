INTEGER,PLUS,MINUS,EOF,Multiply,excep='INTEGER','PLUS','MINUS','EOF','Multiply','excep'
class Token(object):
    def __init__(self,type,value):
        #token type:INTEGER,PLUS,MINUS,or EOF
        self.type=type
        self.value=value
    def __str__(self):
        return 'Token({type},{value})'.format(type=self.type,value=repr(self.value))
    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self,text):
        self.text=text
        self.pos=0
        self.current_token=None
        self.current_char=self.text[self.pos]
    def error(self):
        raise Exception('Error parsing input')
    def advance(self):
        self.pos+=1
        if self.pos>len(self.text)-1:
            self.current_char=None
        else:
            self.current_char=self.text[self.pos]
    def skip_witespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    def integer(self):
        result=''
        while self.current_char is not None and self.current_char.isdigit():
            result+=self.current_char
            self.advance()
        return int(result)
    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_witespace()
                continue
            if self.current_char.isdigit():
                return Token(INTEGER,self.integer())
            if self.current_char=='+':
                self.advance()
                return Token(PLUS,'+')
            if self.current_char=='-':
                self.advance()
                return Token(MINUS,'-')
            if self.current_char=='*':
                self.advance()
                return Token(Multiply,'*')
            if self.current_char=='/':
                self.advance()
                return Token(excep,'/')
            self.error()
        return Token(EOF,None)
    def eat(self,token_tpye):
        if self.current_token.type==token_tpye:
            self.current_token=self.get_next_token()
        else:
            self.error()
    def expr(self):
        self.current_token=self.get_next_token()
        left=self.current_token
        self.eat(INTEGER)
        op=self.current_token
        if op.type==PLUS:
            self.eat(PLUS)
        if op.type==MINUS:
            self.eat(MINUS)
        if op.type==Multiply:
            self.eat(Multiply)
        if op.type==excep:
            self.eat(excep)
        right=self.current_token
        self.eat(INTEGER)
        if op.type==PLUS:
            result=left.value+right.value
        if op.type==MINUS:
            result=left.value-right.value
        if op.type==Multiply:
            result=left.value*right.value
        if op.type==excep:
            result=left.value/right.value
        return result
def main():
        while True:
            try:
                text=input('calc>')
            except EOFError:
                break
            if not text:
                continue
            interpreter=Interpreter(text)
            result=interpreter.expr()
            print(result)
if __name__=='__main__':
    main()