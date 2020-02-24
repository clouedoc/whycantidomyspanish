# whycantidomyspanish


La prof d'espagnol nous a donné une grille avec des mots à retrouver. Les mots peuvent être disposés horizontalement, verticalement et diagonalement; à l'endroit, et à l'envers.

# Techniquement parlant

Ce projet a entièrement été réalisé sur une installation fraiche d'ubuntu avec `vim`, `screen` et `python3` sur un droplet@DigitalOcean:min(price).

## Installation 

Installez la librairie `pyenchant` ainsi que son module Python:

```bash
apt install pyenchant
pip3 install pyenchant
```

Installez le dictionnaire espagnol (ne vient pas par défaut avec pyenchant)
```bash
apt install myspell-es
```

Vous pourrez ainsi exécuter le programme: 

```bash
python3 main.py
```

Les résultats de l'expérience sont disponibles dans `paridad_words.txt` et `turismo_words.txt`.

# Les tableaux

### Paridad

![paridad](https://raw.githubusercontent.com/sheldoncoupeheure/whycantidomyspanish/master/paridad_table.jpg)

### Turismo

![turismo](https://raw.githubusercontent.com/sheldoncoupeheure/whycantidomyspanish/master/turismo_table.jpg)

nique la rotation
