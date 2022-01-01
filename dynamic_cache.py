

def inserir():
    file = open('backup.txt', 'wt')
    file.write('eu sou miguel')
    file.close()

        
def exibir():
    content = open('backup.txt', 'rt')
    for i in content:
        print(i, end='')
    content.close()
        

    
        

