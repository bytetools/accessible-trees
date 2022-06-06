# used if you want to add links to the tree, or a node in the tree
ID = "t1"

# example of tree (commented out)
'''
tree  = [
  ("root", [
    ("child", [
      "grandchild", "grandchild"
    ]),
    ("child", []),
  ]),
]
'''

# every node is written ("value", [])
# the list inside contains all children of that node
# a string can also be used (i.e. "grandchildren"), but it can have no children

# the tree you want converted to HTML, here:
'''
tree = [
  ("n", [
    ("n/2", [
      ("n/4", [
        ("n/8", [
          ("...", [
            ("2", [
              "1", "1"
            ]),
          ]),
        ]),
        ("n/8", [
          "..."
        ]),
      ]),
      ("n/4", [
        ("n/8", [
          "..."
        ]),
        ("n/8", [
          "..."
        ]),
      ]),
    ]),
    ("n/2", [
      ("n/4", [
        ("n/8", [
          "..."
        ]),
        ("n/8", [
          "..."
        ]),
      ]),
      ("n/4", [
        ("n/8", [
          "..."
        ]),
        ("n/8", [
          "..."
        ]),
      ]),
    ]),
  ]),
]
'''

'''
tree = [
  ("Main verb", [
    ("verb", [
      "<span id=\"stay\">stay</span>"
    ]),
    ("tense", [
      "present (-s) stay(s)",
      "past (-ed) stayed"
    ]),
    ("modality/aspect", [
      ("modal auxiliary", [
        "could (modality); <a href=\"#stay\">arrow to stay</a>, <a href=\"#have\">arrow to have</a>, <a href=\"#beis\">arrow to be/is</a>"
      ]),
      ("auxiliaries", [
        "<span id=\"have\">have</span>",
        "<span id=\"beis\">be/is</span>",
      ]),
      ("past participle", [
        "stayed (perfective)"
      ]),
      ("present participle", [
        "staying (progressive aspect)"
      ]),
    ]),
  ]), 
]
'''

'''
tree = [
  ("fib(5): 5", [
    ("fib(4): 3", [
      ("fib(3): 2", [
        ("fib(2): 1", [
          ("fib(1): 1", []),
          ("fib(0): 0", []),
        ]),
        ("fib(1): 1", []),
      ]),
      ("fib(2): 1", [
        ("fib(1): 1", []),
        ("fib(0): 0", []),
      ]),
    ]),
    ("fib(3): 2", [
      ("fib(2): 1", [
        ("fib(1): 1", []),
        ("fiv(0): 0", []),
      ]),
      ("fib(1): 1", []),
    ]),
  ]),
]
'''

'''
tree = [
  ("&lt;html&gt;", [
    ("&lt;head&gt;", [
      "&lt;meta&gt;", "&lt;title&gt;"
    ]),
    ("&lt;body&gt;", [
      ("&lt;h1&gt;", []),
      ("&lt;h2&gt;", []),
      ("&lt;ul&gt;", [
        "&lt;li&gt;",
        "&lt;li&gt;",
      ]),
      ("&lt;h3&gt;", []),
      ("&lt;p&gt;", [
        "&lt;a&gt;"
      ]),
      ("&lt;p&gt;", []),
      ("{&lt;div&gt;}", [
        ("{&lt;p&gt;}", ["{&lt;time&gt;}"]),
        ("{&lt;p&gt;}", []),
      ]),
      ("{&lt;div&gt;}", [
        ("{&lt;p&gt;}", ["{&lt;time&gt;}"]),
        ("{&lt;p&gt;}", []),
      ]),
      ("&lt;div&gt;", []),
      ("&lt;p&gt;", ["&lt;small&gt;"]),
    ]),
  ]),
]
'''

