import sqlite3 as sql
main_connect=sql.connect("main6.db")
main_curr=main_connect.cursor()
main_curr.execute("""
CREATE TABLE IF NOT EXISTS all_relation (
    relation_name TEXT PRIMARY KEY, 
    male_opposite TEXT,
    female_opposite TEXT
)
""")
relations = [

    # 👨‍👩‍👧 Parent → Child
    ("father", "son", "daughter"),
    ("mother", "son", "daughter"),
    ("parent", "child", "child"),
    ("guardian", "ward", "ward"),

    # 👶 Child → Parent (FIXED)
    ("son", "father", "mother"),
    ("daughter", "father", "mother"),
    ("child", "parent", "parent"),

    # 👴 Grand Relations
    ("grandfather", "grandson", "granddaughter"),
    ("grandmother", "grandson", "granddaughter"),
    ("grandson", "grandfather", "grandmother"),
    ("granddaughter", "grandfather", "grandmother"),

    # 👪 Siblings (FIXED LOGIC)
    ("brother", "brother", "sister"),
    ("sister", "brother", "sister"),
    ("sibling", "sibling", "sibling"),

    # 👨‍👩‍👧 Extended Family
    ("uncle", "nephew", "niece"),
    ("aunt", "nephew", "niece"),
    ("nephew", "uncle", "aunt"),
    ("niece", "uncle", "aunt"),

    # 👨‍👩‍👧 Cousins
    ("cousin", "cousin", "cousin"),

    # 💍 Marriage (IMPORTANT FIX)
    ("husband", "husband", "wife"),
    ("wife", "husband", "wife"),
    ("spouse", "spouse", "spouse"),

    # 💍 In-Laws (FIXED)
    ("father-in-law", "son-in-law", "daughter-in-law"),
    ("mother-in-law", "son-in-law", "daughter-in-law"),
    ("son-in-law", "father-in-law", "mother-in-law"),
    ("daughter-in-law", "father-in-law", "mother-in-law"),

    ("brother-in-law", "brother-in-law", "sister-in-law"),
    ("sister-in-law", "brother-in-law", "sister-in-law"),

    # 👶 Generational
    ("ancestor", "descendant", "descendant"),
    ("descendant", "ancestor", "ancestor"),
    ("elder", "younger", "younger"),
    ("younger", "elder", "elder"),

    # ❤️ Social
    ("mentor", "mentee", "mentee"),
    ("coach", "player", "player"),
    ("senior", "junior", "junior"),
    ("friend", "friend", "friend"),
    ("best friend", "best friend", "best friend"),

    # 🏫 Education
    ("teacher", "student", "student"),
    ("professor", "student", "student"),
    ("trainer", "trainee", "trainee"),
    ("classmate", "classmate", "classmate"),

    # 🏢 Work
    ("employer", "employee", "employee"),
    ("manager", "subordinate", "subordinate"),
    ("leader", "follower", "follower"),
    ("colleague", "colleague", "colleague"),
    ("boss", "employee", "employee"),

    # ⚖️ Professional
    ("doctor", "patient", "patient"),
    ("lawyer", "client", "client"),

    # 🏠 Ownership
    ("owner", "tenant", "tenant"),
    ("buyer", "seller", "seller"),
    ("lender", "borrower", "borrower"),

    # 🎤 Interaction
    ("host", "guest", "guest"),
    ("speaker", "audience", "audience"),

    # 🧠 Abstract
    ("creator", "creation", "creation"),
    ("author", "reader", "reader"),
]

# Insert into table
main_curr.executemany("""
INSERT OR IGNORE INTO all_relation (
    relation_name, 
    male_opposite, 
    female_opposite
) VALUES (?, ?, ?)
""", relations)

main_connect.commit()
show=main_curr.execute("select * from all_relation").fetchall()
print(show)
