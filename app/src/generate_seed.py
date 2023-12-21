from mnemonic import Mnemonic

def generate_seed(seed_length):
    try:
        if seed_length == "12" or seed_length == "24":
            entropy_bits = 128 if seed_length == "12" else 256
            mnemonic = Mnemonic("english")
            seed_words = mnemonic.generate(entropy_bits)
            return seed_words
        else:
            return "Invalid choice. Please choose 12 or 24."
    except Exception as e:
        return "An error occurred: " + str(e)