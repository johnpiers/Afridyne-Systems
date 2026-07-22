---
date: 2026-04-05
authors:
  - afridyne
categories:
  - Updates
  - Tutorials
---


# What MkDocs 2.0 means for your documentation projects

Last update: April 13, 2026 – see [update log].

---

!!! important "MkDocs 2.0"

    __Three weeks ago, MkDocs 2.0 was announced – a ground-up rewrite of the documentation tool tens of thousands of projects rely on, introducing potentially significant breaking changes.__
    
    Material for MkDocs depends on MkDocs as its underlying framework and central dependency. We maintain Material for MkDocs, but we have no control over MkDocs itself.
    
    We've taken the time to thoroughly evaluate and test the [MkDocs 2.0 pre-release] and want to share our findings, including what it might mean for your documentation projects, and where [Zensical], our new static site generator that is _compatible with MkDocs 1.x_, fits into the picture.
    
    __If you've missed it__: [MkDocs 1.x is unmaintained], with issues and PRs piling up and no releases in the past 18 months, and seemingly no plans to fix long-standing issues like [live-reload problems]. More importantly, it's unclear whether security issues will be addressed, and whether the project will receive any updates at all in the future.
    
    _Please note that MkDocs 2.0 is still in pre-release, and the information in this article is based on the current state of the project. We keep it updated as we learn more._
    
  [MkDocs 2.0 pre-release]: https://github.com/encode/mkdocs
  [Zensical]: https://squidfunk.github.io/mkdocs-material/blog/2025/11/05/zensical/
  [update log]: #updates

<!-- more -->

---

__This is the fifth article in a series:__

1. [Transforming Material for MkDocs]
2. [Zensical – A modern static site generator built by the creators of Material for MkDocs]
3. [Material for MkDocs Insiders – Now free for everyone]
4. [Goodbye, GitHub Discussions]
5. [What MkDocs 2.0 means for your documentation projects]

  [Transforming Material for MkDocs]: https://squidfunk.github.io/mkdocs-material/blog/2024/08/19/how-were-transforming-material-for-mkdocs/
  [Zensical – A modern static site generator built by the creators of Material for MkDocs]: https://squidfunk.github.io/mkdocs-material/blog/2025/11/05/zensical/
  [Material for MkDocs Insiders – Now free for everyone]: https://squidfunk.github.io/mkdocs-material/blog/2025/11/11/insiders-now-free-for-everyone/
  [Goodbye, GitHub Discussions]: https://squidfunk.github.io/mkdocs-material/blog/2025/11/18/goodbye-github-discussions/
  [What MkDocs 2.0 means for your documentation projects]: https://squidfunk.github.io/mkdocs-material/blog/2026/02/18/mkdocs-2.0/

## What's changing in MkDocs 2.0

