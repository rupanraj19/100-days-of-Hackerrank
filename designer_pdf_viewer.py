def designerPdfViewer(h, word):
    height = 0
    for letter in word:
        height = max(height,h[ord(letter) - ord('a')])

    return height * len(word)

h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
word = "abc"

print(designerPdfViewer(h, word))