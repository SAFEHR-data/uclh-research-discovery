---
layout: page
---

# Submitting a project for inclusion on this site
If you are a UCLH researcher, you can submit details about your own research project(s) and have them added to this site.

Whilst some experience of version control with git and GitHub would be beneficial, the guidance below tries to assume as little prior knowledge as possible and sticks to making changes via the GitHub user interface. Contributors with more experience may want to take a different approach.

**Step 1**: [Upload datasets and code to a research data repository](#step-1-upload-datasets-and-code-to-a-research-data-repository)

**Step 2**: [Clone our repository on GitHub](#step-2-clone-our-repository-on-github)

**Step 3**: [Complete the project template](#step-3-complete-the-project-template)

**Step 4**: [Generate the Jekyll front-matter](#step-4-generate-the-jekyll-front-matter)

**Step 5**: [Make a pull request](#step-5-make-a-pull-request)

## Step 1: Upload datasets and code to a research data repository

To help people who are interested in your research to better understand what data you have used and how you process it, it can be helpful to generate a synthetic dataset which you can share together with any relevant computer code in an open-access repository. We recommend using UCL's institutional [research data respository](https://rdr.ucl.ac.uk/) service as it is free for all UCL researchers to use and provides an embed link which can be used to include your data alongside details about your project on this site. Please read the guidance on the [UCL Library Researd Data Repository](https://www.ucl.ac.uk/library/open-science-research-support/research-data-management/ucl-research-data-repository) page for details on how to prepare and upload your data.

Once your submission has been approved, you can find the embed URL by navigating to your deposit's page and selecting 'Embed' from the menu. Copy the iframe tag and include this in one of the html or markdown files you create in Step 3.

## Step 2: Fork our repository on GitHub

To complete the next steps you will need a GitHub account, which will enable you to take a copy of the site's code and later merge your changes back in. If you don't have one you can [sign up for free](https://github.com/join).

The source code for this site can be found on GitHub: [{{site.data.github.url}}](https://{{site.data.github.url}}). To make a copy you can make changes to, you can fork the repository. You can do whatever you want with the forked copy once you've made it, and then create a pull request (see below) to have your changes merged back into the original code base.

To start, make sure you're logged into your account, and then find the fork button on this site's GitHub repository and click "Create a new fork":

![UCLH Research Discovery GitHub repository (fork)]({{'assets/images/fork_1.png' | relative_url}})

In the form that follows, select your username from the Owner dropdown menu, then click "Create fork". A copy of the repository should then appear under your own username with a note beneath the title saying "forked from {{site.data.github.url}}".

## Step 3: Complete the project template

Once you have forked the repository, you can start adding your project. The pages for each project are kept in separate folders under `/_projects`. Start by creating a new folder for your project containing an `index.md` file.

### index.md
Whilst you might be used to making a new folder before creating the files that go in it, GitHub doesn't actually let you create an empty folder, so you need to create both the folder and your first file at the same time. Every project folder must include a file called index.md, which serves as the landing page for your project, so that's probably the best place to start:

1. From the main page of the forked repository, select the `_projects` folder from the file explorer table. ![Select _projects]({{'assets/images/new_project_1.png' | relative_url}})
2. From within this folder, click *Add file > Create new file* ![Add file > Create new file]({{'assets/images/new_project_2.png' | relative_url}})
3. At the top of the page you'll see an empty box with the placeholder text "Name your file...". Enter the name of the new folder you'd like to create:<br>**The name of the folder will be used to generate the title for your project (see below for how to override this)**<br>![Enter a folder name]({{'assets/images/new_project_3.png' | relative_url}})<br> followed by a forward slash `/`, and then the name of the file `index.md`:<br>![Enter file name]({{'assets/images/new_project_4.png' | relative_url}})
4. You can now start writing a lay summary of your project written in [markdown](https://en.wikipedia.org/wiki/Markdown) format in the text box below. You can include as much detail as you like, but you also have the option to add additional pages if you'd like to split things up into separate sections (see *Extra content* below).
5. When you'd like to save your progress, click "Commit changes...". In the pop-up enter whatever short message you think is appropriate to describe the changes you've made, then click "Commit changes".
6. To edit an existing file, locate and click on it in the GitHub repository's file explorer, then select the pencil icon from the right of the toolbar:![Edit file icon]({{'assets/images/edit_file.png' | relative_url}})


If you're new to markdown:
* Whilst editing a mardown file you can switch between the *Preview* and *Edit* views to get a sense of how your markdown content is going to appear on the page.
* This [markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) to help you get started.


### authors.txt
Your project folder must also include a list of people to be credited as authors on the project in a separate file called `authors.txt` with each name on a separate line. These names will appear at the top of the page, and on the summary card shown on the website's home page.

Make sure you are in your newly created project folder before clicking *Add file > Create new file*.

![Example authors.txt]({{'assets/images/authors_txt.png' | relative_url}})

### title.txt
By default the title for your project will be derived from the folder name by replacing any dash or hyphen characters with spaces, and converting the result to title case.

If you'd like to override this, add a file called `title.txt` and write the title for your project on the first line.

### status.txt
Each project page displays the current status of the project on a label displayed next to the title. This can be one of two options: ongoing or completed, with the default being ongoing. To set the status of your project, include a file called `status.txt` containing one of these two options.

### Extra content
If you'd like to split content across several pages, or include an embed link for your data, you can add extra content by including additional markdown or html files in your project folder. This content will appear in separate tabs across the top of the page. 

The name of the file is used to generate the tab label for the extra content as follows:

* The filename suffix (.md/.html is removed)
* Any underscore(_) or hyphen (-) characters are replaced with spaces
* Digits at the start of the filename are removed
* Any whitespace remaining at the start or end of the name is removed
* The name is converted to title case

As an example, the tab label for `03_code-and_data.md` would be "Code And Data".

Tab order is alphabetical (except index.md which always appears first). To determine the order in which tabs appear, use numbers at the start of your filenames (e.g. `01_methods.md`, `02_privacy.md`, `03_data.html`).

### Assets
The site builder only picks up files with .html or .md suffixes as extra content to be included as tabs on the project page, anything else is ignored. However, you can use relative links to include other types of assets in your pages such as images, javascript, css etc. For example, you could create a folder inside your project folder called images, where you can upload all of the images you'd like to include in your pages. To upload a file, select "Upload files" from the "Add files" dropdown menu.

### Quarto
If you use Quarto to generate an html page, you will find it generates a whole folder of assets that need to be included. No problem, just include the Quarto assets folder in your project folder alongside the html file, and the relative links to those assets should still work.

## Step 4: Generate the Jekyll front-matter
When you've finished adding content, we need to add some metadata called front-matter to the top of your `index.md` file. The front-matter is read by the site generator and includes information about things like the project title, authors, and which extra pages to include. We have a utility script (`_utils/jekyllify.py`) which automatically generates this front-matter, which you can run through GitHub as follows:

1. Select "Actions" from the top navigation menu<br> ![Actions in the top nav menu]({{'assets/images/actions_1.png' | relative_url}})
2. If this is the first time you've run any actions in the fork, you'll see a warning message "Workflows aren't being run on this repository". Click the green button labelled "I understand my workflows, go ahead and enable them".
3. On the following page, in a side menu titled Actions, you'll see a list of available actions. Click the one named Jekyllify projects.<br> ![Actions list]({{'assets/images/actions_3.png' | relative_url}})
4. On this action's page, click "Run workflow" then "Run workflow" again to trigger it. After a few moments you should see a new entry appear in the table below with a yellow circle next to the workflow name.<br> ![Run workflow]({{'assets/images/actions_4.png' | relative_url}})
5. When the workflow has run successfully, you should see a green circle with a tick replace the yellow dot. You can check to confirm something like this appears at the top of `index.md`:
```
---
layout: project
title: My Project
authors:
- Alice Mill
- Bob Bentham
tabs:
- {
  name: vphbybwh,
  type: md,
  source: _analysis.md,
  label: Analysis
  }
- {
  name: kqfokysy,
  type: html,
  source: _data.html,
  label: Data
  }
---
```

If you update the project in future with a new title, authors, or extra content, you'll need to regenerate the front matter. To do this, edit `index.md` to remove the existing front-matter, then run the Jekyllify projects action again.

## Step 5: Make a pull request

To publish your project, you will need to merge your new files back into the original GitHub repository. To do this you will need to submit a [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests). The pull request process allows us to review submissions before they are added to ensure they comply with our standards.

To open a pull request:
1. Select Pull requests from the top navigation menu<br> ![Pull requests in the top nav menu]({{'assets/images/pull_request_1.png' | relative_url}})
2. Click the green 'New pull request' button
3. On the next page title "Comparing changes" you should see the base repository on the left (the original repository) with an arrow pointing to it from the head repository (your fork) on the right. Make sure the pull request is targeting the staging branch on the base repository (this should already be selected as the default option)<br> ![Original repository on the left, fork on the right]({{'assets/images/pull_request_2.png' | relative_url}})
4. Click 'Create pull request'
5. Add a title and description, including any details you think may be relevant for somebody reviewing your changes
6. Then click 'Create pull request'

Your pull request will then need to be approved by two reviewers who are chosen automatically from a pool of volunteer editors. Reviewers might sometimes make comments or request changes before approving your submission so please make sure you are able to receive notifications from GitHub in order to respond to their requests.

Once approved, your project will be merged into the main branch and it will automatically appear on the live website.