!!! version-added "What's changing in MkDocs 2.0"

    Based on the [official announcement], the published [roadmap], and several prior comments and statements from the project's maintainer, MkDocs 2.0 is intended as a ground-up rewrite of the project to reduce complexity – and it comes with some important trade-offs:
    
    - __MkDocs 2.0 is incompatible with Material for MkDocs__ – If your documentation is built with Material for MkDocs, it will cease to work with MkDocs 2.0. Material for MkDocs makes extensive use of the templating and plugin systems of MkDocs 1.x, and the changes that MkDocs 2.0 introduces are not backward-compatible.
    
    - __MkDocs 2.0 won't have a plugin system__ – MkDocs 2.0 is being rewritten with a focus on theming, deliberately [removing plugin support to simplify the codebase]. We believe [the plugin ecosystem] is one of the cornerstones of MkDocs' success and widespread adoption, and its removal will affect workflows and customizations that teams have built over time.
    
    - __MkDocs 2.0 brings breaking changes for themes__ – MkDocs 2.0 comes with a completely rewritten theming system. For instance, [navigation is passed to themes as pre-rendered HTML] rather than structured data. This makes it technically impossible to implement features like navigation tabs, collapsible sections, and other advanced navigation patterns.
    
    ---
    
    It also limits how navigation can be styled in themes, since the HTML of the navigation cannot be adjusted to fit the theme's structure and design.
    
    - __MkDocs 2.0 has a closed contribution model__ – MkDocs 2.0 moves to a "maintainer-driven issues" model, where community members are [asked not to open issues or pull requests], and "feature requests are generally not accepted". It's unclear how users should report bugs or seek fixes when they encounter problems.
    
    - __MkDocs 2.0 is currently unlicensed__ – MkDocs 2.0 doesn't specify a license, which has implications for how it can be used and contributed to by the community. It's unclear what the rationale behind this decision is, but it should be critically evaluated by teams and organizations that rely on MkDocs for their documentation projects.
    
    - __MkDocs 2.0 has a new configuration format__ – MkDocs 2.0 uses TOML for configuration, which is incompatible with the YAML format used in MkDocs 1.x. As a result, existing `mkdocs.yml` files will currently not work with MkDocs 2.0. There is no migration path for existing projects.
    
    ---
    
    A release date has not been announced, so planning around a specific timeline remains difficult. However, the direction of travel has been hinted at by the maintainer on several occasions, and the pre-release version already confirms the impact of these changes on existing projects.
    
  [official announcement]: https://github.com/mkdocs/mkdocs/discussions/4077
  [roadmap]: https://github.com/squidfunk/mkdocs-material/issues/8478#issuecomment-3778358483
  [asked not to open issues or pull requests]: https://github.com/encode/mkdocs?tab=contributing-ov-file#maintainer-driven-issues
  [removing plugin support to simplify the codebase]: https://github.com/mkdocs/mkdocs/discussions/3815#discussioncomment-10398312
  [the plugin ecosystem]: https://github.com/mkdocs/catalog?tab=readme-ov-file#contents
  [navigation is passed to themes as pre-rendered HTML]: https://www.encode.io/mkdocs/styling/#templates
  [MkDocs 1.x is unmaintained]: https://github.com/mkdocs/mkdocs/discussions/4010
  [live-reload problems]: https://github.com/squidfunk/mkdocs-material/issues/8478

## What this means for you?

!!! education "What this means for you?"

    It's worth paying attention: the long-term direction of MkDocs is shifting in ways that diverge from how many documentation teams – and their tooling – currently operate.
    
    While your existing MkDocs projects should continue to work today, be aware that future updates to MkDocs 1.x are unlikely. MkDocs 2.0, in its current form, is not a drop-in replacement for MkDocs 1.x, and does not provide a clear migration path for existing projects.
    
??? info "How to disable the MkDocs 2.0 incompatibility warning"

    Starting in Material for Mkdocs 9.7.2, a warning is printed during a build about the upcoming MkDocs 2.0 changes. We added this warning to ensure users are aware of the potential impact of MkDocs 2.0 on their projects, and to encourage them to evaluate their options and plan accordingly.

    To disable this warning, set this environment variable:

    ``` bash
    export NO_MKDOCS_2_WARNING=1
    ```

## We raised concerns early.

!!! Instruction "We raised concerns early."

    All of this isn't coming as a surprise to us, given that the maintainer has presented his plans in an open video call [back in August 2024]. Since it was unclear whether the maintainer would follow through with these plans, we only mentioned it in a footnote, but the pre-release version of MkDocs 2.0 confirms that there will be significant breaking changes for existing projects:
    
    ---
    
    Here's a summary of [the timeline of events]:
    
    > After [we raised this issue] with the maintainers of MkDocs [...], and [maintainership changed] mid 2024, work on a [ground-up rewrite] that aims to address slow reloads by [rendering only the page currently being built] has started. It's still unclear how this rewrite will integrate with the requirements of existing plugins. Complex plugins such as [mkdocstrings], or our [built-in blog] and [tags] plugins require a coordinated build of all pages to accurately resolve links between pages and to computed resources, which cannot be determined without building the entire project.
    
    > __Update__{ title="August 21, 2024" }: The new maintainer now publicly stated that he's working towards a new version of MkDocs that [does not require or support plugins], and mentions it will be equally capable through offering customization via templating, themes, and styling, which he also mentioned to us and several other users in [a team call on August 1]. In this call, [we raised objections multiple times] in regards to how this will impact the ecosystem, to no avail. No intention or roadmap for plugin support was provided. This development is orthogonal to our goal empowering users and organizations to adapt the core framework to their requirements by the means of modularity. We're working on resolving this situation, and will provide a way forward for our community.
    
    ---
    
    The moment we learned about these plans, [we immediately started working] on what would eventually become [Zensical] – a new static site generator designed to be backward-compatible with MkDocs 1.x and a reliable long-term home for your existing documentation projects.
    
    ---
    
    For years, we were trying to improve MkDocs from within. We authored [12 plugins], which gave us a deep understanding of the plugin API's limitations. We conducted quantitative and qualitative analyses of the ecosystem to identify where MkDocs was falling short and talked to dozens of organizations and key ecosystem members. We raised these issues and repeatedly got nowhere. When the new direction of MkDocs 2.0 became apparent, the thinking was already done.
    
