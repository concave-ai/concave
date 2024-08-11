from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProtocolVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnspecifiedProtocolVersion: _ClassVar[ProtocolVersion]

class TextEncoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnspecifiedTextEncoding: _ClassVar[TextEncoding]
    UTF8: _ClassVar[TextEncoding]
    UTF16: _ClassVar[TextEncoding]

class PositionEncoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnspecifiedPositionEncoding: _ClassVar[PositionEncoding]
    UTF8CodeUnitOffsetFromLineStart: _ClassVar[PositionEncoding]
    UTF16CodeUnitOffsetFromLineStart: _ClassVar[PositionEncoding]
    UTF32CodeUnitOffsetFromLineStart: _ClassVar[PositionEncoding]

class SymbolRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnspecifiedSymbolRole: _ClassVar[SymbolRole]
    Definition: _ClassVar[SymbolRole]
    Import: _ClassVar[SymbolRole]
    WriteAccess: _ClassVar[SymbolRole]
    ReadAccess: _ClassVar[SymbolRole]
    Generated: _ClassVar[SymbolRole]
    Test: _ClassVar[SymbolRole]
    ForwardDefinition: _ClassVar[SymbolRole]

class SyntaxKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnspecifiedSyntaxKind: _ClassVar[SyntaxKind]
    Comment: _ClassVar[SyntaxKind]
    PunctuationDelimiter: _ClassVar[SyntaxKind]
    PunctuationBracket: _ClassVar[SyntaxKind]
    Keyword: _ClassVar[SyntaxKind]
    IdentifierKeyword: _ClassVar[SyntaxKind]
    IdentifierOperator: _ClassVar[SyntaxKind]
    Identifier: _ClassVar[SyntaxKind]
    IdentifierBuiltin: _ClassVar[SyntaxKind]
    IdentifierNull: _ClassVar[SyntaxKind]
    IdentifierConstant: _ClassVar[SyntaxKind]
    IdentifierMutableGlobal: _ClassVar[SyntaxKind]
    IdentifierParameter: _ClassVar[SyntaxKind]
    IdentifierLocal: _ClassVar[SyntaxKind]
    IdentifierShadowed: _ClassVar[SyntaxKind]
    IdentifierNamespace: _ClassVar[SyntaxKind]
    IdentifierModule: _ClassVar[SyntaxKind]
    IdentifierFunction: _ClassVar[SyntaxKind]
    IdentifierFunctionDefinition: _ClassVar[SyntaxKind]
    IdentifierMacro: _ClassVar[SyntaxKind]
    IdentifierMacroDefinition: _ClassVar[SyntaxKind]
    IdentifierType: _ClassVar[SyntaxKind]
    IdentifierBuiltinType: _ClassVar[SyntaxKind]
    IdentifierAttribute: _ClassVar[SyntaxKind]
    RegexEscape: _ClassVar[SyntaxKind]
    RegexRepeated: _ClassVar[SyntaxKind]
    RegexWildcard: _ClassVar[SyntaxKind]
    RegexDelimiter: _ClassVar[SyntaxKind]
    RegexJoin: _ClassVar[SyntaxKind]
    StringLiteral: _ClassVar[SyntaxKind]
    StringLiteralEscape: _ClassVar[SyntaxKind]
    StringLiteralSpecial: _ClassVar[SyntaxKind]
    StringLiteralKey: _ClassVar[SyntaxKind]
    CharacterLiteral: _ClassVar[SyntaxKind]
    NumericLiteral: _ClassVar[SyntaxKind]
    BooleanLiteral: _ClassVar[SyntaxKind]
    Tag: _ClassVar[SyntaxKind]
    TagAttribute: _ClassVar[SyntaxKind]
    TagDelimiter: _ClassVar[SyntaxKind]

class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnspecifiedSeverity: _ClassVar[Severity]
    Error: _ClassVar[Severity]
    Warning: _ClassVar[Severity]
    Information: _ClassVar[Severity]
    Hint: _ClassVar[Severity]

class DiagnosticTag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnspecifiedDiagnosticTag: _ClassVar[DiagnosticTag]
    Unnecessary: _ClassVar[DiagnosticTag]
    Deprecated: _ClassVar[DiagnosticTag]

