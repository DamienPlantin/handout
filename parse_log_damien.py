import logging
import datetime
import sys


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
    return hours


def times(arg):
    """
    Cette fonction permet de convertir les horaires
    en minutes
    """
    logging.info("Start fonction times")
    hours = open_file(arg)
    for hour in hours:
        logging.info(hour)
        hour = hour.split("-")
        time1 = datetime.datetime.strptime(hour[0], "%H:%M")
        time2 = datetime.datetime.strptime(hour[1], "%H:%M")
        time = time2 - time1
        logging.info(time.seconds//60)
        minutes.append(time.seconds//60)
    logging.info("Finished fonction times")
    return minutes


def total_times(arg):
    """
    Cette fonction calcul le temps total du planning
    """
    logging.info("Start fonction total_times")
    minutes = times(arg)
    logging.info(f"Liste des horires en minutes : {minutes}")
    res = 0
    for minute in minutes:
        res += minute
    logging.info(f"Temps total : {res}")
    logging.info("Finished fonction total_times")
    return res


def add_dict(arg):
    """
    Cette fonction permet de mettre en place un dictionnaire
    avec comme clé la matière et comme valeur le temps en minutes.

    """
    logging.info("Start fonction add_dict")
    total_times(arg)
    result = list(zip(matters, minutes))
    result.sort()
    logging.info(f"Liste trier : {result}")
    for matter, minute in result:
        if matter not in dict:
            dict[matter] = minute
        elif matter in dict:
            dict[matter] += minute
    logging.info(f"Dictionnaire des matieres : {dict}")
    logging.info("Finished fonction add_dict")
    return dict


def expected_output(arg):
    logging.info("Start fonction expected_output")
    total = total_times(arg)
    output = add_dict(arg)
    for a in output.keys():
        a = a
        b = output[a]//2
        c = int((b/total)*100)
        b = str(b) + " minutes"
        c = str(c) + "%"
        c = " "*(6-len(c))+str(c)
        a = a+(43-(len(a)+len(b)+len(c)))*" "
        finished = a + b + c
        print(finished)
        logging.info(f"Sortie : {finished}")
    logging.info("Finished fonction expected_output")
    return output


def main():
    sys.stdout = open('expected_output_damien.txt', 'w')
    expected_output(arg)
    sys.stdout.close()


if __name__ == '__main__':
    hours, matters, minutes, dict = [], [], [], {}
    logging.basicConfig(filename='log_damien.log', level=logging.DEBUG)
    arg = sys.argv[1]
    sys.exit(main())
