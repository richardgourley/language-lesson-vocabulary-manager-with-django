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
- This web app could be used as the basis for a language learning app.
- It could also be used by language teachers to share vocabulary and translations with students.

## SITE ADMIN
- The site admin can create, modify and delete lessons with a description and assign an order number. The featured lessons page shows lessons ordered by lowest order number.
- The admin can add vocabulary entries with a translation, to each lesson.

## SITE PAGES
- Featured lessons - shows 10 featured lessons (as assigned by the site admin via the 'order' field for lessons.)
- All lessons
- Entry search - the user can also search all vocabulary entries by keyword.

## TESTING
- All site pages working
- Lessons without vocabulary show 404 for lessons/id
- Featured lessons doesn't show empty lessons (no vocabulary entries)
- All lessons shows a message if no lessons have been created
- Client content contains expected results (messages)
- Client context contains expected query set results

## SKILLS COVERED
As well as general django project set up skills, the project makes use of:
- Generic views
- Foreign keys
- Django forms
- Dango query set searches - filter, annotate, Count, all
- Namespacing urls
- Using admin.StackedInLine to add a model with a foreign key to the parent model in the admin pages.
- Django TestCase - app testing modules, Client, setup_test_environment



