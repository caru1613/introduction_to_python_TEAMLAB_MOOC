from NoteBook import NoteBook
from NoteBook import Note

quote_book = NoteBook("The Quote Book")

new_note = Note()
new_note.write_content("abcdefg")
quote_book.add_note(new_note)

print(quote_book.get_number_of_pages())

quote_book.add_note(Note("Hello, World"))
quote_book.add_note(Note("Hello, World"))
quote_book.add_note(Note("Hello, World"))
quote_book.add_note(Note("Hello, World"))
quote_book.add_note(Note("Hello, World"))

print(quote_book.get_number_of_pages())

my_note = quote_book.remove_note(1)
print(my_note)
my_note = quote_book.remove_note(2)
print(my_note)
my_note = quote_book.remove_note(1)
print(my_note)