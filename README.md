# Language lesson vocabulary manager with Django
This is a simple django project that allows a teacher to create online lessons or lessons for students to see.
There are two models:

## LESSON
### Fields:
- Lesson name
- Description
- Order

## ENTRY
### Fields
- Lesson (Foreign key)
- Entry_text
- Translation

A typical user could be a language teacher who creates entry text with a sentence, word or phrase, before adding a translation and assigning the entry to a lesson eg. entry could be 'oranges' assigned to the lesson 'fruit.'
