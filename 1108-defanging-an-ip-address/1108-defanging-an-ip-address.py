class Solution:
    def defangIPaddr(self, address: str) -> str:
        stri = [ ]
        for i in range(len(address)):
            if address[i] == '.':
                stri.append("[.]")
            else:
                stri.append(address[i])
        return ''.join(stri)
