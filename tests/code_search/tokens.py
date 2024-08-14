from internal.codebase.tokens.tokens import TokensIndexer

m = TokensIndexer("/Users/justwph/labs/hackathons/2024/playground/examples/pytest/4787fd64a4ca0dba5528b5651bddd254102fe9f3/index/scip/scip.sqlite")

tokens = list(m.tokens())
tokens.sort()
print(len(tokens))

with open("tokens.txt", "w") as f:
    for t in tokens:
        f.write(t + "\n")