class Language(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnspecifiedLanguage: _ClassVar[Language]
    ABAP: _ClassVar[Language]
    Apex: _ClassVar[Language]
    APL: _ClassVar[Language]
    Ada: _ClassVar[Language]
    Agda: _ClassVar[Language]
    AsciiDoc: _ClassVar[Language]
    Assembly: _ClassVar[Language]
    Awk: _ClassVar[Language]
    Bat: _ClassVar[Language]
    BibTeX: _ClassVar[Language]
    C: _ClassVar[Language]
    COBOL: _ClassVar[Language]
    CPP: _ClassVar[Language]
    CSS: _ClassVar[Language]
    CSharp: _ClassVar[Language]
    Clojure: _ClassVar[Language]
    Coffeescript: _ClassVar[Language]
    CommonLisp: _ClassVar[Language]
    Coq: _ClassVar[Language]
    CUDA: _ClassVar[Language]
    Dart: _ClassVar[Language]
    Delphi: _ClassVar[Language]
    Diff: _ClassVar[Language]
    Dockerfile: _ClassVar[Language]
    Dyalog: _ClassVar[Language]
    Elixir: _ClassVar[Language]
    Erlang: _ClassVar[Language]
    FSharp: _ClassVar[Language]
    Fish: _ClassVar[Language]
    Flow: _ClassVar[Language]
    Fortran: _ClassVar[Language]
    Git_Commit: _ClassVar[Language]
    Git_Config: _ClassVar[Language]
    Git_Rebase: _ClassVar[Language]
    Go: _ClassVar[Language]
    GraphQL: _ClassVar[Language]
    Groovy: _ClassVar[Language]
    HTML: _ClassVar[Language]
    Hack: _ClassVar[Language]
    Handlebars: _ClassVar[Language]
    Haskell: _ClassVar[Language]
    Idris: _ClassVar[Language]
    Ini: _ClassVar[Language]
    J: _ClassVar[Language]
    JSON: _ClassVar[Language]
    Java: _ClassVar[Language]
    JavaScript: _ClassVar[Language]
    JavaScriptReact: _ClassVar[Language]
    Jsonnet: _ClassVar[Language]
    Julia: _ClassVar[Language]
    Justfile: _ClassVar[Language]
    Kotlin: _ClassVar[Language]
    LaTeX: _ClassVar[Language]
    Lean: _ClassVar[Language]
    Less: _ClassVar[Language]
    Lua: _ClassVar[Language]
    Luau: _ClassVar[Language]
    Makefile: _ClassVar[Language]
    Markdown: _ClassVar[Language]
    Matlab: _ClassVar[Language]
    Nickel: _ClassVar[Language]
    Nix: _ClassVar[Language]
    OCaml: _ClassVar[Language]
    Objective_C: _ClassVar[Language]
    Objective_CPP: _ClassVar[Language]
    Pascal: _ClassVar[Language]
    PHP: _ClassVar[Language]
    PLSQL: _ClassVar[Language]
    Perl: _ClassVar[Language]
    PowerShell: _ClassVar[Language]
    Prolog: _ClassVar[Language]
    Protobuf: _ClassVar[Language]
    Python: _ClassVar[Language]
    R: _ClassVar[Language]
    Racket: _ClassVar[Language]
    Raku: _ClassVar[Language]
    Razor: _ClassVar[Language]
    Repro: _ClassVar[Language]
    ReST: _ClassVar[Language]
    Ruby: _ClassVar[Language]
    Rust: _ClassVar[Language]
    SAS: _ClassVar[Language]
    SCSS: _ClassVar[Language]
    SML: _ClassVar[Language]
    SQL: _ClassVar[Language]
    Sass: _ClassVar[Language]
    Scala: _ClassVar[Language]
    Scheme: _ClassVar[Language]
    ShellScript: _ClassVar[Language]
    Skylark: _ClassVar[Language]
    Slang: _ClassVar[Language]
    Solidity: _ClassVar[Language]
    Svelte: _ClassVar[Language]
    Swift: _ClassVar[Language]
    Tcl: _ClassVar[Language]
    TOML: _ClassVar[Language]
    TeX: _ClassVar[Language]
    Thrift: _ClassVar[Language]
    TypeScript: _ClassVar[Language]
    TypeScriptReact: _ClassVar[Language]
    Verilog: _ClassVar[Language]
    VHDL: _ClassVar[Language]
    VisualBasic: _ClassVar[Language]
    Vue: _ClassVar[Language]
    Wolfram: _ClassVar[Language]
    XML: _ClassVar[Language]
    XSL: _ClassVar[Language]
    YAML: _ClassVar[Language]
    Zig: _ClassVar[Language]
UnspecifiedProtocolVersion: ProtocolVersion
UnspecifiedTextEncoding: TextEncoding
UTF8: TextEncoding
UTF16: TextEncoding
UnspecifiedPositionEncoding: PositionEncoding
UTF8CodeUnitOffsetFromLineStart: PositionEncoding
UTF16CodeUnitOffsetFromLineStart: PositionEncoding
UTF32CodeUnitOffsetFromLineStart: PositionEncoding
UnspecifiedSymbolRole: SymbolRole
Definition: SymbolRole
Import: SymbolRole
WriteAccess: SymbolRole
ReadAccess: SymbolRole
Generated: SymbolRole
Test: SymbolRole
ForwardDefinition: SymbolRole
UnspecifiedSyntaxKind: SyntaxKind
Comment: SyntaxKind
PunctuationDelimiter: SyntaxKind
PunctuationBracket: SyntaxKind
Keyword: SyntaxKind
IdentifierKeyword: SyntaxKind
IdentifierOperator: SyntaxKind
Identifier: SyntaxKind
IdentifierBuiltin: SyntaxKind
IdentifierNull: SyntaxKind
IdentifierConstant: SyntaxKind
IdentifierMutableGlobal: SyntaxKind
IdentifierParameter: SyntaxKind
IdentifierLocal: SyntaxKind
IdentifierShadowed: SyntaxKind
IdentifierNamespace: SyntaxKind
IdentifierModule: SyntaxKind
IdentifierFunction: SyntaxKind
IdentifierFunctionDefinition: SyntaxKind
IdentifierMacro: SyntaxKind
IdentifierMacroDefinition: SyntaxKind
IdentifierType: SyntaxKind
IdentifierBuiltinType: SyntaxKind
IdentifierAttribute: SyntaxKind
RegexEscape: SyntaxKind
RegexRepeated: SyntaxKind
RegexWildcard: SyntaxKind
RegexDelimiter: SyntaxKind
RegexJoin: SyntaxKind
StringLiteral: SyntaxKind
StringLiteralEscape: SyntaxKind
StringLiteralSpecial: SyntaxKind
StringLiteralKey: SyntaxKind
CharacterLiteral: SyntaxKind
NumericLiteral: SyntaxKind
BooleanLiteral: SyntaxKind
Tag: SyntaxKind
TagAttribute: SyntaxKind
TagDelimiter: SyntaxKind
UnspecifiedSeverity: Severity
Error: Severity
Warning: Severity
Information: Severity
Hint: Severity
UnspecifiedDiagnosticTag: DiagnosticTag
Unnecessary: DiagnosticTag
Deprecated: DiagnosticTag
UnspecifiedLanguage: Language
ABAP: Language
Apex: Language
APL: Language
Ada: Language
Agda: Language
AsciiDoc: Language
Assembly: Language
Awk: Language
Bat: Language
BibTeX: Language
C: Language
COBOL: Language
CPP: Language
CSS: Language
CSharp: Language
Clojure: Language
Coffeescript: Language
CommonLisp: Language
Coq: Language
CUDA: Language
Dart: Language
Delphi: Language
Diff: Language
Dockerfile: Language
Dyalog: Language
Elixir: Language
Erlang: Language
FSharp: Language
Fish: Language
Flow: Language
Fortran: Language
Git_Commit: Language
Git_Config: Language
Git_Rebase: Language
Go: Language
GraphQL: Language
Groovy: Language
HTML: Language
Hack: Language
Handlebars: Language
Haskell: Language
Idris: Language
Ini: Language
J: Language
JSON: Language
Java: Language
JavaScript: Language
JavaScriptReact: Language
Jsonnet: Language
Julia: Language
Justfile: Language
Kotlin: Language
LaTeX: Language
Lean: Language
Less: Language
Lua: Language
Luau: Language
Makefile: Language
Markdown: Language
Matlab: Language
Nickel: Language
Nix: Language
OCaml: Language
Objective_C: Language
Objective_CPP: Language
Pascal: Language
PHP: Language
PLSQL: Language
Perl: Language
PowerShell: Language
Prolog: Language
Protobuf: Language
Python: Language
R: Language
Racket: Language
Raku: Language
Razor: Language
Repro: Language
ReST: Language
Ruby: Language
Rust: Language
SAS: Language
SCSS: Language
SML: Language
SQL: Language
Sass: Language
Scala: Language
Scheme: Language
ShellScript: Language
Skylark: Language
Slang: Language
Solidity: Language
Svelte: Language
Swift: Language
Tcl: Language
TOML: Language
TeX: Language
Thrift: Language
TypeScript: Language
TypeScriptReact: Language
Verilog: Language
VHDL: Language
VisualBasic: Language
Vue: Language
Wolfram: Language
XML: Language
XSL: Language
YAML: Language
Zig: Language

class Index(_message.Message):
    __slots__ = ("metadata", "documents", "external_symbols")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_SYMBOLS_FIELD_NUMBER: _ClassVar[int]
    metadata: Metadata
    documents: _containers.RepeatedCompositeFieldContainer[Document]
    external_symbols: _containers.RepeatedCompositeFieldContainer[SymbolInformation]
    def __init__(self, metadata: _Optional[_Union[Metadata, _Mapping]] = ..., documents: _Optional[_Iterable[_Union[Document, _Mapping]]] = ..., external_symbols: _Optional[_Iterable[_Union[SymbolInformation, _Mapping]]] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ("version", "tool_info", "project_root", "text_document_encoding")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TOOL_INFO_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ROOT_FIELD_NUMBER: _ClassVar[int]
    TEXT_DOCUMENT_ENCODING_FIELD_NUMBER: _ClassVar[int]
    version: ProtocolVersion
    tool_info: ToolInfo
    project_root: str
    text_document_encoding: TextEncoding
    def __init__(self, version: _Optional[_Union[ProtocolVersion, str]] = ..., tool_info: _Optional[_Union[ToolInfo, _Mapping]] = ..., project_root: _Optional[str] = ..., text_document_encoding: _Optional[_Union[TextEncoding, str]] = ...) -> None: ...

class ToolInfo(_message.Message):
    __slots__ = ("name", "version", "arguments")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    arguments: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., arguments: _Optional[_Iterable[str]] = ...) -> None: ...

class Document(_message.Message):
    __slots__ = ("language", "relative_path", "occurrences", "symbols", "text", "position_encoding")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    OCCURRENCES_FIELD_NUMBER: _ClassVar[int]
    SYMBOLS_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    POSITION_ENCODING_FIELD_NUMBER: _ClassVar[int]
    language: str
    relative_path: str
    occurrences: _containers.RepeatedCompositeFieldContainer[Occurrence]
    symbols: _containers.RepeatedCompositeFieldContainer[SymbolInformation]
    text: str
    position_encoding: PositionEncoding
    def __init__(self, language: _Optional[str] = ..., relative_path: _Optional[str] = ..., occurrences: _Optional[_Iterable[_Union[Occurrence, _Mapping]]] = ..., symbols: _Optional[_Iterable[_Union[SymbolInformation, _Mapping]]] = ..., text: _Optional[str] = ..., position_encoding: _Optional[_Union[PositionEncoding, str]] = ...) -> None: ...

class Symbol(_message.Message):
    __slots__ = ("scheme", "package", "descriptors")
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    scheme: str
    package: Package
    descriptors: _containers.RepeatedCompositeFieldContainer[Descriptor]
    def __init__(self, scheme: _Optional[str] = ..., package: _Optional[_Union[Package, _Mapping]] = ..., descriptors: _Optional[_Iterable[_Union[Descriptor, _Mapping]]] = ...) -> None: ...

class Package(_message.Message):
    __slots__ = ("manager", "name", "version")
    MANAGER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    manager: str
    name: str
    version: str
    def __init__(self, manager: _Optional[str] = ..., name: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class Descriptor(_message.Message):
    __slots__ = ("name", "disambiguator", "suffix")
    class Suffix(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UnspecifiedSuffix: _ClassVar[Descriptor.Suffix]
        Namespace: _ClassVar[Descriptor.Suffix]
        Package: _ClassVar[Descriptor.Suffix]
        Type: _ClassVar[Descriptor.Suffix]
        Term: _ClassVar[Descriptor.Suffix]
        Method: _ClassVar[Descriptor.Suffix]
        TypeParameter: _ClassVar[Descriptor.Suffix]
        Parameter: _ClassVar[Descriptor.Suffix]
        Meta: _ClassVar[Descriptor.Suffix]
        Local: _ClassVar[Descriptor.Suffix]
        Macro: _ClassVar[Descriptor.Suffix]
    UnspecifiedSuffix: Descriptor.Suffix
    Namespace: Descriptor.Suffix
    Package: Descriptor.Suffix
    Type: Descriptor.Suffix
    Term: Descriptor.Suffix
    Method: Descriptor.Suffix
    TypeParameter: Descriptor.Suffix
    Parameter: Descriptor.Suffix
    Meta: Descriptor.Suffix
    Local: Descriptor.Suffix
    Macro: Descriptor.Suffix
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISAMBIGUATOR_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    name: str
    disambiguator: str
    suffix: Descriptor.Suffix
    def __init__(self, name: _Optional[str] = ..., disambiguator: _Optional[str] = ..., suffix: _Optional[_Union[Descriptor.Suffix, str]] = ...) -> None: ...

class SymbolInformation(_message.Message):
    __slots__ = ("symbol", "documentation", "relationships", "kind", "display_name", "signature_documentation", "enclosing_symbol")
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UnspecifiedKind: _ClassVar[SymbolInformation.Kind]
        AbstractMethod: _ClassVar[SymbolInformation.Kind]
        Accessor: _ClassVar[SymbolInformation.Kind]
        Array: _ClassVar[SymbolInformation.Kind]
        Assertion: _ClassVar[SymbolInformation.Kind]
        AssociatedType: _ClassVar[SymbolInformation.Kind]
        Attribute: _ClassVar[SymbolInformation.Kind]
        Axiom: _ClassVar[SymbolInformation.Kind]
        Boolean: _ClassVar[SymbolInformation.Kind]
        Class: _ClassVar[SymbolInformation.Kind]
        Constant: _ClassVar[SymbolInformation.Kind]
        Constructor: _ClassVar[SymbolInformation.Kind]
        Contract: _ClassVar[SymbolInformation.Kind]
        DataFamily: _ClassVar[SymbolInformation.Kind]
        Delegate: _ClassVar[SymbolInformation.Kind]
        Enum: _ClassVar[SymbolInformation.Kind]
        EnumMember: _ClassVar[SymbolInformation.Kind]
        Error: _ClassVar[SymbolInformation.Kind]
        Event: _ClassVar[SymbolInformation.Kind]
        Fact: _ClassVar[SymbolInformation.Kind]
        Field: _ClassVar[SymbolInformation.Kind]
        File: _ClassVar[SymbolInformation.Kind]
        Function: _ClassVar[SymbolInformation.Kind]
        Getter: _ClassVar[SymbolInformation.Kind]
        Grammar: _ClassVar[SymbolInformation.Kind]
        Instance: _ClassVar[SymbolInformation.Kind]
        Interface: _ClassVar[SymbolInformation.Kind]
        Key: _ClassVar[SymbolInformation.Kind]
        Lang: _ClassVar[SymbolInformation.Kind]
        Lemma: _ClassVar[SymbolInformation.Kind]
        Library: _ClassVar[SymbolInformation.Kind]
        Macro: _ClassVar[SymbolInformation.Kind]
        Method: _ClassVar[SymbolInformation.Kind]
        MethodAlias: _ClassVar[SymbolInformation.Kind]
        MethodReceiver: _ClassVar[SymbolInformation.Kind]
        MethodSpecification: _ClassVar[SymbolInformation.Kind]
        Message: _ClassVar[SymbolInformation.Kind]
        Modifier: _ClassVar[SymbolInformation.Kind]
        Module: _ClassVar[SymbolInformation.Kind]
        Namespace: _ClassVar[SymbolInformation.Kind]
        Null: _ClassVar[SymbolInformation.Kind]
        Number: _ClassVar[SymbolInformation.Kind]
        Object: _ClassVar[SymbolInformation.Kind]
        Operator: _ClassVar[SymbolInformation.Kind]
        Package: _ClassVar[SymbolInformation.Kind]
        PackageObject: _ClassVar[SymbolInformation.Kind]
        Parameter: _ClassVar[SymbolInformation.Kind]
        ParameterLabel: _ClassVar[SymbolInformation.Kind]
        Pattern: _ClassVar[SymbolInformation.Kind]
        Predicate: _ClassVar[SymbolInformation.Kind]
        Property: _ClassVar[SymbolInformation.Kind]
        Protocol: _ClassVar[SymbolInformation.Kind]
        ProtocolMethod: _ClassVar[SymbolInformation.Kind]
        PureVirtualMethod: _ClassVar[SymbolInformation.Kind]
        Quasiquoter: _ClassVar[SymbolInformation.Kind]
        SelfParameter: _ClassVar[SymbolInformation.Kind]
        Setter: _ClassVar[SymbolInformation.Kind]
        Signature: _ClassVar[SymbolInformation.Kind]
        SingletonClass: _ClassVar[SymbolInformation.Kind]
        SingletonMethod: _ClassVar[SymbolInformation.Kind]
        StaticDataMember: _ClassVar[SymbolInformation.Kind]
        StaticEvent: _ClassVar[SymbolInformation.Kind]
        StaticField: _ClassVar[SymbolInformation.Kind]
        StaticMethod: _ClassVar[SymbolInformation.Kind]
        StaticProperty: _ClassVar[SymbolInformation.Kind]
        StaticVariable: _ClassVar[SymbolInformation.Kind]
        String: _ClassVar[SymbolInformation.Kind]
        Struct: _ClassVar[SymbolInformation.Kind]
        Subscript: _ClassVar[SymbolInformation.Kind]
        Tactic: _ClassVar[SymbolInformation.Kind]
        Theorem: _ClassVar[SymbolInformation.Kind]
        ThisParameter: _ClassVar[SymbolInformation.Kind]
        Trait: _ClassVar[SymbolInformation.Kind]
        TraitMethod: _ClassVar[SymbolInformation.Kind]
        Type: _ClassVar[SymbolInformation.Kind]
        TypeAlias: _ClassVar[SymbolInformation.Kind]
        TypeClass: _ClassVar[SymbolInformation.Kind]
        TypeClassMethod: _ClassVar[SymbolInformation.Kind]
        TypeFamily: _ClassVar[SymbolInformation.Kind]
        TypeParameter: _ClassVar[SymbolInformation.Kind]
        Union: _ClassVar[SymbolInformation.Kind]
        Value: _ClassVar[SymbolInformation.Kind]
        Variable: _ClassVar[SymbolInformation.Kind]
    UnspecifiedKind: SymbolInformation.Kind
    AbstractMethod: SymbolInformation.Kind
    Accessor: SymbolInformation.Kind
    Array: SymbolInformation.Kind
    Assertion: SymbolInformation.Kind
    AssociatedType: SymbolInformation.Kind
    Attribute: SymbolInformation.Kind
    Axiom: SymbolInformation.Kind
    Boolean: SymbolInformation.Kind
    Class: SymbolInformation.Kind
    Constant: SymbolInformation.Kind
    Constructor: SymbolInformation.Kind
    Contract: SymbolInformation.Kind
    DataFamily: SymbolInformation.Kind
    Delegate: SymbolInformation.Kind
    Enum: SymbolInformation.Kind
    EnumMember: SymbolInformation.Kind
    Error: SymbolInformation.Kind
    Event: SymbolInformation.Kind
    Fact: SymbolInformation.Kind
    Field: SymbolInformation.Kind
    File: SymbolInformation.Kind
    Function: SymbolInformation.Kind
    Getter: SymbolInformation.Kind
    Grammar: SymbolInformation.Kind
    Instance: SymbolInformation.Kind
    Interface: SymbolInformation.Kind
    Key: SymbolInformation.Kind
    Lang: SymbolInformation.Kind
    Lemma: SymbolInformation.Kind
    Library: SymbolInformation.Kind
    Macro: SymbolInformation.Kind
    Method: SymbolInformation.Kind
    MethodAlias: SymbolInformation.Kind
    MethodReceiver: SymbolInformation.Kind
    MethodSpecification: SymbolInformation.Kind
    Message: SymbolInformation.Kind
    Modifier: SymbolInformation.Kind
    Module: SymbolInformation.Kind
    Namespace: SymbolInformation.Kind
    Null: SymbolInformation.Kind
    Number: SymbolInformation.Kind
    Object: SymbolInformation.Kind
    Operator: SymbolInformation.Kind
    Package: SymbolInformation.Kind
    PackageObject: SymbolInformation.Kind
    Parameter: SymbolInformation.Kind
    ParameterLabel: SymbolInformation.Kind
    Pattern: SymbolInformation.Kind
    Predicate: SymbolInformation.Kind
    Property: SymbolInformation.Kind
    Protocol: SymbolInformation.Kind
    ProtocolMethod: SymbolInformation.Kind
    PureVirtualMethod: SymbolInformation.Kind
    Quasiquoter: SymbolInformation.Kind
    SelfParameter: SymbolInformation.Kind
    Setter: SymbolInformation.Kind
    Signature: SymbolInformation.Kind
    SingletonClass: SymbolInformation.Kind
    SingletonMethod: SymbolInformation.Kind
    StaticDataMember: SymbolInformation.Kind
    StaticEvent: SymbolInformation.Kind
    StaticField: SymbolInformation.Kind
    StaticMethod: SymbolInformation.Kind
    StaticProperty: SymbolInformation.Kind
    StaticVariable: SymbolInformation.Kind
    String: SymbolInformation.Kind
    Struct: SymbolInformation.Kind
    Subscript: SymbolInformation.Kind
    Tactic: SymbolInformation.Kind
    Theorem: SymbolInformation.Kind
    ThisParameter: SymbolInformation.Kind
    Trait: SymbolInformation.Kind
    TraitMethod: SymbolInformation.Kind
    Type: SymbolInformation.Kind
    TypeAlias: SymbolInformation.Kind
    TypeClass: SymbolInformation.Kind
    TypeClassMethod: SymbolInformation.Kind
    TypeFamily: SymbolInformation.Kind
    TypeParameter: SymbolInformation.Kind
    Union: SymbolInformation.Kind
    Value: SymbolInformation.Kind
    Variable: SymbolInformation.Kind
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    ENCLOSING_SYMBOL_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    documentation: _containers.RepeatedScalarFieldContainer[str]
    relationships: _containers.RepeatedCompositeFieldContainer[Relationship]
    kind: SymbolInformation.Kind
    display_name: str
    signature_documentation: Document
    enclosing_symbol: str
    def __init__(self, symbol: _Optional[str] = ..., documentation: _Optional[_Iterable[str]] = ..., relationships: _Optional[_Iterable[_Union[Relationship, _Mapping]]] = ..., kind: _Optional[_Union[SymbolInformation.Kind, str]] = ..., display_name: _Optional[str] = ..., signature_documentation: _Optional[_Union[Document, _Mapping]] = ..., enclosing_symbol: _Optional[str] = ...) -> None: ...

class Relationship(_message.Message):
    __slots__ = ("symbol", "is_reference", "is_implementation", "is_type_definition", "is_definition")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    IS_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    IS_IMPLEMENTATION_FIELD_NUMBER: _ClassVar[int]
    IS_TYPE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    IS_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    is_reference: bool
    is_implementation: bool
    is_type_definition: bool
    is_definition: bool
    def __init__(self, symbol: _Optional[str] = ..., is_reference: bool = ..., is_implementation: bool = ..., is_type_definition: bool = ..., is_definition: bool = ...) -> None: ...

class Occurrence(_message.Message):
    __slots__ = ("range", "symbol", "symbol_roles", "override_documentation", "syntax_kind", "diagnostics", "enclosing_range")
    RANGE_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_ROLES_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    SYNTAX_KIND_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    ENCLOSING_RANGE_FIELD_NUMBER: _ClassVar[int]
    range: _containers.RepeatedScalarFieldContainer[int]
    symbol: str
    symbol_roles: int
    override_documentation: _containers.RepeatedScalarFieldContainer[str]
    syntax_kind: SyntaxKind
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    enclosing_range: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, range: _Optional[_Iterable[int]] = ..., symbol: _Optional[str] = ..., symbol_roles: _Optional[int] = ..., override_documentation: _Optional[_Iterable[str]] = ..., syntax_kind: _Optional[_Union[SyntaxKind, str]] = ..., diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ..., enclosing_range: _Optional[_Iterable[int]] = ...) -> None: ...

class Diagnostic(_message.Message):
    __slots__ = ("severity", "code", "message", "source", "tags")
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    severity: Severity
    code: str
    message: str
    source: str
    tags: _containers.RepeatedScalarFieldContainer[DiagnosticTag]
    def __init__(self, severity: _Optional[_Union[Severity, str]] = ..., code: _Optional[str] = ..., message: _Optional[str] = ..., source: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[DiagnosticTag, str]]] = ...) -> None: ...
