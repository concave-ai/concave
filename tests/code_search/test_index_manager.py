from internal.codebase.manager import CodeSearchManager

manager = CodeSearchManager("../../../playground/examples/pytest/6a3ac51ee2350d5072fdd082040e7cfa22331fc0")

res = manager.full_text_search("_CaptureMethod")
res.print()
print()
print()

symbols = manager.symbol_search("CaptureMethod")
symbols.print()
print()
print()

vectors = manager.vector_search("where define the `CaptureMethod`")
vectors.print()
print()

