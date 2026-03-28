---
icon: octicons/markdown-16
---

![Markdown Logo](images/markdown-mark.svg#only-light){ .center-image }
![Markdown Logo](images/markdown-mark-white.svg#only-dark){ .center-image }

<H1 style="text-align: center;"> Awesome Markdown</H1>

### Getting Started

An overview of Markdown, how it works, and what you can do with it.

### What is Markdown?

<p>Markdown is a lightweight markup language that you can use to add formatting elements to plaintext text documents. Created by <a href="https://daringfireball.net/projects/markdown/">John Gruber</a> in 2004, Markdown is now one of the world’s most popular markup languages.</p>

<p>Using Markdown is different than using a <a href="https://en.wikipedia.org/wiki/WYSIWYG">WYSIWYG</a> editor. In an application like Microsoft Word, you click buttons to format words and phrases, and the changes are visible immediately. Markdown isn’t like that. When you create a Markdown-formatted file, you add Markdown syntax to the text to indicate which words and phrases should look different.</p>

<p>For example, to denote a heading, you add a number sign before it (e.g., <code class="language-plaintext highlighter-rouge"># Heading One</code>). Or to make a phrase bold, you add two asterisks before and after it (e.g., <code class="language-plaintext highlighter-rouge">**this text is bold**</code>). It may take a while to get used to seeing Markdown syntax in your text, especially if you’re accustomed to WYSIWYG applications. The screenshot below shows a Markdown file displayed in the <a href="https://www.markdownguide.org/tools/vscode/">Visual Studio Code text editor</a>.</p>

<p><img srcset="https://mdg.imgix.net/assets/images/vscode.png?auto=format&amp;fit=clip&amp;w=480 480w,              https://mdg.imgix.net/assets/images/vscode.png?auto=format&amp;fit=clip&amp;q=40&amp;w=1080 1080w" src="https://mdg.imgix.net/assets/images/vscode.png" class="img-fluid" alt="Markdown file in the Visual Studio Code text editor" sizes="100vw" /></p>

<p>You can add Markdown formatting elements to a plaintext file using a text editor application. Or you can use one of the many Markdown applications for macOS, Windows, Linux, iOS, and Android operating systems. There are also several web-based applications specifically designed for writing in Markdown.</p>

<p>Depending on the application you use, you may not be able to preview the formatted document in real time. But that’s okay. <a href="https://daringfireball.net/projects/markdown/">According to Gruber</a>, Markdown syntax is designed to be readable and unobtrusive, so the text in Markdown files can be read even if it isn’t rendered.</p>

<blockquote>
  <p>The overriding design goal for Markdown’s formatting syntax is to make it as readable as possible. The idea is that a Markdown-formatted document should be publishable as-is, as plain text, without looking like it’s been marked up with tags or formatting instructions.</p>
</blockquote>

<h2 id="why-use-markdown">Why Use Markdown?</h2>

<p>You might be wondering why people use Markdown instead of a WYSIWYG editor. Why write with Markdown when you can press buttons in an interface to format your text? As it turns out, there are several reasons why people use Markdown instead of WYSIWYG editors.</p>

<ul>
  <li>
    <p>Markdown can be used for everything. People use it to create <a href="https://www.markdownguide.org/getting-started/#websites">websites</a>, <a href="https://www.markdownguide.org/getting-started/#documents">documents</a>, <a href="#notes">notes</a>, <a href="#books">books</a>, <a href="#presentations">presentations</a>, <a href="#email">email messages</a>, and <a href="#documentation">technical documentation</a>.</p>
  </li>
  <li>
    <p>Markdown is portable. Files containing Markdown-formatted text can be opened using virtually any application. If you decide you don’t like the Markdown application you’re currently using, you can import your Markdown files into another Markdown application. That’s in stark contrast to word processing applications like Microsoft Word that lock your content into a proprietary file format.</p>
  </li>
  <li>
    <p>Markdown is platform independent. You can create Markdown-formatted text on any device running any operating system.</p>
  </li>
  <li>
    <p>Markdown is future proof. Even if the application you’re using stops working at some point in the future, you’ll still be able to read your Markdown-formatted text using a text editing application. This is an important consideration when it comes to books, university theses, and other milestone documents that need to be preserved indefinitely.</p>
  </li>
  <li>
    <p>Markdown is everywhere. Websites like <a href="https://www.reddit.com/">Reddit</a> and GitHub support Markdown, and lots of desktop and web-based applications support it.</p>
  </li>
</ul>

<h2 id="kicking-the-tires">Kicking the Tires</h2>

<p>The best way to get started with Markdown is to use it. That’s easier than ever before thanks to a variety of free tools.</p>

<p>You don’t even need to download anything. There are several online Markdown editors that you can use to try writing in Markdown. <a href="https://dillinger.io/">Dillinger</a> is one of the best online Markdown editors. Just open the site and start typing in the left pane. A preview of the rendered document appears in the right pane.</p>

<p><img srcset="https://mdg.imgix.net/assets/images/dillinger.png?auto=format&amp;fit=clip&amp;w=480 480w,              https://mdg.imgix.net/assets/images/dillinger.png?auto=format&amp;fit=clip&amp;q=40&amp;w=1080 1080w" src="https://mdg.imgix.net/assets/images/dillinger.png" class="img-fluid" alt="Dillinger Markdown editor" loading="lazy" sizes="100vw" /></p>

<p>You’ll probably want to keep the Dillinger website open as you read through this guide. That way you can try the syntax as you learn about it. After you’ve become familiar with Markdown, you may want to use a Markdown application that can be installed on your desktop computer or mobile device.</p>

<h2 id="how-does-it-work">How Does it Work?</h2>

<p>Dillinger makes writing in Markdown easy because it hides the stuff happening behind the scenes, but it’s worth exploring how the process works in general.</p>

<p>When you write in Markdown, the text is stored in a plaintext file that has an <code class="language-plaintext highlighter-rouge">.md</code> or <code class="language-plaintext highlighter-rouge">.markdown</code> extension. But then what? How is your Markdown-formatted file converted into HTML or a print-ready document?</p>

<p>The short answer is that you need a <em>Markdown application</em> capable of processing the Markdown file. There are lots of applications available — everything from simple scripts to desktop applications that look like Microsoft Word. Despite their visual differences, all of the applications do the same thing. Like Dillinger, they all convert Markdown-formatted text to HTML so it can be displayed in web browsers.</p>

<p>Markdown applications use something called a <em>Markdown processor</em> (also commonly referred to as a “parser” or an “implementation”) to take the Markdown-formatted text and output it to HTML format. At that point, your document can be viewed in a web browser or combined with a style sheet and printed. You can see a visual representation of this process below.</p>

<div class="alert alert-info">
  <i class="fas fa-info-circle"></i> <strong>Note:</strong> The Markdown application and processor are two separate components. For the sake of brevity, I've combined them into one element ("Markdown app") in the figure below.
</div>

<p><img srcset="https://mdg.imgix.net/assets/images/markdown-flowchart.png?auto=format&amp;fit=clip&amp;w=480 480w,              https://mdg.imgix.net/assets/images/markdown-flowchart.png?auto=format&amp;fit=clip&amp;q=40&amp;w=1080 1080w" src="https://mdg.imgix.net/assets/images/markdown-flowchart.png" class="img-fluid" alt="The Markdown Process" loading="lazy" sizes="100vw" /></p>

<p>To summarize, this is a four-part process:</p>

<ol>
  <li>Create a Markdown file using a text editor or a dedicated Markdown application. The file should have an <code class="language-plaintext highlighter-rouge">.md</code> or <code class="language-plaintext highlighter-rouge">.markdown</code> extension.</li>
  <li>Open the Markdown file in a Markdown application.</li>
  <li>Use the Markdown application to convert the Markdown file to an HTML document.</li>
  <li>View the HTML file in a web browser or use the Markdown application to convert it to another file format, like PDF.</li>
</ol>

<p>From your perspective, the process will vary somewhat depending on the application you use. For example, Dillinger essentially combines steps 1-3 into a single, seamless interface — all you have to do is type in the left pane and the rendered output magically appears in the right pane. But if you use other tools, like a text editor with a static website generator, you’ll find that the process is much more visible.</p>

<h2 id="whats-markdown-good-for">What’s Markdown Good For?</h2>

<p>Markdown is a fast and easy way to take notes, create content for a website, and produce print-ready documents.</p>

<p>It doesn’t take long to learn the Markdown syntax, and once you know how to use it, you can write using Markdown just about everywhere. Most people use Markdown to create content for the web, but Markdown is good for formatting everything from email messages to grocery lists.</p>

<p>Here are some examples of what you can do with Markdown.</p>

<h3 id="websites">Websites</h3>

<p>Markdown was designed for the web, so it should come as no surprise that there are plenty of applications specifically designed for creating website content.</p>

<p>If you’re looking for the simplest possible way to create a website with Markdown files, check out <a href="https://blot.im">blot.im</a>. After you sign up for Blot, it creates a Dropbox folder on your computer. Just drag and drop your Markdown files into the folder and — poof! — they’re on your website. It couldn’t be easier.</p>

<p>If you’re familiar with HTML, CSS, and version control, check out <a href="/tools/jekyll/">Jekyll</a>, a popular static site generator that takes Markdown files and builds an HTML website. One advantage to this approach is that <a href="/tools/github-pages/">GitHub Pages</a> provides free hosting for Jekyll-generated websites. If Jekyll isn’t your cup of tea, just pick one of the <a href="https://jamstack.org/generators/">many other static site generators available</a>.</p>

<div class="alert alert-info">
  <i class="fas fa-info-circle"></i> <strong>Note:</strong> Shameless plug! If you want to learn how to build static websites from scratch, check out <a href="https://www.staticguide.org/"><em>The Static Site Guide</em></a>, another book I wrote.
</div>

<p>If you’d like to use a content management system (CMS) to power your website, take a look at <a href="/tools/ghost/">Ghost</a>. It’s a free and open-source blogging platform with a nice Markdown editor. If you’re a WordPress user, you’ll be happy to know there’s <a href="https://wordpress.com/support/wordpress-editor/blocks/markdown-block/">Markdown support</a> for websites hosted on WordPress.com. Self-hosted WordPress sites can use the <a href="https://jetpack.com/support/jetpack-blocks/markdown/">Jetpack plugin</a>.</p>

<h3 id="documents">Documents</h3>

<p>Markdown doesn’t have all the bells and whistles of word processors like Microsoft Word, but it’s good enough for creating basic documents like assignments and letters. You can use a Markdown document authoring application to create and export Markdown-formatted documents to PDF or HTML file format. The PDF part is key, because once you have a PDF document, you can do anything with it — print it, email it, or upload it to a website.</p>

<p>Here are some Markdown document authoring applications I recommend:</p>

<ul>
  <li><strong>Mac:</strong> <a href="https://www.markdownguide.org/tools/macdown/">MacDown</a>, <a href="https://www.markdownguide.org/tools/ia-writer/">iA Writer</a>, or <a href="https://www.markdownguide.org/tools/marked-2/">Marked 2</a></li>
  <li><strong>iOS / Android:</strong> <a href="https://www.markdownguide.org/tools/ia-writer/">iA Writer</a></li>
  <li><strong>Windows:</strong> <a href="https://kde.github.io/ghostwriter/">ghostwriter</a> or <a href="https://markdownmonster.west-wind.com/">Markdown Monster</a></li>
  <li><strong>Linux:</strong> <a href="https://github.com/retext-project/retext">ReText</a> or <a href="https://kde.github.io/ghostwriter/">ghostwriter</a></li>
  <li><strong>Web:</strong> <a href="https://www.markdownguide.org/tools/dillinger/">Dillinger</a> or <a href="https://www.markdownguide.org/tools/stackedit/">StackEdit</a></li>
</ul>

<div class="alert alert-success">
  <i class="fas fa-lightbulb"></i> <strong>Tip:</strong> <a href="https://ia.net/writer/templates/">iA Writer</a> provides templates for previewing, printing, and exporting Markdown-formatted documents. For example, the "Academic – MLA Style" template indents paragraphs and adds double sentence spacing.
</div>

<h3 id="notes">Notes</h3>

<p>In nearly every way, Markdown is the ideal syntax for taking notes. Sadly, <a href="https://evernote.com/">Evernote</a> and <a href="https://www.onenote.com/">OneNote</a>, two of the most popular note applications, don’t currently support Markdown. The good news is that several other note applications <em>do</em> support Markdown:</p>

<ul>
  <li><a href="https://www.markdownguide.org/tools/obsidian/">Obsidian</a> is a popular Markdown note-taking application loaded with features.</li>
  <li><a href="https://www.markdownguide.org/tools/simplenote/">Simplenote</a> is a free, barebones note-taking application available for every platform.</li>
  <li><a href="https://www.markdownguide.org/tools/notable/">Notable</a> is a note-taking application that runs on a variety of platforms.</li>
  <li><a href="https://www.markdownguide.org/tools/bear/">Bear</a> is an Evernote-like application available for Mac and iOS devices. It doesn’t exclusively use Markdown by default, but you can enable Markdown compatibility mode.</li>
  <li><a href="https://www.markdownguide.org/tools/joplin/">Joplin</a> is a note taking application that respects your privacy. It’s available for every platform.</li>
  <li><a href="https://www.markdownguide.org/tools/boostnote/">Boostnote</a> bills itself as an “open source note-taking app designed for programmers.”</li>
</ul>

<p>If you can’t part with Evernote, check out <a href="https://marxi.co/">Marxico</a>, a subscription-based Markdown editor for Evernote, or use <a href="https://www.markdownguide.org/tools/markdown-here/">Markdown Here</a> with the Evernote website.</p>

<h3 id="books">Books</h3>

<p>Looking to self-publish a novel? Try <a href="https://leanpub.com/">Leanpub</a>, a service that takes your Markdown-formatted files and turns them into an electronic book. Leanpub outputs your book in PDF, EPUB, and MOBI file format. If you’d like to create paperback copies of your book, you can upload the PDF file to another service such as <a href="https://kdp.amazon.com">Kindle Direct Publishing</a>. To learn more about writing and self-publishing a book using Markdown, read <a href="https://medium.com/techspiration-ideas-making-it-happen/how-i-wrote-and-published-my-novel-using-only-open-source-tools-5cdfbd7c00ca">this blog post</a>.</p>

<h3 id="presentations">Presentations</h3>

<p>Believe it or not, you can generate presentations from Markdown-formatted files. Creating presentations in Markdown takes a little getting used to, but once you get the hang of it, it’s a lot faster and easier than using an application like PowerPoint or Keynote. <a href="https://remarkjs.com">Remark</a> (<a href="https://github.com/gnab/remark">GitHub project</a>) is a popular browser-based Markdown slideshow tool, as are <a href="https://jdan.github.io/cleaver/">Cleaver</a> (<a href="https://github.com/jdan/cleaver">GitHub project</a>) and <a href="https://marp.app/">Marp</a> (<a href="https://github.com/marp-team/marp">GitHub project</a>). If you use a Mac and would prefer to use an application, check out <a href="https://www.decksetapp.com/">Deckset</a> or <a href="https://hyperdeck.io/">Hyperdeck</a>.</p>

<h3 id="email">Email</h3>

<p>If you send a lot of email and you’re tired of the formatting controls available on most email provider websites, you’ll be happy to learn there’s an easy way to write email messages using Markdown. <a href="https://www.markdownguide.org/tools/markdown-here/">Markdown Here</a> is a free and open-source browser extension that converts Markdown-formatted text into HTML that’s ready to send.</p>

<h3 id="collaboration">Collaboration</h3>

<p>Collaboration and team messaging applications are a popular way of communicating with coworkers and friends at work and home. These applications don’t utilize all of Markdown’s features, but the features they do provide are fairly useful. For example, the ability to bold and italicize text without using the WYSIWYG interface is pretty handy. <a href="https://www.markdownguide.org/tools/slack/">Slack</a>, <a href="https://www.markdownguide.org/tools/discord/">Discord</a>, <a href="https://www.markdownguide.org/tools/wiki-js/">Wiki.js</a>, and <a href="https://www.markdownguide.org/tools/mattermost/">Mattermost</a> are all good collaboration applications.</p>

<h3 id="documentation">Documentation</h3>

<p>Markdown is a natural fit for technical documentation. Companies like GitHub are increasingly switching to Markdown for their documentation — check out their <a href="https://github.com/blog/1939-how-github-uses-github-to-document-github">blog post</a> about how they migrated their Markdown-formatted documentation to <a href="https://jekyllrb.com/">Jekyll</a>. If you write documentation for a product or service, take a look at these handy tools:</p>

<ul>
  <li><a href="https://readthedocs.org">Read the Docs</a> can generate a documentation website from your open source Markdown files. Just connect your GitHub repository to their service and push — Read the Docs does the rest. They also have a <a href="https://readthedocs.com/">service for commercial entities</a>.</li>
  <li><a href="https://www.mkdocs.org/">MkDocs</a> is a fast and simple static site generator that’s geared towards building project documentation. Documentation source files are written in Markdown and configured with a single YAML configuration file. MkDocs has several <a href="https://www.mkdocs.org/user-guide/styling-your-docs/">built in themes</a>, including a port of the <a href="https://readthedocs.org/">Read the Docs</a> documentation theme for use with MkDocs. One of the newest themes is <a href="https://squidfunk.github.io/mkdocs-material/">MkDocs Material</a>.</li>
  <li><a href="https://docusaurus.io/">Docusaurus</a> is a static site generator designed exclusively for creating documentation websites. It supports translations, search, and versioning.</li>
  <li><a href="https://vuepress.vuejs.org/">VuePress</a> is a static site generator powered by <a href="https://vuejs.org/">Vue</a> and optimized for writing technical documentation.</li>
  <li><a href="https://jekyllrb.com/">Jekyll</a> was mentioned earlier in the section on websites, but it’s also a good option for generating a documentation website from Markdown files. If you go this route, be sure to check out the <a href="https://idratherbewriting.com/documentation-theme-jekyll/">Jekyll documentation theme</a>.</li>
</ul>

<h2 id="flavors-of-markdown">Flavors of Markdown</h2>

<p>One of the most confusing aspects of using Markdown is that practically every Markdown application implements a slightly different version of Markdown. These variants of Markdown are commonly referred to as <em>flavors</em>. It’s your job to master whatever flavor of Markdown your application has implemented.</p>

<p>To wrap your head around the concept of Markdown flavors, it might help to think of them as language dialects. People in New York City speak English just like the people in London, but there are substantial differences between the dialects used in both cities. The same is true for people using different Markdown applications. Using <a href="https://dillinger.io/">Dillinger</a> to write with Markdown is a vastly different experience than using <a href="https://ulysses.app/">Ulysses</a>.</p>

<p>Practically speaking, this means you never know exactly what a company means when they say they support “Markdown.” Are they talking about only the <a href="https://www.markdownguide.org/basic-syntax/">basic syntax elements</a>, or all of the basic and <a href="https://www.markdownguide.org/extended-syntax/">extended syntax elements</a> combined, or some arbitrary combination of syntax elements? You won’t know until you read the documentation or start using the application.</p>

<p>If you’re just starting out, the best advice I can give you is to pick a Markdown application with good Markdown support. That’ll go a long way towards maintaining the portability of your Markdown files. You might want to store and use your Markdown files in other applications, and to do that you need to start with an application that provides good support. You can use the <a href="https://www.markdownguide.org/tools/">tool directory</a> to find an application that fits the bill.</p>

<h2 id="additional-resources">Additional Resources</h2>

<p>There are lots of resources you can use to learn Markdown. Here are some other introductory resources:</p>

<ul>
  <li><a href="https://daringfireball.net/projects/markdown/">John Gruber’s Markdown documentation</a>. The original guide written by the creator of Markdown.</li>
  <li><a href="https://www.markdowntutorial.com/">Markdown Tutorial</a>. An open source website that allows you to try Markdown in your web browser.</li>
  <li><a href="https://github.com/mundimark/awesome-markdown">Awesome Markdown</a>. A list of Markdown tools and learning resources.</li>
  <li><a href="https://dave.autonoma.ca/blog/2019/05/22/typesetting-markdown-part-1">Typesetting Markdown</a>. A multi-part series that describes an ecosystem for typesetting Markdown documents using <a href="https://pandoc.org/">pandoc</a> and <a href="https://www.contextgarden.net/">ConTeXt</a>.</li>
</ul>
 
 Awesome Series @ Write Kit

[Markdown (Syntax & Extensions, Documentation & Cheat Sheets, Libraries, ...)](https://github.com/writekit/awesome-markdown) • 
[Markdown Editors & (Pre)viewers](https://github.com/writekit/awesome-markdown-editors)  •
[Books (Services, Hand-Written, Auto-Built w/ Open Data, ...)](https://github.com/writekit/awesome-books)


# Awesome Markdown

A collection of awesome markdown goodies (libraries, services, editors, tools, cheatsheets, etc.)

Note: :octocat: stands for the GitHub page and :gem: stands for the RubyGems page.

---

[ANNOUNCEMENT] Looking for the latest news, tools, tips & tricks, and more
about markdown and friends?
Follow along the Manuscripts News ([@manuscriptsnews](https://twitter.com/manuscriptsnews)) channel on twitter for updates.

---


#### _Contributions welcome. Anything missing? Send in a pull request. Thanks._


## Table of Contents

<!--

Generated with [markedpp](#markedpp). Get [nodejs](https://nodejs.org) first

1. $ npm i -g markedpp
2. $ markedpp --github -o README.md README.md

-->

<!-- !toc (minlevel=2 omit="Table of Contents") -->

* [Markdown](#markdown)
* [Markdown Syntax Extensions](#markdown-syntax-extensions)
  * [MultiMarkdown (MMD)](#multimarkdown-mmd)
  * [Markdown Extra](#markdown-extra)
  * [Markdown Extended (MDE)](#markdown-extended-mde)
* [Manuscripts](#manuscripts)
* [CommonMark](#commonmark)
* [GitHub Flavored Markdown (GFM)](#github-flavored-markdown-gfm)
* [Vanilla Flavored Markdown (VFMD)](#vanilla-flavored-markdown-vfmd)
* [Markdown Documentation](#markdown-documentation)
  * [Markdown Cheatsheets / Quick References]
  * [Markdown Getting Started Guides / Tutorials]
* [Markdown Building Blocks](#markdown-building-blocks)
  * [Markdown Libraries & Tools]
  * [Babelmark](#babelmark)
  * [Markdown Style Guides / Best Practices]
  * [Markdown Lint / Style Rule Checker]
  * [Markdown Web Components / Custom Elements]
  * [Markdown to Website / Blog]
  * [Markdown to Email](#markdown-to-email)
  * [Markdown to Presentation / Slideshow]
  * [Markdown to Portable Document Format (PDF)](#markdown-to-portable-document-format-pdf)
  * [Markdown Styles / Documents / Pages]
  * [Markdown to Books](#markdown-to-books)
  * [Markdown to Table of Contents (TOC)](#markdown-to-table-of-contents-toc)
  * [Markdown to Markdown Pre-Processor](#markdown-to-markdown-pre-processor)
* [Convert to Markdown Tools](#convert-to-markdown-tools)
  * [Microsoft Word to Markdown](#microsoft-word-to-markdown)
  * [Hypertext Markup Language (HTML) to Markdown](#hypertext-markup-language-html-to-markdown)
  * [Source Code to Markdown](#source-code-to-markdown)
  * [Technical Documentation to Markdown](#technical-documentation-to-markdown)
  * [Screencast to Markdown](#screencast-to-markdown)
  * [JSON to Markdown](#json-to-markdown)
* [Book Services](#book-services)
* [Articles](#articles)
* [Meta](#meta)

<!-- toc! -->

## Markdown

_email-style writing for the web by John Gruber and Aaron Swartz_ 

- **Markdown** (web: [daringfireball.net/projects/markdown](http://daringfireball.net/projects/markdown)) - original Markdown syntax write-up and processor in Perl by John Gruber; no longer maintained (last update in December 2004)

History / Genesis

- [Introducing Markdown](http://daringfireball.net/2004/03/introducing_markdown) by John Gruber - March 15, 2004

  >   I've written a text-to-HTML formatting tool called Markdown, which is now available for download.
  > Markdown allows web writers to compose text using a simple, readable, plain text formatting syntax;
  > Markdown takes care of translating it to valid XHTML (or, if you prefer, HTML).

- [Dive into Markdown](http://daringfireball.net/2004/03/dive_into_markdown) by John Gruber - March 19, 2004

  >  You don't need to "preview" an email before you send it -- you write it, you read it, you edit it, right there.
  >
  >  In fact, I love writing email. Email is my favorite writing medium. I've sent over 16,000 emails in the last five years. 
  > The conventions of plain text email allow me to express myself clearly and precisely, without ever getting in my way.
  >
  > Thus, Markdown. Email-style writing for the web.

- [Markdown](http://www.aaronsw.com/weblog/001189) by Aaron Swartz - March 22, 2004

  >    For months I've been working with John Gruber on a new project. The idea was to make writing simple web pages,
  > and especially weblog entries, as easy as writing an email, by allowing you to use much the same syntax and converting it 
  > automatically into HTML.
  >
  >   Together we pored over the syntax details from top to bottom, trying to develop the perfect format, 
  > and I think we've got something pretty darn great. We've tested it extensively: on our blogs, in my comments form, in our emails.


<!--
- [**Talk**](https://pairlist6.pair.net/mailman/listinfo/markdown-discuss) - markdown-discuss mailing list
    no longer in use
  -->

Documentation

- [**Markdown @ Wikipedia**](http://en.wikipedia.org/wiki/Markdown)


## Markdown Syntax Extensions

<img src="https://daringfireball.net/graphics/smartypants_title.gif" alt="SmartyPants -- Smart quotes plug-in for Movable Type" width="384" height="96">

- [SmartyPants](http://daringfireball.net/projects/smartypants) -  convert (c) into ?, "" into ?, etc. 
- [Emojis](http://www.emoji-cheat-sheet.com) - [:octocat:](https://github.com/arvida/emoji-cheat-sheet.com)
- [CriticMarkup](http://criticmarkup.com) - [:octocat:](https://github.com/CriticMarkup)
- [GitHub Flavored Markup (GFM)](https://help.github.com/articles/github-flavored-markdown) - @mention, to do lists w/ [ ] and [x], etc.

### MultiMarkdown (MMD)

- [MultiMarkdown (MMD)](http://fletcherpenney.net/multimarkdown) - Markdown extensions by Fletcher Penney adding footnotes, tables, definition lists, document metadata (e.g. title, author, date, etc.) and more; first added to MultiMarkdown.pl
    - [Cheatsheet](https://rawgit.com/fletcher/human-markdown-reference/master/index.html)  - syntax quick reference
    - [Test Suite :octocat:](https://github.com/fletcher/MMD-Test-Suite)
- [MultiMarkdown.pl :octocat:](https://github.com/fletcher/MultiMarkdown) - historic MultiMarkdown.pl code; converter script in Perl (last update in Jan 2011)

### Markdown Extra

- [Markdown Extra](https://michelf.ca/projects/php-markdown/extra/) - Markdown extensions by Michel Fortin; first added to PHP Markdown (Extra)
- [Dingus](https://michelf.ca/projects/php-markdown/dingus/)  - try Markdown Extra in your browser

### Markdown Extended (MDE)

- [Markdown Extended (MDE) @ aboutmde.org](http://aboutmde.org)
    - [Spec](http://manifest.aboutmde.org)
    - [Cheatsheet](http://cheatsheet.aboutmde.org/) - syntax quick reference; examples side-by-side
    - [Dingus](http://dingus.aboutmde.org) - try Markdown Extended in your browser
- [Code :octocat:](https://github.com/piwi/markdown-extended) - converter script in PHP


## Manuscripts

_Free book format for Markdown_

**Manuscripts**
(web: [`manuscripts.github.io`](http://manuscripts.github.io),
 github: [`manuscripts`](https://github.com/manuscripts)) -
adds book.yml for book (meta) info e.g. title, author, publisher, year etc.
and contents.yml for table of contents and file structure

- Manuscripts Book Starter Kit (github: [`manuscripts/book-starter`](https://github.com/manuscripts/book-starter))



## CommonMark

_A strongly specified, highly compatible implementation of Markdown_

**CommonMark**
(web: [`commonmark.org`](http://commonmark.org))

- Spec (web: [`spec.commonmark.org`](http://spec.commonmark.org)) - Edited by John MacFarlane 
- Dingus (web: [`spec.commonmark.org/dingus`](http://spec.commonmark.org/dingus)) - try CommonMark in your browser
- Talk (web: [`talk.commonmark.org`](http://talk.commonmark.org))
- Code (github: [`jgm/CommonMark`](https://github.com/jgm/CommonMark)) - spec and reference code in JavaScript and C

## GitHub Flavored Markdown (GFM)

_CommonMark with GitHub Extensions_

**GitHub Flavored Markdown (GFM)**

- Spec (web: [`github.github.com/gfm`](https://github.github.com/gfm))
- Code (github: [`github/cmark`](https://github.com/github/cmark) - reference code in C (fork of cmark w/ extensions)

Extensions include:

Leaf Blocks: Tables ++ 
Container Blocks: Task list items ++
Inlines: Strikethrough; Autolinks; Disallowed Raw HTML


## Vanilla Flavored Markdown (VFMD)

_A variant of Markdown with an unambiguous specification of its syntax_ 

**Vanilla Flavored Markdown (VFMD)**
(web: [`vfmd.org`](http://www.vfmd.org), github: [`vfmd`](https://github.com/vfmd))

- Spec (web: [vfmd.org/vfmd-spec/specification](http://www.vfmd.org/vfmd-spec/specification)) - Edited by Roopesh Chander
- Code (github: [`vfmd/vfmd-src`](https://github.com/vfmd/vfmd-src)) - reference code in C++

Differences include:

Intra-word emphasis;
Simplified reference link/image syntax;
Lists and the 4-space rule;
Better automatic link detection;
Double blank lines as end of blocks;
Starting number in lists; 
Misnested constructs; 
Including raw HTML;
Character encoding



## Markdown Documentation

### Markdown Cheatsheets / Quick References

- [Markdown Cheatsheet :octocat:](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [The Ultimate Markdown Cheat Sheet](https://github.com/lifeparticle/Markdown-Cheatsheet)

### Markdown Getting Started Guides / Tutorials

- [Markdown Tutorial](http://markdowntutorial.com) - [:octocat:](https://github.com/gjtorikian/markdowntutorial.com)
- [Mastering Markdown @ GitHub Guides](https://guides.github.com/features/mastering-markdown)
- [Markdown Basics @ GitHub Help](https://help.github.com/articles/markdown-basics)
- [Markdown Guide](https://www.markdownguide.org/)



## Markdown Building Blocks

### Markdown Libraries & Tools

<a name="pandoc"></a>

**Pandoc**
(web: [`pandoc.org`](http://pandoc.org),
 github: [github.com/jgm/pandoc](https://github.com/jgm/pandoc)) -
a universal document converter (in Haskell)


**kramdown**
(web: [`kramdown.gettalong.org`](http://kramdown.gettalong.org),
 github: [`gettalong/kramdown`](https://github.com/gettalong/kramdown),
 gem: [`kramdown`](https://rubygems.org/gems/kramdown)) -
markdown library & command line tool (in Ruby)


**Markdown Extended (MDE)**
(github: [`e-picas/markdown-extended`](https://github.com/e-picas/markdown-extended)
- transform plain text input (strings or files) in various output formats (in PHP)

<a name="marked"></a>

**marked**
(web: [`marked.js.org`](https://marked.js.org), github: [marked :octocat:](https://github.com/markedjs/marked)) a markdown parser and compiler. Built for speed. (In Javascript)


<a name="markdown-it"></a>

**markdown-it**
(web: [`markdown-it.github.io`](https://markdown-it.github.io/), github: [markdown-it :octocat:](https://github.com/markdown-it/markdown-it)) Javascript markdown parser. 100% CommonMark support, extensions, syntax plugins & high speed.
Is extensible with [plugins](https://www.npmjs.com/search?q=keywords:markdown-it-plugin).

**concat-md**
([npm](https://www.npmjs.com/package/concat-md), [github](https://github.com/ozum/concat-md#readme)) CLI and API to concatenate markdown files and modify as necessary. Also adds titles from FrontMatter, file names and directory names, decreases level of existing titles to comply with added titles.

**mdcode**
(github: [mdcode](https://github.com/szkiba/mdcode)) Markdown code block authoring tool. It enables testable code blocks, with two-way synchronization between code blocks and source files.

**quikdown**
  ([web](https://deftio.github.io/quikdown/), [npm](https://www.npmjs.com/package/quikdown), [github 
  :octocat:](https://github.com/deftio/quikdown)) Lightweight (10KB) markdown parser with bidirectional
  HTML conversion, built-in XSS protection, and extensible plugin system. Zero dependencies, works in browser and
  Node.js. Features include drop-in editor component, TypeScript support, and lazy linefeeds for chat applications.
  ([Live Parser Demo](https://deftio.github.io/quikdown/examples/quikdown-live.html), [Editor 
  Demo](https://deftio.github.io/quikdown/examples/qde/))

**mq**
(web: [mqlang.org](https://mqlang.org), github: [mq :octocat:](https://github.com/harehare/mq)) A command-line tool that processes Markdown using a syntax similar to jq. Written in Rust, allowing you to easily slice, filter, map, and transform structured data in Markdown files.
  
### Babelmark

- [Babelmark 2]() - a tool for comparing the output of various implementations of Markdown syntax
    - [Babelmark 2 F.A.Q.](http://johnmacfarlane.net/babelmark2/faq.html) - frequently asked questions (and answers) e.g. ... ??


### Markdown Style Guides / Best Practices

to be done

### Markdown Lint / Style Rule Checker

- [markdownlint](https://github.com/DavidAnson/markdownlint) - A Node.js style checker and lint tool for Markdown/CommonMark files offering a good set of defaults. Allows for customization.
- [mdformat](https://github.com/executablebooks/mdformat) - CommonMark compliant Markdown formatter
- [mdlint]() to be done
- [mdsf](https://github.com/hougesen/mdsf) - Use your preferred code formatter to format markdown code snippets.
- [vscode-markdownlint](https://github.com/DavidAnson/vscode-markdownlint) - [Visual Studio Code Plugin](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) enabling in-place linting of markdown files.
- [mado](https://github.com/akiomik/mado) - A fast Markdown linter written in Rust. GitHub Actions are supported.


### Markdown Web Components / Custom Elements

- [Markdown-Tag](https://github.com/MarketingPipeline/Markdown-Tag) - Render Markdown to HTML on any website using a md tag
- [`<x-markdown>`]() - to be done




### Markdown to Website / Blog

**Jekyll**
(web: [`jekyllrb.com`](http://jekyllrb.com),
 github: [`jekyll/jekyll` :octocat:](https://github.com/jekyll/jekyll),
 gem: [`jekyll` :gem:](https://rubygems.org/gems/jekyll)) -
transform your plain text into static websites and blogs (in Ruby)

**Middleman**
(web: [`middlemanapp.com`](https://middlemanapp.com),
 github: [`middleman/middleman` :octocat:](https://github.com/middleman/middleman),
 gem: [`middleman` :gem:](https://rubygems.org/gems/middleman)) -
makes developing websites simple (in Ruby)

**Slate** (github: [lord/slate :octocat:](https://github.com/lord/slate)) - beautiful API documentation, based on **Middleman**

**Shins** (github: [`Mermade/shins` :octocat:](https://github.com/Mermade/shins), npm: [`shins`](https://www.npmjs.com/package/shins)) – beautiful API documentation, with node.js (port of **Slate**)

**md-fileserver** (github: [md-fileserver :octocat:](https://github.com/commenthol/md-fileserver), npm: [`md-fileserver`](https://www.npmjs.com/package/md-fileserver)) – View markdown files locally in browser.

**Compiiile** (github: [@compiiile/compiiile :octocat:](https://github.com/compiiile/compiiile), npm: [`@compiiile/compiiile`](https://www.npmjs.com/package/@compiiile/compiiile)) – Preview and serve folders containing Markdown files with full-text search and presentation slides.

**ZenMD** (github: [`@randomor/zenmd`](https://github.com/randomor/zenmd), npm: [`zenmd`](https://www.npmjs.com/package/zenmd) – The simplest way to convert a folder of Markdown files into a site of HTML files.

### Markdown to Email

**Markdown Here**
(web: [`markdown-here.com`](http://markdown-here.com),
 github: [`adam-p/markdown-here`](https://github.com/adam-p/markdown-here)) -
a browser extension for rendering email written in Markdown;
available for Chrome, Firefox, Safari, Thunderbird, and more;
besides email also works with Evernote, Google Groups, Blogger, and more



### Markdown to Presentation / Slideshow

**Slide Show (S9)**
(web: [`slideshow-s9.github.io`](http://slideshow-s9.github.io),
 github: [`slideshow-s9/slideshow`](https://github.com/slideshow-s9),
 gem: [`slideshow`](https://rubygems.org/gems/slideshow)) -
a free web alternative to PowerPoint and Keynote in Ruby

- Templates (github: [`slideshow-templates`](https://github.com/slideshow-templates))

**Slidev** (github: [`slidev`](http://github.com/slidevjs/slidev)) - Slidev allows you to create slideshows from a markdown file. You can include HTML and Vue components in the markdown.

**Markpress** (github: [`markpress`](https://github.com/gamell/markpress)) - A command line tool and node package to convert markdown files into self-contained [impressjs](https://github.com/impress/impress.js/) html presentations. [Example](https://gamell.github.io/markpress) 

**nodePPT** (github: [`nodePPT`](https://github.com/ksky521/nodePPT)) - A web presentation tool supporting markdown based on GFM.

**Deckset** (website: [Deckset](http://www.decksetapp.com)) – A macOS desktop app that renders Markdown presentations in beautifully designed templates.

**GitPitch** (website: [GitPitch](http://gitpitch.com/), github: [gitpitch :octocat:](https://github.com/gitpitch/gitpitch/)) – Markdown Presentations For Everyone on GitHub, GitLab, Bitbucket, GitBucket, Gitea, and Gogs. [Example](https://gitpitch.com/gitpitch/gitpitch/master)

**zoetic** (github [zoetic](https://github.com/kantord/zoetic)) - Markdown presentations with your webcam as your background while presenting

### Markdown to Portable Document Format (PDF)

- [markdown-pdf :octocat:](https://github.com/alanshaw/markdown-pdf), [(npm Package)](https://www.npmjs.com/package/markdown-pdf) -  converts Markdown files to PDFs


### Markdown Styles / Documents / Pages

**The Zen of Page Designs**
(github: [`pagedesigns`](https://github.com/pagedesigns))


### Markdown to Books

**The Zen of Book Designs**
(github: [`bookdesigns`](https://github.com/bookdesigns))



**Hyper Book (H9)** [:octocat:](https://github.com/hybook), [:gem:](https://rubygems.org/gems/hybook)

- [Templates :octocat:](https://github.com/book-templates)



### Markdown to Table of Contents (TOC)

* **Generate a markdown table of contents (TOC) with [remarkable](https://github.com/jonschlinkert/remarkable)**
  (github: [`markdown-toc`](https://github.com/jonschlinkert/markdown-toc)) 
* [markedpp](#markedpp) Markdown to Markdown Pre-Processor
* [mdtoc :octocat:](https://github.com/tallclair/mdtoc) - Standalone TOC generator designed for CI


### Markdown to Markdown Pre-Processor

<a name="markedpp"></a>

* **markedpp** (github: [markedpp :octocat:](https://github.com/commenthol/markedpp)) adds support for table-of-contents (TOC), numbered headings, includes other markdown files and/or create reference lists for use with different markdown processors like [marked](#marked), [markdown-it](#markdown-it), [pandoc](#pandoc) or for hosting on github.com, gitlab.com, bitbucket.org or ghost.org.


## Convert to Markdown Tools

### Microsoft Word to Markdown

- [Word To Markdowm gem :octocat:](https://github.com/benbalter/word-to-markdown), [:gem:](https://rubygems.org/gems/word-to-markdown) - "liberate" content from the jail that is Microsoft Word documents; converts to plain-text Markdown

### Hypertext Markup Language (HTML) to Markdown

Ruby

- [reverse_markdown :octocat:](https://github.com/xijo/reverse_markdown), [:gem:](https://rubygems.org/gems/reverse_markdown) - map simple HTML back into markdown
- [html2markdown :octocat:](https://github.com/29decibel/html2markdown), [:gem:](https://rubygems.org/gems/html2markdown) - simple and flexible HTML to markdown converter
- [hypertextmarkdown :octocat:](https://github.com/jcheatham/hypertextmarkdown), [:gem:](https://rubygems.org/gems/hypertextmarkdown) - HTML to markdown converter
- [html2md :octocat:](https://github.com/pmorton/html2md), [:gem:](https://rubygems.org/gems/html2md) - converts basic HTML to markdown 
- [unmarkdown :octocat:](https://github.com/soffes/unmarkdown), [:gem:](https://rubygems.org/gems/unmarkdown) - convert HTML to Markdown
- [upmark :octocat:](https://github.com/conversation/upmark), [:gem:](https://rubygems.org/gems/upmark) - a HTML to Markdown converter
- [remark :octocat:](https://github.com/mislav/remark) - HTML to Markdown converter in Ruby


JavaScript / Node.js

- [turndown :octocat:](https://github.com/domchristie/turndown), [(npm Package)](https://www.npmjs.com/package/turndown), [(Demo site)](http://domchristie.github.io/turndown/)  - a HTML to Markdown converter in JavaScript (formerly known as `to-markdown`)
- [html2markdown :octocat:](https://github.com/alexgorbatchev/html2markdown),  [(npm Package)](https://www.npmjs.com/package/html2markdown) -  converting HTML to Markdown
- [Markitdown](http://markitdown.medusis.com) - A client-side web app that lets you paste formatted text from a webpage (e.g with links intact) and recieve markdown output.
  - [Markitdown.medusis.com :octocat:](https://github.com/bambax/markitdown.medusis.com) - A client-side web app for converting rich text to markdown

More

- [heckyesmarkdown.com](http://heckyesmarkdown.com) - instantly convert a webpage to markdown; the service presents a simple interface that converts any reasonable web page into markdown (note: the service seems to use the Readability API to remove all the non-content cruft from the source page before proceeding with markdownification)

### Source Code to Markdown

Generate API documentation from source code in Markdown, then host it on the web using one of the many [Markdown to Website] tools to host and serve it.

- [widdershins :octocat:](https://github.com/Mermade/widdershins) - turn [OpenAPI/Swagger](https://www.openapis.org) REST API documentation to Markdown
- [Moxygen :octocat:](https://github.com/sourcey/moxygen) - [Doxygen](http://www.stack.nl/~dimitri/doxygen/) (C++, but also supports other popular programming languages such as C, Objective-C, C#, PHP, Java, Python, IDL , Fortran, VHDL, Tcl, and to some extent D.) documentation to Markdown
- [raml2html/markdown-theme :octocat:](https://github.com/raml2html/markdown-theme) - turn [RAML](http://raml.org) REST API documentation to Markdown using raml2html
- [jsdoc-to-markdown :octocat:](https://github.com/jsdoc2md/jsdoc-to-markdown) - JavaScript API documentation via JSDoc to Markdown
- [mmarkdown :octocat:](https://github.com/albinotonnina/mmarkdown) - Interpret mmd fenced code blocks in a markdown file and generate a cooler version of it.
- [markpush](https://gitlab.com/alex20465/markpush) - Firefox/Chrome Extension to push Articles on git repositories in a readable markdown format.

### Technical Documentation to Markdown

- [dita-ot-markdown](https://github.com/jelovirt/dita-ot-markdown) – converts DITA into Markdown, integrates with standard DITA OT toolchain 

### Screencast to Markdown

- [Paircast](https://paircast.io) - Combines desktop video, git diffs, and voice transcriptions into markdown documentation.

### JSON to Markdown

JavaScript / Node.js

- [json2md](https://github.com/IonicaBizau/json2md) - A JSON to Markdown converter.
- [ts-markdown](https://github.com/kgar/ts-markdown) - An extensible TypeScript markdown generator that takes JSON and creates a markdown document.

## Book Services

- [Softcover.io](https://www.softcover.io) - publish from the comfort of your command-line by Michael Hartl et al 
    - [Softcover :octocat:](https://github.com/softcover/softcover), [:gem:](https://rubygems.org/gems/softcover) - a command line tool for book generation, building, and publishing 
- [GitBook.com](https://www.gitbook.com)  - write and publish books with Markdown and Git by Samy Pessé et al
    - [GitBook :octocat:](https://github.com/GitbookIO/gitbook) - a command line tool (and Node.js library) for building beautiful books using GitHub/Git and Markdown (or AsciiDoc)
    
<!-- break -->

- [Bitbooks.cc (discontinued; archived)](https://github.com/bitbooks) - Bitbooks turns a repo full of markdown files into a handsome, hosted, online book - by Bryan Braun
    - [Franklin :octocat:](https://github.com/bryanbraun/franklin) - a static-site framework, optimized for online books



## Articles

- [Why You Shouldn't Use Markdown for Documentation](http://ericholscher.com/blog/2016/mar/15/dont-use-markdown-for-technical-docs) by Eric Holscher, March 2016
- [Stop Using Markdown For Documentation](https://mister-gold.pro/posts/en/asciidoc-vs-markdown/) by Anton Zolotukhin, April 2018
- [Why isn't there a formal grammar for Markdown?](http://roopc.net/posts/2014/markdown-cfg) by Roopesh Chander, September 2014
- [The Ultimate Markdown Cheat Sheet](https://medium.com/towards-data-science/the-ultimate-markdown-cheat-sheet-3d3976b31a0)


## Meta

**License**

The awesome list is dedicated to the public domain. Use it as you please with no restrictions whatsoever.

**Questions? Comments?**

Send them along to the markdown-discuss mailing list. Thanks!

