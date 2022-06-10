import ply.lex as lex
import ply.yacc as yacc
import image as im

reserved = {
    'canva':'CNV',
    'square':'SQR',
    'circle':'CR',
    'triangle':'TR',
    }

tokens = ['ID', 'ASIGN',
          'DRAWTO', 'ERASETO'] + list(reserved.values())

t_ignore  = ' \t'

t_CNV = r'canva'

t_SQR = r'square'
t_CR = r'circle'
t_TR = r'triangle'

t_ASIGN = r'<<'
t_DRAWTO = r'<\+'
t_ERASETO = r'<-'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_error(t):
    print("Syntax Error")
    t.lexer.skip(1)

precedence=(('right', 'DRAWTO'),
            ('right', 'ERASETO'),
            ('right', 'ASIGN'),
            ('right', 'ID'),
            ('right', 'CNV'),
            )

save_canvas = {}
save_figures = {}

def p_def_canva(t):
    'end : ID ASIGN s '
    save_canvas[t[1]] = {'im':t[3]}
        
def p_show(t):
    'end : s'
    try:
        im.show_canvas(t[1])
    except LookupError:
            print("Canvas '%s' no existe!" % t[3])

def p_expr_canva(t):
    's : CNV'
    t[0] = im.new_canvas(2000, 2000, 215, 215, 215)


def p_expr_id(t):
    's : ID'
    try:
        t[0] = save_canvas[t[1]]['im']
    except LookupError:
            print("Canvas '%s' no existe!" % t[3])

            
def p_draw_square(t):
    's : s DRAWTO SQR'
    try:
        t[0] = im.draw_rectangle(t[1],400,400,1600,1600, 46,139,87)
    except LookupError:
            print("Canvas '%s' no existe!" % t[1])
            
def p_draw_circle(t):
    's : s DRAWTO CR'
    try:
        t[0] = im.draw_circle(t[1],200,200,1800,1800, 81,0,93)
    except LookupError:
            print("Canvas '%s' no existe!" % t[1])
            
def p_draw_triangle(t):
    's : s DRAWTO TR'
    try:
        t[0] = im.draw_polygon(t[1],1000, 1500, 500, 500, 1500, 500, 238,232,170)
    except LookupError:
            print("Canvas '%s' no existe!" % t[1])
            
def p_erase_square(t):
    's : s ERASETO SQR'
    try:
        t[0] = im.draw_rectangle(t[1],400,400,1600,1600, 215,215,215)
    except LookupError:
            print("Canvas '%s' no existe!" % t[1])
            
def p_erase_circle(t):
    's : s ERASETO CR'
    try:
        t[0] = im.draw_circle(t[1],200,200,1800,1800, 215,215,215)
    except LookupError:
            print("Canvas '%s' no existe!" % t[1])

def p_erase_triangle(t):
    's : s ERASETO TR'
    try:
        t[0] = im.draw_polygon(t[1],1000, 1500, 500, 500, 1500, 500, 215,215,215)
    except LookupError:
            print("Canvas '%s' no existe!" % t[1])
            
def p_error(t):
    print("Error!")
            

    
lexer=lex.lex()
parser=yacc.yacc()
while True:
    try:
        data = input()
    except EOFError:
        break
    parser.parse(data)







