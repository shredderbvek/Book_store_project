category_choice = (
    ('fiction', 'Fiction'),
    ('poetry', 'Poetry'),
    ('academics', 'Academics'),
    ('politics', 'Politics'),
    ('history', 'History'),
    ('comics', 'Comics'),
    ('non-fiction', 'Non-fiction'),
)
genre = {}
for item in category_choice:
    genre[item[0]] = item[1]