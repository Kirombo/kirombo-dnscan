import dns.resolver

print("[#] Kirombo - Enumeração de sub-domínios [#]\n")

dom = input("Dominio: ")
res = dns.resolver.Resolver()
wordlist = input("Wordlist: ")
print("\n")

arqv = open(wordlist)
subdoms = arqv.read().splitlines()

for subdom in subdoms:
    try:
        sub_dom = subdom + "." + dom
        rslt = res.resolve(sub_dom, "A")
        for ip in rslt:
            print(sub_dom, "->", ip, "\n")

    except:
        print("Erro!\n")
