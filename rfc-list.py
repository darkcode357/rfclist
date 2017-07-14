from os import system
import sys, urllib.request
criador = "by darkcode 14/7/2017"
versao = "1"
def rfclist():
    try:
        numero_rfc = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Deve fornecer um numero de RFC para a busca...")
        sys.exit(2)
    site = 'http://www.ietf.org/rfc/rfc{}.txt'
    url = site.format(numero_rfc)
    rfc_raw = urllib.request.urlopen(url).read()
    rfc = rfc_raw.decode()
    save = str(input("quer salar o arquiv s/n :"))
    if save == 's':
        print("salvando.....")
        print("um momento.....")
        try:
            nome_arquivo = str(input("nome do protocolo > "))
            arquivo = open(nome_arquivo, 'r+')
            arquivo.writelines(rfc)
            system('nano' + ' ' + ' ' + '' +nome_arquivo)
            dsa = str(input("quer ler outro protocolo s/n :"))
            if dsa == 's':
                rfclist()
            else:
                print("saida....")
                print(criador)
        except FileNotFoundError:
            arquivo = open(nome_arquivo, 'w+')
            arquivo.writelines(rfc)
            system('nano' + ' ' + ' ' + '' + nome_arquivo)

    else:
        system("clear")
        print(rfc)
        print("saida")
        print(criador)
rfclist()