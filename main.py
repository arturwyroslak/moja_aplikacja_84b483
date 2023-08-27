import openai

# Ustawienie klucza API
openai.api_key = "TUTAJ_WPISZ_TWÓJ_KLUCZ_API"

# Funkcja do interakcji z chatbotem
def chat_with_bot(message):
    response = openai.Completion.create(
        engine="davinci",
        prompt=message,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        response_format="json"
    )

    # Pobranie odpowiedzi od chatbota
    reply = response['choices'][0]['text'].strip()
    return reply

# Główna pętla aplikacji
if __name__ == "__main__":
    print("Witaj! Jestem chatbotem. Możesz ze mną porozmawiać, zadając pytania.")

    while True:
        user_input = input("Ty: ")
        
        if user_input.lower() == "exit":
            break

        # Zadanie pytania chatbotowi
        bot_reply = chat_with_bot(user_input)
        print("Chatbot: " + bot_reply)

W pliku z kluczem API (klucz_api.txt) należy umieścić swój własny klucz API dostępny po rejestracji na stronie OpenAI.