## Why forking is impractical.

We considered forking MkDocs, but quickly realized it wasn't viable: every plugin in the ecosystem has a direct dependency on `mkdocs`, which means forking MkDocs would require forking every single one of its [300 plugins] – __like moving an entire city at once__.

!!! recommendation "Why forking MkDocs isn't a viable path"

    MkDocs is Open Source and permissively licensed, so forking it seems like the natural answer – it's exactly what Open Source is designed for. Take the codebase, fix what's broken, maintain it under a new name, and move forward. There are two reasons why we don't consider this a viable path forward for the ecosystem:
    
    ---

    **The dependency problem.** Every plugin in the MkDocs ecosystem has a direct dependency on the `mkdocs` package. A fork would need a different package name, which means every one of the [300+ plugins] in the ecosystem would also need to be forked and updated.

    You could work around this by intercepting Python's import system at runtime, making your fork silently pretend to be `mkdocs` – and some forks have done exactly that. But this only preserves the ecosystem on the surface. Plugins interact with MkDocs in two ways: through the official hook system, and by directly calling functions and accessing data structures that MkDocs exposes. Unlike many languages, Python has no concept of visibility – there is no distinction between public and internal APIs. In practice, this means that every function, class, and variable in MkDocs is potentially plugin surface. Plugins routinely reach into MkDocs internals – not because they're badly written, but because there was no other way to get the job done. Any meaningful change to the codebase risks breaking plugins in ways that are hard to predict and even harder to debug.
    
    ---

    <font color="#ff6b6b">**The architecture problem.**</font> Even a fork that solves the dependency problem inherits the deeper issues that have held MkDocs back for years. Anyone who has written MkDocs plugins knows the long tail of "plugin X is incompatible with plugin Y" reports – these aren't one-off bugs, they're a systemic consequence of how the plugin architecture works. As we documented in [ZAP 007], the underlying problem is that MkDocs has no model of data dependencies, which makes the following impossible without a ground-up rewrite:

    - <font color="#EF559F">**Parallel builds**</font> – plugins share mutable state at fixed synchronization points, making safe parallelization impossible even with free-threaded Python.
    - <font color="#4dadf7">**Differential builds**</font> – without knowing what each plugin reads and writes, there's no way to skip work that hasn't changed.
    - <font color="#20c997">**Multi-project coordination**</font> – MkDocs has no programmatic API for coordinating multiple builds, forcing fragile workarounds like cross-process manifests.
    - <font color="#FFDF42">**Meaningful caching**</font> – with no runtime-managed build graph, every plugin has to implement its own caching, and most don't.
    - <font color="#ff6b6b">**Fast live preview**</font> – MkDocs must complete a full build before the preview server accepts connections, because navigation requires the entire site to be known upfront.
          
      ---

    A fork inherits all of these insurmountable limitations. The only way to fix these problems is to rethink how plugins work at a fundamental level – at which point you're no longer forking MkDocs, you're building something new.

    That's what we did.

  [300+ plugins]: https://github.com/mkdocs/catalog?tab=readme-ov-file#contents
  [ZAP 007]: https://zensical.org/spark/proposals/zap-007-module-system/

