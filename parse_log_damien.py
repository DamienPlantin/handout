import logging
import datetime
import sys

hours, matters, minutes, dict = [], [], [], {}


def open_file(arg):
    """
    Cette fonction permet de lire le fichier, de récupérer les horaires
    et les matieres, et de les séparer dans des listes différentes
    """
    logging.info("Start fonction open_file")
    logging.info(f"Ouverture fichier : {arg}")
    with open(arg) as f:
        lines = f.read().strip()
        for line in lines.split("\n"):
            if line != "":
                hours.append(line[0:11])
                matters.append(line[12:])
    logging.info(f"Liste des matieres : {matters}")
    logging.info(f"Liste des heures : {hours}")
    logging.info("Finished fonction open_file")
    return matters, hours


def times(matters, hours):
    """
    Cette fonction permet de convertir les horaires
    en minutes
    """
    logging.info("Start fonction times")
    for hour in hours:
        logging.info(hour)
        hour = hour.split("-")
        time1 = datetime.datetime.strptime(hour[0], "%H:%M")
        time2 = datetime.datetime.strptime(hour[1], "%H:%M")
        time = time2 - time1
        logging.info(time.seconds//60)
        minutes.append(time.seconds//60)
    result = list(zip(matters, minutes))
    logging.info("Finished fonction times")
    return result


def add_dict(result):
    """
    Cette fonction permet de mettre en place un dictionnaire
    avec comme clé la matière et comme valeur le temps en minutes.

    """
    logging.info("Start fonction add_dict")
    res = 0
    result.sort()
    logging.info(f"Liste trier : {result}")
    for matter, minute in result:
        res += minute
        if matter not in dict:
            dict[matter] = minute
        elif matter in dict:
            dict[matter] += minute
    logging.info(f"Temps total : {res}")
    logging.info(f"Dictionnaire des matieres : {dict}")
    logging.info("Finished fonction add_dict")
    return res, dict


def expected_output(total, output):
    logging.info("Start fonction expected_output")
    for a in output.keys():
        a = a
        b = output[a]
        c = int((b/total)*100)
        b = str(b) + " minutes"
        c = str(c) + "%"
        c = " "*(6-len(c))+str(c)
        a = a + (43-(len(a)+len(b) + len(c)))*" "
        finished = a + b + c
        print(finished)
        logging.info(f"Sortie : {finished}")
    logging.info("Finished fonction expected_output")
    return finished


def main():
    matters, hours = open_file(arg)
    result = times(matters, hours)
    total, output = add_dict(result)
    sys.stdout = open('expected_output_damien.txt', 'w')
    expected_output(total, output)
    sys.stdout.close()


if __name__ == '__main__':
    logging.basicConfig(filename='log_damien.log', level=logging.DEBUG)
    arg = sys.argv[1]
    sys.exit(main())
