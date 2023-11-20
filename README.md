# astrea

## Overview
Astrea is a custom static site generator meant to ease the experience of desgining of one's own [Digital Garden](https://maggieappleton.com/garden-history). Astrea allows users to write pages using the precision of `HTML` while also taking care of the headers and footers of the website file, keeping them consistent site-wide. When a new page is added, Astrea automatically handles its addition, logging it in every other page's navigation bar under its appropriate category by parsing a customizable pre-header.

## Philosophy
I am of the opinion that the best and most meaningful personal blogs are born out of simplicity. In this spirit, I desiged my this website manager which forces me to be creative given a set of simple and restrictive rules. I am exceedingly impressed by what I can do with html and css that I write by hand rather than what I can build using a paid website service. I encourage others to give this tool a try. Discover what you can make when you have full control over your website/blog/digital garden.

## How to use
Astrea requires Python >3.X

To run Astrea, do `python main.py` or `python3 main.py`. If successful, you should see something like `Processed 3 files in 9.619 miliseconds.`

Astrea works by first detecting the `.htm` files within the `inc/` folder, making a catalogue of them and their category. Each file's category is defined within the file itself between the `---` markers. Astrea detects all unique occurrences of a category and determines the membership of all files.  Astrea then parses the `.htm` files. The `.htm` format requires users to write, in `HTML`, all of the file contents within the `<main>` element. Astrea appends text requirements for the `HTML` format including the navigation bar which contains all file categories and links to the other site files. Finally, a `<footer>` is added to each file. The post-processsed files are saved in `site/`.

Mess around with this! Add your own files, change up the `home.html` landing page, fiddle with `links/main.css` to create your own styling. You'll probably want to change the places where my name is referenced directly or links to places that don't exist.

## Other
If you have any questions please let me know! If you have any optimizations/suggestions for the code, let me know too or make your own pull requests! I've cobbled this together in 1 hour spurts over 2 weeks, all while being fried after work so it's guarenteed that much of this code is less than optimal. Lastly, have fun! I'm excited to see what you come up with using Astrea. 

An unfinished version of Astrea lives in purgatory in my [PythonProjects](https://github.com/seanlabean/PythonProjects/tree/master/SiteGenerator) repository.

The `.css` used in this example is heavily inspired by the artists over at [100Rabbits](https://100r.co). 