!!! important "Impractical"
    With forking being impractical, we had to start from scratch.
    
  [we immediately started working]: https://squidfunk.github.io/mkdocs-material/blog/2024/08/19/how-were-transforming-material-for-mkdocs/
  [the timeline of events]: https://squidfunk.github.io/mkdocs-material/blog/2024/08/19/how-were-transforming-material-for-mkdocs/#fn:7
  [back in August 2024]: https://github.com/mkdocs/mkdocs/discussions/3671#discussioncomment-10164237
  [300 plugins]: https://github.com/mkdocs/catalog?tab=readme-ov-file#contents
  [we raised this issue]: https://github.com/mkdocs/mkdocs/issues/3695
  [maintainership changed]: https://github.com/mkdocs/mkdocs/discussions/3677
  [ground-up rewrite]: https://github.com/mkdocs/sketch
  [rendering only the page currently being built]: https://github.com/mkdocs/mkdocs/issues/3695#issuecomment-2117939743
  [mkdocstrings]: https://mkdocstrings.github.io/
  [built-in blog]: https://squidfunk.github.io/mkdocs-material/plugins/blog/
  [tags]: https://squidfunk.github.io/mkdocs-material/plugins/tags/
  [does not require or support plugins]: https://github.com/mkdocs/mkdocs/discussions/3815#discussioncomment-10398312
  [a team call on August 1]: https://github.com/mkdocs/mkdocs/discussions/3671#discussioncomment-10164237
  [we raised objections multiple times]: https://github.com/mkdocs/mkdocs/discussions/3671#discussioncomment-10215445
  [a reliable, backward-compatible home]: https://zensical.org/compatibility/
  [12 plugins]: https://squidfunk.github.io/mkdocs-material/plugins/

## Where Zensical comes in.

!!! abstract "Zensical"

    [Zensical][website] is designed to be a __drop-in replacement for MkDocs 1.x__, with the goal of building your existing projects without any changes. _We're not fully there yet_ – supporting the most popular MkDocs plugins in the ecosystem is an ambitious undertaking – but it's our current focus, and we're fully committed to getting there.
    
    Rather than turning this into a marketing pitch, we encourage you to read the [announcement post][Zensical] if you'd like to understand how Zensical differs from MkDocs and what you can already expect today. Additionally, the [compatibility section] on our website offers an overview of what features are already supported without changes.
    
    We also encourage you to do your own research, evaluate the implications for your projects, and consider all available options. If you've relied on Material for MkDocs professionally, valued our work, and are looking for a clear path forward, we're offering [hands-on support for migration].
    
    _If you have any questions, feel free to reach out to Kathi at hello@zensical.org._
    
## Updates.

!!! desc "April 2026"

    ### April 2026.
    
    - __April 13, 2026__: We added a section on why forking MkDocs isn't a viable path forward for the ecosystem – an excerpt of [ZAP 007], which analyzes MkDocs' architectural limitations.
    
