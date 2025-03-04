import requests

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"The definition of '{word}':")
        for meaning in data[0]["meanings"]:
            for definition in meaning["definitions"]:
                print(f"- {definition['definition']}")
    else:
        print("No results found for this word.")

if __name__ == "__main__":
    word = input("Enter a word in English: ")
    get_definition(word)


