# 🔍 Network Scanner

Scanner de rede em Python construído em um ambiente de laboratório isolado no VirtualBox como projeto de portfólio de cibersegurança júnior.

## ✨ Funcionalidades
- Descoberta de hosts via ping sweep
- Escaneamento de portas TCP com detecção de serviços
- Banner grabbing (versões dos serviços)
- Geração automática de relatórios em JSON e TXT

## 🖥️ Ambiente de Laboratório
| Máquina | Sistema | IP |
|---|---|---|
| Atacante | Kali Linux 2025.2 | 192.168.56.105 |
| Alvo | Metasploitable 2 | 192.168.56.106 |
| Rede | Host-Only Adapter (isolada) | 192.168.56.0/24 |

## 🚀 Como usar
```bash
sudo python3 scanner.py -t 192.168.56.106
```

## ⚠️ Aviso
Apenas para uso educacional em ambientes de laboratório isolados. Nunca utilize em sistemas sem autorização.
