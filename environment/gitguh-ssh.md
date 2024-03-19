<!-- markdownlint-disable MD007 -->
<!-- cSpell:ignore  bieitostudies -->

# SSH Keys and Github

```bash
cd ~/.ssh
## generar clave publica y clave privada
ssh-keygen -t rsa -C "$(whoami)-laptop"
ls
# [out] authorized_keys  authorized_keys  bieitostudies-laptop  bieitostudies-laptop.pub  known_hosts
# bieitostudies-laptop clave privada // bieitostudies-laptop.pub  clave publica
# en github vamos a configuración/SSH and GPG keys
# new SSH key
# añadimos nuestra clave publica(.pub)
ssh -T git@github.com
# [out]
# Si informa, Hi [your Github username]! You've successfully authenticated, but GitHub does not provide shell access.entonces la conexión fue exitosa y usted sabe que ha configurado sus claves correctamente.
```
