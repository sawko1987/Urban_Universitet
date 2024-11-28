calls = 0
def count_calls():
    global calls
    calls +=1
def string_info (string):
    count_calls()
    for lines in string:
        return f"({len(string)},'{string.lower()}','{string.upper()}')"
def is_contains (string,list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower() in i.lower():
            return True
    return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', list_to_search=['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', list_to_search=['recycling', 'cyclic'])) # No matches
print(calls)






