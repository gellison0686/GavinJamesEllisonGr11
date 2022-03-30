def product(fileName):

        h = open(fileName, "r")
        answer = 1

        for line in h:
            answer = answer * int(line)
        h.close()
        return answer
