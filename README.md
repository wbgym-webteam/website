# WBGym-Website
The new website of the WBGym in Kleinmachnow

For the German version of this file, see [here](README_GER.md).

## Information for Contributors

### File Structure

The entire server is located in the folder `wbgym/`.
It contains the so-called apps, which represent different areas of the website:
* The app named `wbgym` is the core of the server and contains general settings for the entire server. It is automatically created by Django.
* The app named `content` is intended for the actual content of the website, i.e. what the users of the website see in the end. The naming is not mandatory and can be changed if a better name is found.
* In addition, further apps can be added, which are responsible for the administration of the users (ams) or for the administration of the database (cms), for example.

There is an app for the templates, called `themes`.
* The folder `templates` contains all HTML files that are delivered by the website. These files are used by Django as a template, which is then filled with content before it is sent to the user. **Important:** TailwindCSS is used in there for styling. The HTML files are therefore not pure HTML files, but contain additional class names brought by TailwindCSS. See [here](https://tailwindcss.com/docs) for more information.
