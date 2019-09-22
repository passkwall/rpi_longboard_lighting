import csv
import math
import time

with open("log.csv", "r") as log:
    with open("out.csv", "w", newline='') as output:
        logs = csv.reader(log)
        outp = csv.writer(output)

        long_poll = []
        an_array = []


        for row in logs:
            x = row[0]
            x = float(x.strip("'"))
            if len(an_array) > 10:
                an_array.pop(0)
                an_array.append(x)
            else:
                an_array.append(x)

            if len(long_poll) > 100:
                long_poll.pop(0)
                long_poll.append(x)
            else:
                long_poll.append(x)

            short_average = sum(an_array)/(len(an_array))
            long_average = sum(long_poll)/(len(long_poll))
            outp.writerow([x, short_average, long_average, row[3]])
            
            if len(an_array) > 10:
                if (long_average - short_average) > 1 and x < -10:
                    thing = {
                        "short poll": short_average,
                        "long poll": long_average,
                        "l over s": round(long_average / short_average, 2),
                        "s over l": round(short_average / long_average, 2),
                        "difference": round(long_average - short_average, 2),
                        "x": x
                    }
                    # print(short_average)
                    # print(long_average)
                    # print(long_average / short_average)
                    print(thing)
                    # time.sleep(1)
