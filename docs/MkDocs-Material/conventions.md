---
icon: simple/materialformkdocs
---

![](imgs/20260107-220626.png){ .center-image }
<H1 style="text-align: center;">Conventions</H1>

!!! important "Conventions"
    This section explains several conventions used in this documentation.
    
## Symbols

!!! desc "Symbols"

    This documentation use some symbols for illustration purposes. Before you read on, please make sure you've made yourself familiar with the following list of conventions:
    
### <!-- md:version --> – Version { data-toc-label="Version" }

!!! desc "Version"

    The tag symbol in conjunction with a version number denotes when a specific feature or behavior was added. Make sure you're at least on this version if you want to use it.
    
### <!-- md:default --> – Default Value { #default data-toc-label="Default Value" }

!!! desc "Default Value"

    Some properties in `mkdocs.yml` have default values for when the author does not explicitly define them. The default value of the property is always included.
    
#### <!-- md:default computed --> – Default value Is Computed { #default data-toc-label="Is Computed" }

!!! desc "Default Value is Computed"

    Some default values are not set to static values but computed from other values, like the site language, repository provider, or other settings.
    
#### <!-- md:default none --> – Default Value is Empty { #default data-toc-label="Is Empty" }

!!! desc "Default Value is Empty"

    Some properties do not contain default values. This means that the functionality that is associated with them is not available unless explicitly enabled.
    
### <!-- md:flag metadata --> – Metadata Property { #metadata data-toc-label="Metadata Property" }

!!! desc "Metadata Property"

    This symbol denotes that the thing described is a metadata property, which can be used in Markdown documents as part of the front matter definition.
    
### <!-- md:flag multiple --> – Multiple Instances { #multiple-instances data-toc-label="Multiple Instances" }

!!! desc "Multiple instances"

    This symbol denotes that the plugin supports multiple instances, i.e, that it can be used multiple times in the `plugins` setting in `mkdocs.yml`.
    
### <!-- md:feature --> – Optional Feature { #feature data-toc-label="Optional Feature" }

!!! desc "Optional Feature"

    Most of the features are hidden behind feature flags, which means they must be explicitly enabled via `mkdocs.yml`. This allows for the existence of potentially orthogonal features.
    
### <!-- md:flag experimental --> – Experimental { data-toc-label="Experimental" }

!!! desc "Experimental"

    Some newer features are still considered experimental, which means they might (although rarely) change at any time, including their complete removal (which hasn't happened yet).
    
### <!-- md:plugin --> – Plugin { data-toc-label="Plugin" }

!!! desc "Plugin"

    Several features are implemented through MkDocs excellent plugin architecture, some of which are built-in and distributed with Material for MkDocs, so no installation is required.
    
### <!-- md:extension --> – Markdown Extension { data-toc-label="Markdown Extension" #extension }

!!! desc "Markdown Extension"

    This symbol denotes that the thing described is a Markdown extension, which can be enabled in `mkdocs.yml` and adds additional functionality to the Markdown parser.
    
### <!-- md:flag required --> – Required Value { #required data-toc-label="Required Value" }

!!! desc "Required Value"

    Some (very few in fact) properties or settings are required, which means the authors must explicitly define them.
    
### <!-- md:flag customization --> – Customization { #customization data-toc-label="Customization" }

!!! desc "Customization"

    This symbol denotes that the thing described is a customization that must be added by the author.
    
### <!-- md:utility --> – Utility { data-toc-label="Utility" }

!!! desc "Utility"

    Besides plugins, there are some utilities that build on top of MkDocs in order to provide extended functionality, like for example support for versioning.
    

