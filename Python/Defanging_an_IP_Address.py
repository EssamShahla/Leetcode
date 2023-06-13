class Solution(object):
    def defangIPaddr(self, address):
        result = ""
        for char in address:
            if char != ".":
                result+=char
            else:
                result+="[.]"
        return result