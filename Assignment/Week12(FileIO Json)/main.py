import os

if os.path.isfile("accounts.json"):
    os.remove("accounts.json")

if __name__ == "__main__":
    import doctest

    doctest.testfile("docs/bankaccount.md")