!!! desc "March 2026"

    ### March 2026.
    
    - __March 27, 2026__: In [Talk Python To Me #542](https://talkpython.fm/episodes/show/542), Martin Donath shares the backstory of Zensical, and reflects on the lessons learned maintaining Material for MkDocs for almost a decade.
    
    - __March 22, 2026__: In [The Slow Collapse of MkDocs], Florian Maas outlines the entire timeline of events starting in 2014 that eventually led to the fracturing of the MkDocs ecosystem.
    
    - __March 10, 2026__: We released 9.7.5, which limits the version range of MkDocs to `<2`. This ensures that your builds will continue to work, even if MkDocs 2.0 is released.
    
    - __March 10, 2026__: Access to the `mkdocs` package for the maintainers removed on March 9 [seems to have been restored](https://github.com/orgs/ProperDocs/discussions/1#discussioncomment-16060966), including the original creator of MkDocs.
    
    - __March 9, 2026__: One of the previous maintainers [changed ownership of the `mkdocs` package on PyPI](https://web.archive.org/web/20260310162839/https://github.com/mkdocs/mkdocs/discussions/4089)[^2], removing access for all other maintainers, including the original creator of MkDocs.
    
    [^2]:
      The link points to the web archive, as the original post has been edited multiple times by the previous maintainer.
      
    - __March 4, 2026__: We added a paragraph explaining that prior attempts on resolving the situation were unsuccessful and why we decided to find a new path for our community.
    
    - __March 3, 2026__: We added a paragraph on the new contribution model that MkDocs 2.0 is adopting, and the implications for users and contributors from our perspective.
    
!!! desc "February 2026"

    ### February 2026.
    
    - __February 27, 2026__: We added a note on the `NO_MKDOCS_2_WARNING` environment variable to disable the MkDocs 2.0 incompatibility warning in Material for MkDocs.
    
    - __February 19, 2026__: The published MkDocs 2.0 roadmap was deleted. The link now points to an issue comment that contains a screenshot of the last available version of the roadmap.
    
    - __February 13, 2026__: The mention of compatibility planned for MkDocs 1.x and MkDocs 2.0 projects was removed from the MkDocs 2.0 [`README.md`](https://github.com/encode/mkdocs/commit/313d3e8#diff-b335630551682c19a781afebcf4d07bf978fb1f8ac04c6bf87428ed5106870f5L52).
    
  [The Slow Collapse of MkDocs]: https://fpgmaas.com/blog/collapse-of-mkdocs/
  [compatibility section]: https://zensical.org/compatibility/features/
  [hands-on support for migration]: https://zensical.org/spark/
  [website]: https://zensical.org
  [why we built Zensical]: Zensical.md
  [feature parity]: https://zensical.org/compatibility/features/
  [module system]: https://zensical.org/about/roadmap/#module-system
  
---

<a href="https://www.mathjax.org" class="mathjax-badge">
    <img title="Powered by MathJax"
    src="https://www.mathjax.org/badge/mj_logo.png"
    border="0" alt="Powered by MathJax" />
</a>

<H2 style="text-align: center;">The First Isomorphism Theorem</H2>
<H3 style="text-align: center;">R. C. Daileda</H3> 

??? desc "Misc Maths Fun! Click on the formulas to see the magic."
    ### 1st Isomorphism Theorem {.toc-hidden-header}
    <a href="https://www.mathjax.org">
        <img title="Powered by MathJax"
        src="https://www.mathjax.org/badge/badge.gif"
        border="0" alt="Powered by MathJax" />
    </a>
    
    The homomorphism $\color{#ff6b6b}{f}$ is injective if and only if its kernel is only the singleton set $\color{#f08c00}{e_G}$, because otherwise $\color{#cc5de8}{\exists}\, \color{#f08c00}{a},\color{#f08c00}{b}\color{#cc5de8}{\in} \color{#4dadf7}{G}$ with $\color{#f08c00}{a}\color{#cc5de8}{\neq} \color{#f08c00}{b}$ such that $\color{#ff6b6b}{f}(\color{#f08c00}{a})=\color{#ff6b6b}{f}(\color{#f08c00}{b})$.
    
    ---
            
       
    Let $\color{#4dadf7}{G}$ be a group. For any $\color{#20c997}{H} \color{#cc5de8}{<} \color{#4dadf7}{G}$, the "reduction mod $\color{#20c997}{H}$" map

    $$\begin{aligned}
    \color{#ff6b6b}{\pi} : \color{#4dadf7}{G} &\to \color{#4dadf7}{G}/\color{#20c997}{H}, \\
    \color{#f08c00}{a} &\mapsto \color{#f08c00}{a}\color{#20c997}{H},
    \end{aligned}$$

    which sends each element of $\color{#4dadf7}{G}$ to its coset in $\color{#4dadf7}{G}/\color{#20c997}{H}$ is called the natural surjection. When $\color{#20c997}{H} \color{#cc5de8}{\triangleleft} \color{#4dadf7}{G}$, we have:

    $$\color{#ff6b6b}{\pi}(\color{#f08c00}{a}\color{#f08c00}{b}) = (\color{#f08c00}{a}\color{#f08c00}{b})\color{#20c997}{H} = (\color{#f08c00}{a}\color{#20c997}{H})(\color{#f08c00}{b}\color{#20c997}{H}) = \color{#ff6b6b}{\pi}(\color{#f08c00}{a})\color{#ff6b6b}{\pi}(\color{#f08c00}{b}),$$

    for all $\color{#f08c00}{a}, \color{#f08c00}{b} \color{#cc5de8}{\in} \color{#4dadf7}{G}$. This means that $\color{#ff6b6b}{\pi}$ is actually a surjective homomorphism in this case, which we call the natural epimorphism. Since $\color{#20c997}{H}$ is the identity coset in $\color{#4dadf7}{G}/\color{#20c997}{H}$, notice that $\color{#f08c00}{a} \color{#cc5de8}{\in} \color{#20c997}{\ker \pi}$ if and only if:

    $$\color{#f08c00}{a}\color{#20c997}{H} = \color{#ff6b6b}{\pi}(\color{#f08c00}{a}) = \color{#20c997}{H} \color{#cc5de8}{\iff} \color{#f08c00}{a} \color{#cc5de8}{\in} \color{#20c997}{H}.$$

    Thus:

    $$\color{#20c997}{\ker \pi} = \color{#20c997}{H}.$$

    That is, every normal subgroup of $\color{#4dadf7}{G}$ is the kernel of a homomorphism with domain $\color{#4dadf7}{G}$. The converse is also true.
    
    **Lemma 1.** Let $\color{#ff6b6b}{f} : \color{#4dadf7}{G} \to \color{#20c997}{G'}$ be a homomorphism of groups. Then $\color{#20c997}{\ker f} \color{#cc5de8}{\triangleleft} \color{#4dadf7}{G}$.
    
    **Proof.** Let $\color{#f08c00}{x} \color{#cc5de8}{\in} \color{#4dadf7}{G}$ and let $\color{#f08c00}{a} \color{#cc5de8}{\in} \color{#20c997}{\ker f}$. Then $\color{#ff6b6b}{f}(\color{#f08c00}{a}) = \color{#f08c00}{e'}$ is the identity in $\color{#20c997}{G'}$ so that:
    
    $$\color{#ff6b6b}{f}(\color{#f08c00}{x}\color{#f08c00}{a}\color{#f08c00}{x}^{-1}) = \color{#ff6b6b}{f}(\color{#f08c00}{x})\color{#ff6b6b}{f}(\color{#f08c00}{a})\color{#ff6b6b}{f}(\color{#f08c00}{x})^{-1} = \color{#ff6b6b}{f}(\color{#f08c00}{x})\color{#f08c00}{e'}\color{#ff6b6b}{f}(\color{#f08c00}{x})^{-1} = \color{#ff6b6b}{f}(\color{#f08c00}{x})\color{#ff6b6b}{f}(\color{#f08c00}{x})^{-1} = \color{#f08c00}{e'},$$
    
    which shows that $\color{#f08c00}{x}\color{#f08c00}{a}\color{#f08c00}{x}^{-1} \color{#cc5de8}{\in} \color{#20c997}{\ker f}$.
    
    Since $\color{#f08c00}{a} \color{#cc5de8}{\in} \color{#20c997}{\ker f}$ was arbitrary, this proves:
    
    $$\color{#f08c00}{x}(\color{#20c997}{\ker f})\color{#f08c00}{x}^{-1} \color{#cc5de8}{\subseteq} \color{#20c997}{\ker f}.$$
    
    And since $\color{#f08c00}{x} \color{#cc5de8}{\in} \color{#4dadf7}{G}$ was arbitrary, this proves $\color{#20c997}{\ker f} \color{#cc5de8}{\triangleleft} \color{#4dadf7}{G}$. <span style="float: right">$\square$</span>
    
    Given a group $\color{#4dadf7}\mathbf{G}$ and a subgroup $\color{#20c997}\mathbf{H}$, Lemma 1 provides perhaps the easiest way to show that $\color{#20c997}\mathbf{H}$ is normal in $\color{#4dadf7}\mathbf{G}$: simply identify $\color{#20c997}\mathbf{H}$ as the kernel of a homomorphism $\color{#ff6b6b}{\mathbf{f}} : \color{#4dadf7}\mathbf{G} \to \color{#20c997}\mathbf{G'}$.
    
    There is actually a deeper connection between normal subgroups and kernels. Let $\color{#ff6b6b}{\mathbf{f}} : \color{#4dadf7}\mathbf{G} \to \color{#20c997}\mathbf{G'}$ be a group homomorphism. We have seen that $\color{#ff6b6b}{\mathbf{f}}$ is injective if and only if $\color{#20c997}\boldsymbol{\ker \mathbf{f}}$ is trivial. Until now this is the only real utility we’ve found for the kernel of a homomorphism.
    
    But when $\color{#20c997}\boldsymbol{\ker \mathbf{f}}$ is nontrivial it actually provides a precise measurement of the failure of the injectivity of $\color{#ff6b6b}{\mathbf{f}}$.
    
    To see why, for $\color{#f08c00}{\mathbf{a}}, \color{#f08c00}{\mathbf{b}} \in \color{#4dadf7}\mathbf{G}$ we define $\color{#f08c00}{\mathbf{a}} \color{#ff6b6b}\boldsymbol{\sim} \color{#f08c00}{\mathbf{b}}$ if and only if $\color{#ff6b6b}{\mathbf{f}}(\color{#f08c00}{\mathbf{a}}) = \color{#ff6b6b}{\mathbf{f}}(\color{#f08c00}{\mathbf{b}}).$ It is an easy exercise to see that $\color{#ff6b6b}\boldsymbol{\sim}$ is an equivalence relation on $\color{#4dadf7}\mathbf{G}$ (indeed, on the domain of any function between two sets). Since
    
    $$\color{#ff6b6b}{\mathbf{f}(\mathbf{a}) = \mathbf{f}(\mathbf{b})} \;\color{#cc5de8}{\iff}\; \color{#f08c00}{\mathbf{e}} \color{#ffffff}{=} \color{#ff6b6b}{\mathbf{f}(\mathbf{b})^{-1}\mathbf{f}(\mathbf{a}) = \mathbf{f}(\mathbf{b}^{-1}\mathbf{a})} \;\color{#cc5de8}{\iff}\; \color{#f08c00}{\mathbf{b}^{-1}\mathbf{a}} \color{#cc5de8}{\in} \color{#20c997}\boldsymbol{\ker \mathbf{f}} \;\color{#cc5de8}{\iff}\; \color{#f08c00}{\mathbf{a}} \color{#cc5de8}{\equiv} \color{#f08c00}{\mathbf{b}} \;\color{#cc5de8}{\pmod{\color{#20c997}\boldsymbol{\ker \mathbf{f}}}}$$
    
    the relation $\color{#ff6b6b}\boldsymbol{\sim}$ is just congruence modulo $\color{#20c997}\boldsymbol{\ker \mathbf{f}}.$ So the equivalence class of $\color{#f08c00}{\mathbf{a}} \in \color{#4dadf7}\mathbf{G}$ under $\color{#ff6b6b}\boldsymbol{\sim}$ is just the coset $\color{#f08c00}{\mathbf{a}}(\color{#20c997}\boldsymbol{\ker \mathbf{f}}):$
    
    <div class="eq-tagged" markdown>

    $$\color{#f08c00}{\mathbf{a}}(\color{#20c997}\boldsymbol{\ker \mathbf{f}}) = \color{#cc5de8}{\{}\color{#f08c00}{\mathbf{b}} \color{#cc5de8}{\in} \color{#4dadf7}\mathbf{G} \;\color{#cc5de8}{\mid}\; \color{#ff6b6b}{\mathbf{f}(\mathbf{b}) = \mathbf{f}(\mathbf{a})}\color{#cc5de8}{\}}$$

    <span class="eq-tag">(1)</span>

    </div>
    
---