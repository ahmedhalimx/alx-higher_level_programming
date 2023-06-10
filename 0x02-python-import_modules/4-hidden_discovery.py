#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    n = dir(hidden_4)
    for nn in n:
        if nn[:2] != "__":
            print(nn)
