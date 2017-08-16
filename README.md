# Big Title

Cool things about sql.

## The story of Literator

Literator is a small town disconnected from everywhere and they lost all their books to a fire.
They decided to crowd source books so that they have something to read. They got together and
started writing books. They have written 30 books in the end and they all chipped in.
They also started reading the books as soon as the books have something in them regardless of
them finished or not. Some books may have never been finished.

`book` table contains the book names and their titles. `person` table contains the people, their
names and their dates of birth.

`read` and `write` tables are event log tables. They contain event data about the start and end
time of the read/write session, who was doing it and if they finished reading/writing the book in
 that session.

Each book was written by a number of people. Writing sessions did not overlap to prevent the
stories from getting confusing. They have finished writing most books but some may have been left
 unfinished.

They also read the books individually. They had e-books (they learned from the fire) so more than
 one person could read the books at the same time. Most of them finished their books but some of
 them did not finish some books.

## Sample queries

All persons in the town
Writer count per book in descending order of count
Oldest/youngest person and their DOB
Total number of write sessions
longest reading session length
longest writing session