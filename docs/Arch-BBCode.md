---
icon: material/arch
---

<div style="display: none;">
  <h1>Header</h1>
</div>

![Local image](./assets/logo1.svg){ .center-image }

<H1 style="text-align: center;">💡 Arch BBCode</H1>

BBCode is a collection of formatting tags that are used to change the look of text in this forum. BBCode is based on the same principal as, and is very similar to, HTML. Below is a list of all the available BBCodes and instructions on how to use them.

Administrators have the ability to enable or disable BBCode. You can tell if BBCode is enabled or disabled whenever you post a message or edit your signature.

!!! tip "BBCode Styles"
    **The following tags change the appearance of text:**

    `[b]Bold text[/b]` produces **Bold text**

    `[u]Underlined text[/u]` produces <u>Underlined text</u>

    `[i]Italic text[/i]` produces *Italic text*

    `[s]Strike-through text[/s]` produces ~~Strike-through text~~

    `[del]Deleted text[/del]` produces <del>Deleted text</del>

    `[ins]Inserted text[/ins]` produces <ins>Inserted text</ins>

    `[em]Emphasised text[/em]` produces *Emphasised text*

    `[color=#FF0000]Red text[/color]` produces <span style="color: #FF0000;">Red text</span>

    `[color=blue]Blue text[/color]` produces <span style="color: blue;">Blue text</span>

    `[h]Heading Text[/h]` produces Heading Text


!!! warning "Links and Images"
    **You can create links to other documents or to email addresses using the following tags:**

    `[url=https://bbs.archlinux.org/]Arch Linux Forums[/url]` produces [Arch Linux Forums](https://bbs.archlinux.org/)

    `[url]https://bbs.archlinux.org/[/url]` produces [https://bbs.archlinux.org/](https://bbs.archlinux.org/)

    `[url=/help.php]This help page[/url]` produces [This help page](https://bbs.archlinux.org/help.php)

    `[email]myname@example.com[/email]` produces [myname@example.com](mailto:myname@example.com)

    `[email=myname@example.com]My email address[/email]` produces [My email address](mailto:myname@example.com)

    `[topic=1]Test topic[/topic]` produces [Test topic](https://bbs.archlinux.org/viewtopic.php?id=1)

    `[topic]1[/topic]` produces [https://bbs.archlinux.org/viewtopic.php?id=1](https://bbs.archlinux.org/viewtopic.php?id=1)

    `[post=1]Test post[/post]` produces [Test post](https://bbs.archlinux.org/viewtopic.php?pid=1#p1)

    `[post]1[/post]` produces [https://bbs.archlinux.org/viewtopic.php?pid=1#p1](https://bbs.archlinux.org/viewtopic.php?pid=1#p1)

    `[forum=1]Test forum[/forum]` produces [Test forum](https://bbs.archlinux.org/viewforum.php?id=1)

    `[forum]1[/forum]` produces [https://bbs.archlinux.org/viewforum.php?id=1](https://bbs.archlinux.org/viewforum.php?id=1)

    `[user=2]Test user[/user]` produces [Test user](https://bbs.archlinux.org/profile.php?id=2)

    `[user]2[/user]` produces [https://bbs.archlinux.org/profile.php?id=2](https://bbs.archlinux.org/profile.php?id=2)

    ---

    If you want to display an image you can use the img tag. The text appearing after the "=" sign in the opening tag is used for the alt attribute and should be included whenever possible.

    `[img=FluxBB bbcode test]https://bbs.archlinux.org/img/test.png[/img]` produces ![FluxBB bbcode test](https://bbs.archlinux.org/img/test.png)


!!! danger "Quotes"
    **If you want to quote someone, you should use the quote tag.**

    `[quote=James]This is the text I want to quote.[/quote]`

    produces a quote box like this:
    > **James wrote:**
    > This is the text I want to quote.

    If you don't want to quote anyone in particular, you can use the quote tag without specifying a name.

    `[quote]This is the text I want to quote.[/quote]`

    produces a quote box like this:
    > This is the text I want to quote.

    **Note:** If a username contains the characters `[` or `]` you can enclose it in quote marks.


!!! info "Advanced Formatting"
    ### Code
    When displaying source code you should make sure that you use the code tag. Text displayed with the code tag will use a monospaced font and will not be affected by other tags.

    `[code]This is some code.[/code]`

    produces:
    ```
    This is some code.
    ```

    ---

    ### Lists
    To create a list you can use the list tag. You can create 3 types of lists using the list tag.

    `[list][*]Example list item 1.[/*][*]Example list item 2.[/*][*]Example list item 3.[/*][/list]`
    produces a bulleted list:
    * Example list item 1.
    * Example list item 2.
    * Example list item 3.

    `[list=1][*]Example list item 1.[/*][*]Example list item 2.[/*][*]Example list item 3.[/*][/list]`
    produces a numbered list:
    1. Example list item 1.
    2. Example list item 2.
    3. Example list item 3.

    `[list=a][*]Example list item 1.[/*][*]Example list item 2.[/*][*]Example list item 3.[/*][/list]`
    produces an alphabetically labelled list:
    a. Example list item 1.
    b. Example list item 2.
    c. Example list item 3.

    ---

    ### Nested Tags
    BBCode can be nested to create more advanced formatting. For example:
    `[b][u]Bold, underlined text[/u][/b]` produces **<u>Bold, underlined text</u>**

    ---

    ### Smilies
    If you like (and if it is enabled), the forum can convert a series of smilies to images.


    | Code | Result | Code | Result |
    | :--- | :--- | :--- | :--- |
    | `:)` or `=)` | ![smile](https://bbs.archlinux.org/img/smilies/smile.png) | `:|` or `=|` | ![neutral](https://bbs.archlinux.org/img/smilies/neutral.png) |
    | `:(` or `=(` | ![sad](https://bbs.archlinux.org/img/smilies/sad.png) | `:D` or `=D` | ![big_smile](https://bbs.archlinux.org/img/smilies/big_smile.png) |
    | `:o` or `:O` | ![yikes](https://bbs.archlinux.org/img/smilies/yikes.png) | `;)` | ![wink](https://bbs.archlinux.org/img/smilies/wink.png) |
    | `:/` | ![hmm](https://bbs.archlinux.org/img/smilies/hmm.png) | `:P` or `:p` | ![tongue](https://bbs.archlinux.org/img/smilies/tongue.png) |
    | `:lol:` | ![lol](https://bbs.archlinux.org/img/smilies/lol.png) | `:mad:` | ![mad](https://bbs.archlinux.org/img/smilies/mad.png) |
    | `:rolleyes:` | ![roll](https://bbs.archlinux.org/img/smilies/roll.png) | `:cool:` | ![cool](https://bbs.archlinux.org/img/smilies/cool.png) |
