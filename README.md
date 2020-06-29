# Language lesson vocabulary manager with Django
This is a django project made up of 2 models:

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

## WHO IS IT FOR?
- The web app could be used as a language teaching app.
- It could also be used by teachers who wish to share vocabulary and a translation with students either before or after classes.

## SITE ADMIN
- The site admin can create, modify and delete lessons with a description and assign an order number. This allows the creation of featured lessons for the home page.
- The admin can then add vocabulary entries to the lesson along with a translation.

## USER
- The home page allows users to see 10 featured lessons (as assigned by the site admin via the 'order' field for lessons.)
- The user can click to see all lessons.
- Entry search - the user can also search all vocabulary entries by keyword.

## SKILLS COVERED
As well as general django project set up skills, the project makes use of:
- Generic views
- Foreign keys
- Django forms
- Namespacing urls
- Using admin.StackedInLine to add a model with a foreign key to the parent model in the admin pages.



