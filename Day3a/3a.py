def part1(data):
        numbers = re.findall(r'mul\((\d+,\d+)\)', data)
        sum = 0
        for i in numbers:
            x,y = i.split(",")
            sum += int(x)*int(y)
        return (sum)
    
def part2(data):
        data = "do()" + data + """don't()"""
        matches = re.findall(r"(?<=do\(\)).+?(?=don't\(\))", data)
        sum = 0
        for i in matches:
            sum += part1(i)
        return(sum)