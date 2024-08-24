from concave.internal.codebase.manager import CodeSearchManager


def search(uuid, key):
    manager = CodeSearchManager(f"../../../playground/examples/pytest/{uuid}")

    res = manager.full_text_search(key)
    res.print()
    print()
    print()

    symbols = manager.symbol_search(key)
    symbols.print()
    print()
    print()


search("4787fd64a4ca0dba5528b5651bddd254102fe9f3", "_format_repr_exception")
