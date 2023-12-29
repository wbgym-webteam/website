# Guide for Frontend Development

This guide will help you develop themes for the WBGym website. \
**Contents**:

- [Getting Started](#getting-started)
- [Troubleshooting](#troubleshooting)
- [Useful Links](#useful-links)

## Getting Started

When you first clone the repository, you will need to install the dependencies. These are:

- [Node.js](https://nodejs.org/en/)
- Python 3.8 or higher
- Python packages: `pip install -r requirements.txt`

Once you have installed these, you can run the following command to install the Node.js dependencies:

```bash
python manage.py tailwind start
```

This will install the dependencies and if you run the command again, it will make a **development** build of the theme.

To make a **production** build, run the following command:

```bash
python manage.py tailwind build
```

Afterwards you can run the server with the following command:

```bash
python manage.py runserver
```

## Troubleshooting

Oftentimes when you try to run the command `python manage.py tailwind start`, you will get an error which says, that you haven't installed npm (NodePackageManager).To fix this issue, follow the steps below:

1. **Check your environment variables.** To do this, press the Windows key and search for "environment variables". Click on the button that says "Environment Variables" and then click on "Path" in the "System variables" section. Click on "Edit" and then click on "New". Paste the following path into the text box: `C:\Users\YOUR_USERNAME\AppData\Roaming\npm.cmd`. Replace `YOUR_USERNAME` with your username. Click on "OK" and then click on "OK" again. Now you should be able to run the command `python manage.py tailwind start` without any issues.

2. **If the above step didn't work, try the following:**
Restart your computer. Then run the command `python manage.py tailwind start` again. If it still doesn't work, continue to the next step.

3. **Check the `NPM_BIN_PATH` variable** in the `wbgym/settings.py`-File. If it is the same path as the actual path to the npm.cmd on your computer (test it by inserting the path into the file explorer) and it's still not working, open an issue on Github. Do it the following way:

- Title: "NPM_BIN_PATH is wrong"
- Labels: bug, help wanted, Django, duplicate (if there is already an issue about this)
- Description: write, which steps you've already tried to fix the issue and what the output of the command `python manage.py tailwind start` is. Also write, what you've done beyond the steps in this guide.

## Useful Links

- [Setup and run Tailwind with Python Django](https://django-tailwind.readthedocs.io/en/latest/installation.html)
- [Tailwind CSS](https://tailwindcss.com/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Tailwind CSS Cheat Sheet](https://nerdcave.com/tailwind-cheat-sheet)
- [Tailwind CSS Color Palette](https://tailwindcss.com/docs/customizing-colors#color-palette-reference)
- [Tailwind CSS Color Palette Generator](https://javisperez.github.io/tailwindcolorshades/)
