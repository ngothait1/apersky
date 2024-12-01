import time

def countLogsByKeyword():
    try:
        keywords = ["INFO", "WARN", "ERROR"]
        counts = {key: 0 for key in keywords}
        with open("/var/log/syslog", "r") as log_file:
            for line in log_file:
                words = line.split()
                for keyword in keywords:
                    if keyword in words:
                        counts[keyword] += 1
        return counts
    except Exception as e:
        print("An error occurred while reading the log file: " + str(e))
        return {key: 0 for key in ["INFO", "WARN", "ERROR"]}

def getOutput():
    counts = countLogsByKeyword()
    timestamp = int(time.time())
    output = str(timestamp) + "," + str(counts["INFO"]) + "," + str(counts["WARN"]) + "," + str(counts["ERROR"])
    return output

if __name__ == "__main__":
    print(getOutput())
