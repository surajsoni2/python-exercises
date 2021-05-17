def split_and_join(line):
    newstr=line.split()
    newstr="-".join(newstr)
    return newstr

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)