'''
tree = [
  ("NP", [
    ("Determiners (closed class, function words", [
      ("PreArt", [
        ("quantifiers<br>{some} (of)", []),
        ("partitive<br>(a) {little} of", []),
        ("fractions<br>{three}-fourths", []),
        ("multipliers<br>once (a/every/each)", []),
      ]),
      ("PossProD", [
        "{my}"
      ]),
      ("Articles", [
        ("DefArt", ["{the}"]),
        ("IndefArt", ["a/{an}"]),
      ]),
      ("Demonstrative", [
        "this", "that"
      ]),
      ("Number", [
        "three", "third"
      ]),
    ]),
    ("Genetives", [
      ("Inflective", ["the people's joy"]),
      ("Phrasal", ["the joy of the people"]),
    ]),
    ("Adjectives (open class, content words)", ["nice"]),
    ("Noun or Pro", [
      ("Proper", ["Monaco"]),
      ("Common", ["books"]),
      ("Pro", ["he"]),
    ]),
    ("PostN", ["both"]),
    ("Other", [
      ("{RelCl}<br>which I told {you} about", []),
      ("PP<br>in red", []),
      ("Other", []),
    ]),
  ]),
]
'''

'''
tree = [
  ("document (Document root)", [
    ("html (Nodes)", [
      ("&lt;head&gt; (sibling nodes)", [
        ("&lt;meta&gt;", []),
        ("&lt;title&gt;", []),
      ]),
      ("&lt;body&gt; (sibling nodes; parent of h1)", [
        ("&lt;h1&gt; (child of body)", []),
        ("&lt;p&gt;", ["&lt;a&gt;"]),
        ("&lt;img&gt;", []),
        ("&lt;h2&gt;", []),
        ("&lt;div&gt;", [
          ("&lt;p&gt;", [
            ("&lt;time&gt;", []),
          ]),
          ("&lt;p&gt;", []),
        ]),
        ("&lt;div&gt;", [
          ("&lt;p&gt;", [
            ("&lt;time&gt;", []),
          ]),
          ("&lt;p&gt;", []),
        ]),
      ]),
    ]),
  ]),
]
'''

"""
tree = [
  ("&lt;p&gt; Element node", [
    ("Photo of Conservatory Pond in", []),
    ("&lt;a&gt;", [
      ("  href=\"http://www.centralpark.com/\"", []),
      ("Central Park", []),
    ]),
    ("[return and spaces]", []),
  ]),
]
"""

'''
tree = [
  ("qs(arr, o, n-1) [1, n]", [
    ("qs(...) [2, n/2]", [
      ("qs(...) [3, n/4]", []),
      ("qs(...) [3, n/4]", []),
    ]),
    ("qs(...) [2, n/2]", [
      ("qs(...) [3, n/4]", []),
      ("qs(...) [3, n/4]", []),
    ]),
  ]),
]
'''

'''
tree = [
  ("...", [
    "qs(...) [{% katex %} \log_{2}(n) {% endkatex %}, 1]",
    "qs(...) [{% katex %} \log_{2}(n) {% endkatex %}, 1]"
  ])
]
'''

"""
tree = [
  ("NP", [
    "Det: the",
    "Adj: old",
    "N (H): man", 
  ]),
]
"""

'''
tree = [
  ("PP", [
    "P (H): in",
    ("NP", [
      "Det: the",
      "N (H): garden"
    ]),
  ]),
]
'''

'''
tree = [
  ("label: root", [
    ("label: node", [
      ("(blank node)", [
        ("(blank node, right)", []),
      ]),
      "(blank node)",
    ]),
    ("(blank node)", [
      "(blank node, right"
    ]),
  ])
]
'''
"""
tree = [
  ("(empty node)", [
    ("(empty node, left)", [
      "(empty node, left)",
      "(empty node, center)",
      "(empty node, right)",
    ]),
    ("(empty node, center)", [
    ]),
    ("(empty node, right)", [
      "(empty node, center)"
    ]),
  ]),
]
"""

'''
tree = [
  "(empty node)"
]
'''

