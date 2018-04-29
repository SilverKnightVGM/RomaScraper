**RomaScraper**
===============

This scraper written in Python 3 was intentended to scrape an article site and download for offline viewing in HTML format. This repository also includes scripts to convert them to .docx files. The main script (roma_scraper.py) can be easily modified to fetch specific content from any site.

There are differences depending which conversion method is used:
* **Powershell**: Slower to convert, sometimes it seems like it gets stuck, results in a smaller file size since all hrefs (links) to images stay as links in when converted to docx. This also preserves all the CSS formatting and colors so it is more accurate.
* **Pandoc**: You can use [Pandoc](https://pandoc.org/index.html) to convert HTML to DOCX. This method is faster at conversion, and embeds the images, resulting in bigger files but you don't need to be online to view them. However, this method removes any CSS and colors in the resulting files. Just include pandoc.exe in this same directory to use it.

*TODO Note*: Right now the the .py and .bat scripts used for downloading and conversion don't check for existing files, so it will replace any files you already have with the same name that are already downloaded or converted, there is no way to resume where you left off if stopped.
