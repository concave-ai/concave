from concave.internal.codebase.search.full_text.full_text import FullTextSearcher

searcher = FullTextSearcher("/Users/justwph/labs/hackathons/2024/playground/examples/pytest/4787fd64a4ca0dba5528b5651bddd254102fe9f3/src")
result = searcher.search(["EncodedFile"])
searcher.print(result)