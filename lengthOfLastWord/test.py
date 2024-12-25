# # input = "Hello World"
# input = "   fly me   to   the moon  "
# # input = "luffy is still joyboy"
# hasil = input.split()
# last_hasil = hasil[-1]
# fix = len(last_hasil)
# print(fix)

def lengthOfLastWord(masukan):
    hasil1 = masukan.split()
    hasil2 = hasil1[-1]
    hasil3 = len(hasil2)

    print(hasil3)

    return lengthOfLastWord

# lengthOfLastWord("   fly me   to   the moon  ")
# lengthOfLastWord("luffy is still joyboy")
lengthOfLastWord("Hello World")