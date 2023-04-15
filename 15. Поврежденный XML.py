from string import ascii_lowercase

alphabet = '<>/' + ascii_lowercase

def test_xml(s):
    tags = []
    tag = ""
    stack = []
    if s[0] == '<':
        for let in s:
            if let == '>':
                if (len(tag) > 1 and tag[1] != '/') or (len(tag) > 2 and tag[1] == '/'):
                    tag += '>'
                    tags.append(tag)
                    tag = ''
                else:
                    return False
            else:
                tag += let
        if tag != '':
            return False
        for tag in tags:
            if tag[1] != '/':
                stack.append(tag)
            else:
                if len(stack) > 0 and stack[-1] == tag[0] + tag[2:]:
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        else:
            return True
    else:
        return False
def main(s):
    for let in alphabet:
        for i in range(len(s)):
            copy_s = s
            copy_s = s[:i] + let + s[i+1:]
            if test_xml(copy_s):
                return copy_s
s = input()
print(main(s))