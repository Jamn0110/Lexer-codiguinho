
import src.lexer

def codigo(text):
    content = text
    print(content)

    #Lexer 
    lex = src.lexer.Lexer(content)

    tokens = lex.tokenizar()
    let = "Lexema  :  Token "
    
    for token in tokens:
        let += token[0] + ' --> ' + token[1] + " "
    let += "\n"  
    return let   
