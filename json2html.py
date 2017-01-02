from json2html import *

_json2conv = {
        "glossary": {
                "title": "example glossary",
                "GlossDiv": {
                        "title": "S",
                        "GlossList": {
                                "GlossEntry": {
                                        "ID": "SGML",
                                        "SortAs": "SGML",
                                        "GlossTerm": "Standard Generalized Markup Language",
                                        "Acronym": "SGML",
                                        "Abbrev": "ISO 8879:1986",
                                        "GlossDef": {
                                                "para": "A meta-markup language, used to create markup languages such as DocBook.",
                                                "GlossSeeAlso": ["GML", "XML"]
                                        },
                                        "GlossSee": "markup"
                                }
                        }
                }
        }
}

json2html.convert(json = _json2conv)