"""
tree = [
  ("(empty node)", [
    ("(empty node)", [
      ("(empty node)", []),
      ("(empty node)", []),
    ]),
    ("(empty node) ", []),
  ]),
]
"""

'''
tree = [
  ("A", [
    ("B (subtree rooted at B)", [
      "E (subtree rooted at B, leaf)", "F (subtree rooted at B, leaf)",
    ]),
    "C (leaf)",
    ("D", [
      "G (right, leaf)"
    ]),
  ]),
]
'''

"""
tree = [
  ("A", [
    ("B (left subtree of A)", [
      ("D (left subtree of A)", [
        "H (left, left subtree of A)"
      ]),
      ("E (left subtree of A)", []),
    ]),
    ("C (right child of A)", [
      ("F", []),
      ("G (right subtree of C)", [
        "I (right subtree of C)", "J (right subtree of C)",
      ]),
    ]),
  ]),
]
"""

"""
tree = [
  ("A (height of the tree is 3)", [
    ("B (level 1, height of node B is 2)", [
      ("D (level 2)", [
        ("H (left, level 3)", []),
      ]),
      ("E (level 2, depth of node E is 2)", []),
    ]),
    ("C (level 1)", [
      ("F (level 2)", []),
      ("G (level 2)", [
        ("I (level 3)", []),
        ("J (level 3)", []),
      ]),
    ]),
  ]),
]
"""

'''
tree = [
  ("A", [
    ("B", [
      ("D", []),
      ("E", []),
    ]),
    ("C", [
      ("F", []),
      ("G", []),
    ]),
  ]),
]
'''

"""
tree = [
  ("01", [
    ("11", [
      ("21", [
        ("31", []),
        ("32", []),
      ]),
      ("22", [
        ("33", []),
        ("34", []),
      ]),
    ]),
    ("12", [
      ("23", [
        ("35", []),
        ("36", []),
      ]),
      ("24", [
        ("37", []),
        ("38", []),
      ]),
    ]),
  ]),
]
"""

'''
tree = [
  ("A", [
    ("B", [
      ("D", []),
      ("E", []),
    ]),
    ("C", [
      ("F (left)", []),
    ]),
  ]),
]
'''

"""
tree = [
  ("A", [
    ("B", ["D (left)"]),
    ("C", [
      ("E", [
        ("G (right)", []),
      ]),
      ("F", []),
    ]),
  ]),
]
"""

'''
tree = [
  ("A", [
    ("B (left)", [
      ("C", []),
      ("D", []),
    ]),
  ]),
]
'''


"""
tree = [
  ("8", [
    ("4", [
      ("2", ["1 (right)"]),
      ("3", []),
    ]),
    ("7", [
      "5", "6"
    ]),
  ]),
]
"""

'''
tree = [
  ("Sentence (all items are green, except for red subtree)", [
    ("NP:Subj", ["I &ndash; Pro"]),
    ("VP:Pred", [
      ("MV:Pres", ["know &ndash; VT",
        ("NP:DO", [
          ("NP:Head", [
            ("Det", [
              ("the &ndash; DefArt", []),
            ]),
            "man &ndash; N"
          ]),
          ("RefCl:Adj (subtree is red)", [
            ("NP:Subj", [
              "that &ndash; that"
            ]),
            ("VP:Pred", [
              ("MV:Past", [
                "caused &ndash; VT",
              ]),
              ("NP:DO", [
                ("Det", [
                  "the &ndash; DefArt",
                ]),
                "accident &ndash; N"
              ]),
            ]),
          ]),
        ]),
      ]),
    ]),
  ]),
]
'''

