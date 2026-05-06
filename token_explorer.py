import tiktoken

def get_size_label(count):
    if count < 20: return "short prompt"
    elif count < 100: return "Medium prompt"
    else:
        return "Long prompt"
    
def token_report(text, encoding):
    tokens = encoding.encode(text)
    print("\n" + "=" * 50)
    print("TOKEN REPORT")
    print("=" * 50)
    print("\nOriginal text:", text)
    print("Token count:", len(tokens))
    print("Prompt size:", get_size_label(len(tokens)))
    print("\nToken IDs:", tokens)
    print("\nToken pieces:")
    for i, tid in enumerate(tokens , 1):
        piece = encoding.decode([tid])
        print(f"{i}. ID: {tid} | Piece: {repr(piece)}")
    print("\nDecoded:", encoding.decode(tokens))
    print("=" * 50)

def main():
    encoding = tiktoken.get_encoding("o200k_base")
    print("Token Explorer CLI")
    print("Type text to see how it becomes tokens.")
    print("Type Q to quit.\n")

    while True:
        text = input("Enter Text: ")
        if text.lower() in ["q", "quit"]:
            print("Goodbye. ")
            break
        if not text.strip():
            print("Please type something.")
            continue
        token_report(text, encoding)
    
if __name__ == "__main__":
    main()