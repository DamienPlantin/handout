def parse_line(line):
    """
    Reads a string from the log, returns a tuple with type of activity and
    duration

    Chose the following convention : it the two times are equal even has 0
    duration
    Otherwise if the first time is bigger than the second,
    it's an even that happens overnight
    :param line: line from the logfile : format "HH:MM-HH-MM <activity>"
    :returns: tuple (x,y) with x int (duration in minutes) and y str,
    None if incorrect input string
    :rtype: tuple
    """
    if line == "":
        return None
    try:
        p = line.split()
        if len(p) < 2:
            return None
        activity_name = " ".join(p[1:])
        t = p[0].split("-")

        def _tm(ts):
            # Parses a HH:MM str into an int for total minutes
            a, b = ts.split(":")
            a = int(a)*60
            b = int(b)
            return a+b
        t1, t2 = _tm(t[0]), _tm(t[1])
        # check if times are in decreasing or increasing order to
        # check whether even is overnight
        return (activity_name, t2-t1 if (t2 >= t1) else 24*60+t2-t1)
    except ValueError:
        return None


def parse_file(infile):
    """
    Parses a log file then returns the info in two dictionnaries
    :param infile: file like object
    :returns: a pair of dictionaries : first is number of occurence per title,
    other is total duration
    """
    # counts references per service
    cpt = {}
    # total time
    dur = {}
    for line in infile:
        c = parse_line(line)
        if c:
            activity, duration = c
            if activity not in cpt:
                cpt[activity] = 0
            if activity not in dur:
                dur[activity] = 0
            cpt[activity] += 1
            dur[activity] += duration
    return cpt, dur


def print_result(dur):
    """
    Prints the result from parsing the log file to the expected format.
    :param dur: dictionary with total duration per type
    """
    total_min = sum(dur.values())
    for h in sorted(dur.keys()):
        a = h
        b = dur[h]
        # only want the truncated percentage
        c = int((b/total_min)*100)

        # transform to strings and compute necessary lengths
        b = str(b)+" minutes"
        c = str(c)+"%"
        c = " "*(6-len(c))+str(c)
        a = a+(43-(len(a)+len(b)+len(c)))*" "

        print(a+b+c)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("path")

    args = parser.parse_args()
    with open(args.path, "r") as f:
        c, d = parse_file(f)
        print_result(d)


if __name__ == "__main__":
    import sys
    sys.exit(main())
