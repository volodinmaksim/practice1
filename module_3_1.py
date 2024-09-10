calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    mas = (len(string), string.upper(), string.lower())
    return mas

def is_contains(string, listing):
    count_calls()
    for string2 in listing:
        if string.lower() == string2.lower():
            return True
    else:
        return False


print (is_contains('Sid', ['siD', 34]))
print(string_info('dfDAS'))
string_info("dfgd")
string_info("hbsased")
string_info("fsdsd")

print(calls)
