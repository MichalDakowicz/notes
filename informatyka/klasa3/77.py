def vigenere(text, key, encrypt=True):
    result = ""
    key_len = len(key)
    key_index = 0
    repeats = 1

    for char in text:
        if 'A' <= char <= 'Z':
            shift = ord(key[key_index % key_len]) - ord('A')
            code = ord(char) + shift if encrypt else ord(char) - shift
            if code > ord('Z'):
                code -= 26
            if code < ord('A'):
                code += 26
            result += chr(code)
            key_index += 1
            if key_index % key_len == 0:
                repeats += 1
        else:
            result += char

    return result, repeats


def zadanie_77_1():
    with open("informatyka/dane/77/dokad.txt", "r", encoding="utf-8") as file:
        text = file.readline().strip()

    key = "LUBIMYCZYTAC"
    encrypted, repeats = vigenere(text, key, True)

    print("77.1")
    print("Liczba powtórzeń klucza:", repeats)
    print("Tekst zaszyfrowany:", encrypted)

    return f"77.1\na) {repeats}\nb) {encrypted}\n"


def zadanie_77_2():
    with open("informatyka/dane/77/szyfr.txt", "r", encoding="utf-8") as file:
        encrypted = file.readline().strip()
        key = file.readline().strip()

    decrypted, _ = vigenere(encrypted, key, False)

    print("77.2")
    print("Tekst odszyfrowany:", decrypted)

    return f"77.2\n{decrypted}\n"


def zadanie_77_3():
    with open("informatyka/dane/77/szyfr.txt", "r", encoding="utf-8") as file:
        encrypted = file.readline().strip()
        key = file.readline().strip()

    counts = [0] * 26
    for char in encrypted:
        if 'A' <= char <= 'Z':
            counts[ord(char) - ord('A')] += 1

    print("77.3 a) Liczby wystąpień liter:")
    result = "77.3\na)\n"
    for i, count in enumerate(counts):
        letter = chr(i + ord('A'))
        print(f"{letter}: {count}")
        result += f"{letter}: {count}\n"

    total = sum(counts)
    coincidence = sum(c * (c - 1) for c in counts)

    if total > 1:
        ic = coincidence / (total * (total - 1))
        est_key_len = 0.0285 / (ic - 0.0385)
        est_key_len = round(est_key_len, 2)
    else:
        est_key_len = 0.0

    print(f"\nSzacunkowa długość klucza: {est_key_len}")
    print(f"Dokładna długość klucza: {len(key)}")

    result += f"\nSzacunkowa długość klucza: {est_key_len}\nDokładna długość klucza: {len(key)}\n"
    return result


if __name__ == "__main__":
    output = (
        zadanie_77_1() + "\n" +
        zadanie_77_2() + "\n" +
        zadanie_77_3()
    )