"""
tree = [
  ("17", [
    ("13", [
      ("9", ["11 (right)"]),
      ("16", []),
    ]),
    ("27", [
      ("20", []),
      ("39", []),
    ]),
  ]),
]
"""
'''
tree = [
  ("5", [
    ("3", [
      ("1", ["2 (right)"]),
      ("4", []),
    ]),
    ("7", [
      ("6", []),
      ("8", []),
    ]),
  ]),
]
'''
'''
tree = [
  ("black", [
    ("red", [
      ("orange", ["green (right)"]),
      ("yellow", []),
    ]),
    ("purple", [
      ("light blue", []),
      ("blue", []),
    ]),
  ]),
]
'''

'''
tree = [
  ("47", [
    ("32", [
      ("19", [
        ("10", [
          ("7", []),
          ("12", []),
        ]),
        ("23", [
          ("30 (right)", []),
        ]),
      ]),
      ("41", [
        ("37", []),
        ("44", ["43 (left, inserted)"]),
      ]),
    ]),
    ("63", [
      ("54", [
        ("53", []),
        ("59", ["57 (left)"]),
      ]),
      ("79", [
        ("96 (right)", [
          ("91", []),
          ("97", []),
        ]),
      ]),
    ]),
  ]),
]
'''
'''
tree = [
  ("7", [
    ("4", [
      ("1", []),
      ("5", []),
    ]),
    ("9", []),
  ]),
]
'''

'''
tree = [
  ("9", [
    ("1 (left)", [
      ("7 (right)", [
        ("4 (left)", [
          ("5 (right)", []),
        ]),
      ]),
    ]),
  ]),
]
'''

'''
tree = [
  ("37", [
    ("19", []),
    ("41", []),
  ]),
]
'''

tree = [
  ("47", [
    ("32", [
      ("19", [
        ("10", [
          ("7", []),
          ("12", []),
        ]),
        ("23", ["30 (right)"]),
      ]),
      ("41", [
        ("44", []),
        ("37", []),
      ]),
    ]),
    ("59", [
      ("54", [
        ("53", []),
        ("57", []),
      ]),
      ("96", [
        ("91", []),
        ("97", []),
      ]),
    ]),
  ]),
]

'''
tree = [
  ("63", [
    ("54 (parent)", [
      ("53", []),
      ("59 (nd; isLeftChild = false)" ,["57 (left)"]),
    ]),
    ("79", [
      ("96 (right)", [
        ("91", []),
        ("97", []),
      ]),
    ]),
  ]),
]
'''

'''
tree = [
  ("59", [
    ("57", []),
  ]),
]
'''

'''
tree = [
  ("59", [
    ("54", []),
    ("96", []),
  ]),
]
'''

'''
tree = [
  ("root", [
    ("R", [
    ]),
  ]),
]
'''

'''
tree = [
  ("94 (0, green, changed)", [
    ("76 (1, green)", [
      ("70 (3, green)", [
        ("27 (7, green)", []),
        ("36 (8, green)", []),
      ]),
      ("48 (4, green)", [
        ("29 (9, green)", []),
        ("37 (10, green)", []),
      ]),
    ]),
    ("89 (2, green, changed)", [
      ("58 (5, green)", [
        ("42 (11, green)", []),
        ("23 (12, green)", []),
      ]),
      ("13 (6, green)", [
      ]),
    ]),
  ]),
]
'''

'''
tree = [
  ("0 (level 0)", [
    ("1 (level 1)", [
      ("3 (level 2)", []),
      ("4 (level 2)", []),
    ]),
    ("2 (level 1)", [
      ("5 (level 2)", []),
      ("6 (level 2)", []),
    ]),
  ]),
]
'''

'''
tree = [
  ("43", [
    ("24", [
      ("12", []),
      ("37", []),
    ]),
    ("61", []),
  ]),
]
'''

'''
tree = [
  ("61", [
    ("12 (left)", [
      ("43 (right)", [
        ("37 (left)", [
          ("24 (left)", []),
        ]),
      ]),
    ]),
  ]),
]
'''

