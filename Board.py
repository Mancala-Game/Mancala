import copy

#converter lista para string
#facilita para representar o jogo
def convert_str(list):
    list_aux=[]
    for i in list:
        list_aux += (str)(i)
    return list_aux

class Board:

    def __init__(self):
        self.list=[4,4,4,4,4,4,4,4,4,4,4,4]
        self.mancalas=[0,0]

    def __str__(self):
        list_aux=convert_str(self.list)
        manc = convert_str(self.mancalas)
        text = """┌──┬──┬──┬──┬──┬──┬──┬──┐
│  │{}│{}│{}│{}│{}│{}│  │  
├{}┼──┼──┼──┼──┼──┼──┼{}┤
│  │{}│{}│{}│{}│{}│{}│  │  
└──┴──┴──┴──┴──┴──┴──┴──┘""" \
            .format(list_aux[0].rjust(2, '0'), list_aux[1].rjust(2, '0'), list_aux[2].rjust(2, '0'),list_aux[3].rjust(2, '0'),list_aux[4].rjust(2, '0'), list_aux[5].rjust(2, '0'), 
                    manc[0].rjust(2,'0'),manc[1].rjust(2,'0'),
                    list_aux[6].rjust(2, '0'),list_aux[7].rjust(2, '0'),list_aux[8].rjust(2, '0'), list_aux[9].rjust(2, '0'), list_aux[10].rjust(2, '0'),list_aux[11].rjust(2, '0'))
        return text

jogo=Board()
print(jogo)