# Guide for Developing Frontend
This guide will help you develop themes for the WBGym website. \
**Contents**:
- [What is used here?](#What-is-used-here?)
- [Testing](#Testing)

## What is used here?
This website uses plain HTML with Jinja (a templating engine from Python Django). In addition we integrated TailwindCSS for styling, because it looks much better and is easier to code. There is no JS-Framework used, because it would be overkill this project. And we don't need that many interactive elements.

## Testing
To test the website, you need to rebuild the CSS with the following command:

```bash
python manage.py tailwind build
```

After that you can run the server with:

```bash
python manage.py runserver
```
