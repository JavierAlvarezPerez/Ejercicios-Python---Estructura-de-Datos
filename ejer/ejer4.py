logs = [
    ("192.168.1.1", "/home", "Chrome"),
    ("192.168.1.2", "/login", "Firefox"),
    ("192.168.1.1", "/dashboard", "Chrome"),
    ("192.168.1.3", "/home", "Edge"),
    ("192.168.1.2", "/home", "Firefox")
]

#diccionario: IP - conjunto de URLs
ip_urls = {}

#diccionario: URL - contador de visitas
visitas_url = {}

#diccionario: navegador - contador
uso_navegador = {}

#conjunto de IPs únicas
ips_unicas = set()

for ip, url, navegador in logs:

#IP - URLs
    if ip not in ip_urls:
        ip_urls[ip] = set()
    ip_urls[ip].add(url)

#contar visitas por URL
    visitas_url[url] = visitas_url.get(url, 0) + 1

#contar navegadores
    uso_navegador[navegador] = uso_navegador.get(navegador, 0) + 1

#ips únicas
    ips_unicas.add(ip)

#navegador más usado
navegador_mas_usado = max(uso_navegador, key=uso_navegador.get)

#lista ordenada de ips
ips_ordenadas = sorted(ips_unicas)

print("IP -> URLs visitadas:")
print(ip_urls)

print("\nVisitas por URL:")
print(visitas_url)

print("\nNavegador más utilizado:")
print(navegador_mas_usado)

print("\nIPs únicas ordenadas:")
print(ips_ordenadas)