'''
tree = [
  ("root (black)", [
    ("(red, left)", [
      ("(black, left)", [
        ("(red, left)", [
          ("(black, leaves)", []),
          ("(black, leaves)", []),
        ]),
      ]),
    ]),
  ]),
]
'''

'''
tree = [
  ("root (black)", [
    ("(red)", [
      ("(black)", [
        ("(red)", [
          ("(black; leaves, imagined)", []),
          ("(black; leaves, imagined)", []),
        ]),
        ("(red)", [
          ("(black; leaves, imagined)", []),
          ("(black; leaves, imagined)", []),
        ]),
      ]),
      ("(black)", [
        ("(red)", [
          ("(black; leaves, imagined)", []),
          ("(black; leaves, imagined)", []),
        ]),
        ("(red)", [
          ("(black; leaves, imagined)", []),
          ("(black; leaves, imagined)", []),
        ]),
      ]),
    ]),
    ("(red)", [
      ("(black)", [
        ("(red)", [
          ("(black; leaves, imagined)", []),
          ("(black; leaves, imagined)", []),
        ]),
        ("(red)", [
          ("(black; leaves, imagined)", []),
          ("(black; leaves, imagined)", []),
        ]),
      ]),
      ("(black)", [
        ("(red)", [
          ("(black; leaves, imagined)", []),
          ("(black; leaves, imagined)", []),
        ]),
        ("(red)", [
          ("(black; leaves, imagined)", []),
          ("(black; leaves, imagined)", []),
        ]),
      ]),
    ]),
  ]),
]
'''

'''
tree = [
  ("x", [
    ("y", [
      ("A (tree)", []),
      ("B (tree)", []),
    ]),
    ("z", [
      ("C (tree)", []),
      ("D (tree)", []),
    ]),
  ]),
]
'''
'''
tree = [
  ("47", [
    ("32", [
      ("13 (left)", []),
    ]),
    ("81", []),
  ]),
]
'''
'''
tree = [
  ("40 (temp)", [
    ("44 (right)", []),
  ]),
]
'''

"""
tree = [
  ("47", [
    ("81 (right)", []),
  ]),
]
"""
"""
tree = [
  ("40", [
    ("37 (left)", []),
  ]),
]
"""
'''
tree = [
("32 (temp)", [
  ("13 (left)", [
    ("7", []),
    ("29", []),
  ]),
]),
]
'''

'''
tree = [
  ("32 (temp)", [
    ("13", [
      ("7", []),
      ("29", []),
    ]),
    ("47", [
      ("40", [
        ("37 (left)", []),
      ]),
      ("81", []),
    ]),
  ]),
]
'''

'''
tree = [
  ("47 (yellow arrow to 40)", [
    ("32 (x, yellow arrow to 37)", [
      ("13", []),
      ("40 (y, yellow arrow to 32)", [
        ("37", []),
        ("44", []),
      ]),
    ]),
    ("81", []),
  ]),
]
'''

'''
tree = [
  ("root (black)", [
    ("x (red)", [
    ]),
    ("blank node (red)", [
      ("{% katex %}y_{null}{% endkatex %} (black, right)", []),
    ]),
  ]),
]
'''

'''
tree = [
  ("47 (black)", [
    ("32 (black)", [
      ("black node", []),
      ("black node", []),
    ]),
    ("71 (red)", [
      ("65 (black)", [
        ("black node", []),
        ("black node", []),
      ]),
      ("87 (black)", [
        ("82 (red)", [
          ("black node", []),
          ("black node", []),
        ]),
        ("93 (red)", [
          ("black node", []),
          ("black node", []),
        ]),
      ]),
    ]),
  ]),
]
'''

'''
tree = [
  ("root (blue)", [
    ("x (black)", [
    ]),
    ("y (red)", [
      ("black node", []),
      ("black node", []),
    ]),
  ]),
]
'''

