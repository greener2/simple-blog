# simple-blog
A simple blog built in Django to chronicle my adventures in learning fullstack development.

## Movitation
I wanted to learn how to make a simple blogging platform in Django, as a lot of Python backend is written in Django. 
I also wanted to challenge myself to learn how to style a not-incredibly-ugly website (I'm very willing to admit my 
frontend skills need a *LOT* of work!) and to create something that I would actually use.

## Structure
It's a regular Django app called `blog`, with the project name being `blogsite`. It is accessible from the URL 
`http://127.0.0.1:8000/blog` with the admin page being at `http://127.0.0.1:8000/admin`.

## Features
The blog has the following very simple features.

- Tags for tagging posts, and searching for posts that have particular tags.
- Search function to search for a term in the title, subtitle or body of each post.
- Correct HTML rendering for the post body (HTML is stored and is rendered correctly in the browser.)

Planned for the future:

- Automated testing
- A nicer admin/CMS setup for inputting blog posts
- A comment section (although that might involve an over-estimation of how many people are going to read it!) 

## License
MIT Licensed, so you should be able to do whatever you want with it, if you choose.

## Contact
Author is Rob Greene (greener2-at-gmail.com) if you have any questions or suggestions. 