'''
tree = [
  ("47 (black)", [
    ("32 (black)", [
      ("black node", []),
      ("black node", []),
    ]),
    ("65 (red)", [
      ("65 (black)", [
        ("51 (red)", [
          ("black node", []),
          ("black node", []),
        ]),
        ("black node", []),
      ]),
      ("direct connection to 51", []),
      ("87 (black)", [
        ("82 (red)", [
          ("black node", []),
          ("black node", []),
        ]),
        ("93 (red)", [
          ("black node", []),
          ("black node", []),
        ]),
      ]),
    ]),
  ]),
]
'''


'''
tree = [
  ("47 (black)", [
    ("32 (black)", []),
    ("65 (red)", [
      ("51 (black)", [
        ("black node", []),
        ("black node", []),
      ]),
      ("87 (black)", [
        ("82 (red)", [
          ("black node", []),
          ("black node", []),
        ]),
        ("93 (red)", [
          ("black node", []),
          ("black node", []),
        ]),
      ]),
    ]),
  ]),
]
'''

'''
tree = [
  ("47 (black)", [
    ("x (black)", []),
    ("71 (red)", [
      ("65 (black)", [
        ("black node", []),
        ("black node", []),
      ]),
      ("87 (black)", [
        ("82 (red)", [
          ("black node", []),
          ("black node", []),
        ]),
        ("93 (red)", [
          ("black node", []),
          ("black node", []),
        ]),
      ]),
    ]),
  ]),
]
'''

'''
tree = [
  ("47 (red)", [
    ("x (black)", []),
    ("71 (y, black)", [
      ("65 (black)", [
        ("black node", []),
        ("black node", []),
      ]),
      ("87 (black)", [
        ("82 (red)", [
          ("black node", []),
          ("black node", []),
        ]),
        ("93 (red)", [
          ("black node", []),
          ("black node", []),
        ]),
      ]),
    ]),
  ]),
]
'''

'''
tree = [
  ("71 (black)", [
    ("47 (red, new x)", [
      ("x (black)", []),
      ("65 (red, y)", [
        ("black node", []),
        ("black node", []),
      ]),
    ]),
    ("87 (black)", [
      ("82 (red)", [
        ("black node", []),
        ("black node", []),
      ]),
      ("93 (red)", [
        ("black node", []),
        ("black node", []),
      ]),
    ]),
  ]),
]
'''

"""
tree = [
  ("71 (black)", [
    ("47 (black, x)", [
      ("black node", []),
      ("65 (red)", [
        ("black node", []),
        ("black node", []),
      ]),
    ]),
    ("87 (black)", [
      ("82 (red)", [
        ("black node", []),
        ("black node", []),
      ]),
      ("93 (red)", [
        ("black node", []),
        ("black node", []),
      ]),
    ]),
  ]),
]
"""

'''
tree = [
  ("document", [
    ("&lt;html&gt;", [
      ("&lt;head&gt;", [
        ("&lt;meta&gt;", []),
        ("&lt;title&gt;", []),
      ]),
      ("&lt;body&gt;", [
        ("&lt;h1&gt;", []),
        ("&lt;p&gt;", [
          ("&lt;a&gt;", []),
        ]),
        ("&lt;img&gt;", []),
        ("&lt;h2&gt;", []),
        ("&lt;div&gt;", [
          ("&lt;p&gt;", [
            ("&lt;time&gt;", []),
          ]),
          ("&lt;p&gt;", []),
        ]),
        ("&lt;div&gt;", [
          ("&lt;p&gt;", [
            ("&lt;time&gt;", []),
          ]),
          ("&lt;p&gt;", []),
        ]),
      ]),
    ]),
  ]),
]
'''

tree = [
  ("&lt;p&gt; (Element node)", [
    ("Photo of Conservatory Pond in (Text node)", [
    ]),
    ("&lt;a&gt; (Element node)", [
      ("href=\"http://www.centralpark.com/\" (Attribute node)", []),
      ("Central Park (Text node)", []),
    ]),
    ("[return and spaces]", []),
  ]),
]
