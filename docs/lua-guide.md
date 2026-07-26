---
icon: simple/materialformkdocs
---

<div style="display: none;"><h1>Header</h1></div>

![](imgs/20260724-153731.png){: style="display: block; margin: 0 auto"}
<H1 style="text-align: center;"><ins>lua-guide</ins></H1>

---

![](imgs/20260724-143441.png){: style="display: block; margin: 0 auto"}

<H2 style="text-align: center;"><ins>NVIM REFERENCE MANUAL</ins></H2>
<H3 style="text-align: center;"><ins>Guide to using Lua in Nvim</ins></H3>
                            
!!! desc "Introduction *lua-guide*"
    ### Introduction {.toc-hidden-header}
    This guide introduces the basics of everyday Lua usage for configuring and controlling Nvim. It assumes some familiarity with the (non-Lua) basics of Nvim (commands, options, mappings, autocommands), which are covered in the [user-manual](https://neovim.io/doc/user/usr_toc/#user-manual).
    
    This is not a comprehensive encyclopedia of all available features. Think of it as a survival kit: the bare minimum needed to comfortably get started on using Lua in Nvim.
    
    - See [lua-plugin](https://neovim.io/doc/user/lua-plugin/#lua-plugin) for guidance on developing Lua plugins.
    - See [luaref](https://neovim.io/doc/user/luaref/#luaref) and [lua-concepts](https://neovim.io/doc/user/lua/#lua-concepts) for details on the Lua programming language.
    
---

#### About the API:*`lua-guide-api`* {: data-toc-label="lua-guide-api" }

!!! ex "About the API [*lua-guide-api*](https://neovim.io/doc/user/lua-guide/#lua-guide-api)"

    The purpose of this guide is to introduce the different ways of interacting with Nvim through Lua (the "API"). This API consists of three different layers:
    
    1. The "Vim API" inherited from Vim: [Ex-command](https://neovim.io/doc/user/vimindex/#Ex-command)s and [vimscript-functions](https://neovim.io/doc/user/vimfn/#vimscript-functions) as well as [user-function](https://neovim.io/doc/user/vimeval/#user-function)s in Vimscript. These are accessed through [vim.cmd()](https://neovim.io/doc/user/lua/#vim.cmd()) and [vim.fn](https://neovim.io/doc/user/lua/#vim.fn) respectively, which are discussed under [lua-guide-vimscript](https://neovim.io/doc/user/lua-guide/#lua-guide-vimscript) below.
    
    2. The "Nvim API" written in C for use in remote plugins and GUIs; see |api|. These functions are accessed through |vim.api|.
    
    3. The "Lua API" written in and specifically for Lua. These are any other functions accessible through `vim.*` not mentioned already; see [lua-stdlib](https://neovim.io/doc/user/lua/#lua-stdlib).
    
    ---
    
    This distinction is important, as API functions inherit behavior from their original layer: For example, Nvim API functions always need all arguments to be specified even if Lua itself allows omitting arguments (which are then passed as `nil`); and Vim API functions can use `0`-based indexing even if Lua arrays are 1-indexed by default.
    
    Through this, any possible interaction can be done through Lua without writing a complete new API from scratch. For this reason, functions are usually not duplicated between layers unless there is a significant benefit in functionality or performance (e.g., you can map Lua functions directly through [nvim_create_autocmd()](https://neovim.io/doc/user/api/#nvim_create_autocmd()) but not through [:autocmd](https://neovim.io/doc/user/autocmd/#%3Aautocmd)). In case there are multiple ways of achieving the same thing, this guide will only cover what is most convenient to use from Lua.
    
#### Using Lua:`lua-guide-using-Lua` {: data-toc-label="lua-guide-using-Lua" }

!!! desc "[*lua-guide-using-Lua*](https://neovim.io/doc/user/lua-guide/#lua-guide-using-Lua)"

    To run Lua code from the Nvim command line, use the [:lua](https://neovim.io/doc/user/lua/#%3Alua) command:
    
    !!! abstract ""
        ```vim
        :lua print("Hello!")
        ```
        
    Note: each [:lua](https://neovim.io/doc/user/lua/#%3Alua) command has its own scope and variables declared with the local keyword are not accessible outside of the command. This won't work:
    
    !!! abstract ""
        ```vim
        :lua local foo = 1
        :lua print(foo)
        
        "prints "nil" instead of "1"
        ```
    
    You can also use `:lua=`, which is equivalent to `:lua vim.print(...)`, to conveniently check the value of a variable or a table:
    !!! quote ""
        ```vim
        :lua =package
        ```
    
    To run a Lua script in an external file, you can use the [:source](https://neovim.io/doc/user/repeat/#%3Asource) command exactly like for a Vimscript file:
    
    !!! abstract ""
        ```vim
        :source ~/programs/baz/myluafile.lua
        ```
    
    Finally, you can include Lua code in a Vimscript file by putting it inside a [:lua-heredoc](https://neovim.io/doc/user/lua/#%3Alua-heredoc) block:
    !!! abstract ""
        ```vim
        lua << EOF
          local tbl = {1, 2, 3}
          for k, v in ipairs(tbl) do
            print(v)
          end
        EOF
        ```
    
---

#### Lua cannot normally be interrupted by [CTRL-C:](https://neovim.io/doc/user/various/#CTRL-C)`lua-guide-interrupt` {: data-toc-label="lua-guide-interrupt" }

!!! recommendation "[*lua-guide-interrupt*](https://neovim.io/doc/user/lua-guide/#lua-guide-interrupt)"

    Lua cannot normally be interrupted by [CTRL-C](https://neovim.io/doc/user/various/#CTRL-C) (Lua does not implicitly "yield" to Nvim). To allow the user to interrupt potentially slow loops, periodically call [vim.wait()](https://neovim.io/doc/user/lua/#vim.wait()). Passing `interval=0` skips the dummy timer setup, minimizing per-call overhead in a tight loop:
    
    ```
    while true do
      
      -- ...work...
      local _, code = vim.wait(0, nil, 0)
      if code == -2 then -- CTRL-C.
      
        break
        
      end
    
    end
    ```
    
---

See also: [Issue/6800](https://github.com/neovim/neovim/issues/6800)

---

#### Using Lua files on startup: `lua-guide-config` {: data-toc-label="lua-guide-config" }

!!! important "[*lua-guide-config*](https://neovim.io/doc/user/lua-guide/#lua-guide-config)"

    Nvim supports using `init.vim` or `init.lua` as the configuration file, but not both at the same time. This should be placed in your [config](https://neovim.io/doc/user/starting/#config) directory (run `:echo stdpath('config')` to see where it is). Note that you can also use Lua in `init.vim` and Vimscript in `init.lua`, which will be covered below.
    
    If you'd like to run any other Lua script on [startup](https://neovim.io/doc/user/starting/#startup) automatically, then you can simply put it in `plugin/` in your ['runtimepath'](https://neovim.io/doc/user/options/#'runtimepath').
    
#### Lua Modules:`lua-guide-modules` {: data-toc-label="lua-guide-modules" }

!!! instruction "[*lua-guide-modules*](https://neovim.io/doc/user/lua-guide/#lua-guide-modules)"

    If you want to load Lua files on demand, you can place them in the `lua/` directory in your ['runtimepath'](https://neovim.io/doc/user/options/#'runtimepath') and load them with `require`. (This is the Lua equivalent of Vimscript's [autoload](https://neovim.io/doc/user/userfunc/#autoload) mechanism.)
    
    Let's assume you have the following directory structure:

    :material-folder: **~/.config/nvim**  
    ├── :material-folder: after/  
    ├── :material-folder: ftplugin/  
    ├── :material-folder: lua/  
    │&nbsp;&nbsp;&nbsp;├── :material-language-lua: myluamodule.lua  
    │&nbsp;&nbsp;&nbsp;└── :material-folder: other_modules/  
    │&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── :material-language-lua: anothermodule.lua  
    │&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── :material-language-lua: init.lua  
    ├── :material-folder: plugin/  
    ├── :material-folder: syntax/  
    └── :material-cog-outline: init.vim
    

#### Then the following Lua code will load: `myluamodule.lua` {: data-toc-label="Load myluamodule.lua" }

!!! desc "*`myluamodule.lua`*"

    !!! abstract ""
        ```vim
        require("myluamodule")
        ```
    ---
    
    !!! abstract ""
    
        Note the absence of a `.lua` extension.
    
        Similarly, loading `other_modules/anothermodule.lua` is done via
        
        !!! desc ""
            ```vim
            require('other_modules/anothermodule')
            
            -- or
            
            require('other_modules.anothermodule')
            ```
            
    ---
    
    !!! abstract ""
        Note how "submodules" are just subdirectories; the `.` is equivalent to the path separator `/` (even on Windows).
        
        A folder containing an |init.lua| file can be required directly, without having to specify the name of the file:
        
        !!! desc ""
            ```vim
            require('other_modules') -- loads other_modules/init.lua
            ```
    
!!!desc "*`pcall()`* *`module_with_error`*"
    
    !!! abstract ""
        Requiring a nonexistent module or a module which contains syntax errors aborts the currently executing script. `pcall()` may be used to catch such errors. The following example tries to load the `module_with_error` and only calls one of its functions if this succeeds and prints an error message otherwise:
        
        !!! desc ""
            
            ```vim
            local ok, mymod = pcall(require, 'module_with_error')
            
            if not ok then
            
              print("Module had an error")
            
            else
            
              mymod.func()
            
            end
            ```
    ---
    
    !!! abstract ""
    
        In contrast to [:source](https://neovim.io/doc/user/repeat/#%3Asource), [require()](https://neovim.io/doc/user/luaref/#require()) not only searches through all `lua/` directories under 'runtimepath', it also caches the module on first use. Calling `require()` a second time will therefore _not_ execute the script again and instead return the cached file. To rerun the file, you need to remove it from the cache manually first:
        
        !!! desc ""
        
            ```vim
            package.loaded['myluamodule'] = nil
            require('myluamodule')    -- read and execute the module again from disk
            ```
        
    ---
    
    See also:
    
    • [lua-module-load](https://neovim.io/doc/user/lua/#lua-module-load): how `require()` finds modules
    
    • [pcall()](https://neovim.io/doc/user/luaref/#pcall())
    

#### Using Vim commands and functions from Lua:*`lua-guide-vimscript`* {: data-toc-label="lua-guide-vimscript" }
---

!!! important "*NOTE!*"
    - *All Vim commands and functions are accessible from Lua.*

!!! desc "Vim Commands *`lua-guide-vim-commands`*"

    !!! abstract ""
        To run an arbitrary Vim command from Lua, pass it as a string to |vim.cmd()|:
    
        !!! desc ""
        
            ```vim
            vim.cmd("colorscheme habamax")
            ```
    
    !!! abstract ""
        Note that special characters will need to be escaped with backslashes:
        
        !!! desc ""
        
            ```vim
            vim.cmd("%s/\\Vfoo/bar/g")
            ```
    
    !!! abstract ""
        An alternative is to use a literal string (see [lua-literal](https://neovim.io/doc/user/luaref/#lua-literal)) delimited by double brackets `[[ ]]` as in:
    
        !!! desc ""
        
            ```vim
            vim.cmd([[%s/\Vfoo/bar/g]])
            ```
    
    !!! abstract ""
        Another benefit of using literal strings is that they can be multiple lines; this allows you to pass multiple commands to a single call of |vim.cmd()|:
    
        !!! desc ""
            
            ```vim
            vim.cmd([[
              highlight Error guibg=red
              highlight link Warning Error
            ]])
            ```
        
    !!! abstract ""
        This is the converse of[: lua-heredoc](https://neovim.io/doc/user/lua/#%3Alua-heredoc) and allows you to include Vimscript code in your `init.lua.`
        
        If you want to build your Vim command programmatically, the following form can be useful (all these are equivalent to the corresponding line above):
        
        !!! desc ""
        
            ```vim
            vim.cmd.colorscheme("habamax")
            
            vim.cmd.highlight({ "Error", "guibg=red" })
            
            vim.cmd.highlight({ "link", "Warning", "Error" })
            ```
    
#### Vimscript Functions:*`lua-guide-vim-functions`* {: data-toc-label="lua-guide-vim-functions"  } 

!!! desc "Vimscript Functions:*`lua-guide-vim-functions`*"

    !!! abstract ""
        Use [vim.fn](https://neovim.io/doc/user/lua/#vim.fn) to call Vimscript functions from Lua. Data types between Lua and Vimscript are automatically converted:
    
        !!! desc ""
        
            ```vim
            print(vim.fn.printf('Hello from %s', 'Lua'))
            
            
            local reversed_list = vim.fn.reverse({ 'a', 'b', 'c' })
            vim.print(reversed_list) -- { "c", "b", "a" }
            
            local function print_stdout(chan_id, data, name)
              print(data[1])
            end
            
            vim.fn.jobstart('ls', { on_stdout = print_stdout })
            ```
        
    !!! abstract ""
        This works for both [vimscript-functions](https://neovim.io/doc/user/vimfn/#vimscript-functions) and [user-function](https://neovim.io/doc/user/vimeval/#user-function)s.
        
        Note that hashes (`#`) are not valid characters for identifiers in Lua, so, e.g., |autoload| functions have to be called with this syntax:
        
        !!! desc ""
        
            ```vim
            vim.fn['my#autoload#function']()
            ```
            
    See also:
    • [vimscript-functions](https://neovim.io/doc/user/vimfn/#vimscript-functions): descriptions of all Vimscript functions
    
    • [function-list](https://neovim.io/doc/user/usr_41/#function-list): Vimscript functions grouped by topic
    
    • [:runtime](https://neovim.io/doc/user/repeat/#%3Aruntime): run all Lua scripts matching a pattern in 'runtimepath'
    

#### Variables:*`lua-guide-variables`* {: data-toc-label="lua-guide-variables" }

!!! desc "Variables:*`lua-guide-variables`*"

    Variables can be set and read using the following wrappers, which directly correspond to their [variable-scope](https://neovim.io/doc/user/vimeval/#variable-scope):
    
    • [vim.g](https://neovim.io/doc/user/lua/#vim.g): global variables ([g:](https://neovim.io/doc/user/vimeval/#g%3A))
    • [vim.b](https://neovim.io/doc/user/lua/#vim.b): variables for the current buffer ([b:](https://neovim.io/doc/user/vimeval/#b%3A))
    • [vim.w](https://neovim.io/doc/user/lua/#vim.w): variables for the current window ([w:](https://neovim.io/doc/user/vimeval/#w%3A))
    • [vim.t](https://neovim.io/doc/user/lua/#vim.t): variables for the current tabpage ([t:](https://neovim.io/doc/user/vimeval/#t%3A))
    • [vim.v](https://neovim.io/doc/user/lua/#vim.t): predefined Vim variables ([v:](https://neovim.io/doc/user/vvars/#v%3A))
    • [vim.env](https://neovim.io/doc/user/lua/#vim.env): environment variables defined in the editor session
            
    !!! abstract ""
    
        Data types are converted automatically. For example:
        
        !!! desc ""
            
            ```vim
            vim.g.some_global_variable = {
                key1 = "value",
                key2 = 300
            }
                
                
            vim.print(vim.g.some_global_variable)
                
            --> { key1 = "value", key2 = 300 }
            ```
            
    !!! abstract ""
        You can target specific buffers (via number), windows (via |window-ID|), or tabpages by indexing the wrappers:
        
        !!! desc ""
            
            ```vim
            vim.b[2].myvar = 1               -- set myvar for buffer number 2
            
            vim.w[1005].myothervar = true    -- set myothervar for window ID 1005
            ```
    
    !!! abstract ""
        Some variable names may contain characters that cannot be used for identifiers in Lua. You can still manipulate these variables by using the syntax
        
        !!! desc ""
            
            ```vim
            vim.g['my#variable'] = 1
            ```
                
    !!! abstract ""
        Note that you cannot directly change fields of array variables. This won't work:
        
        !!! desc ""
            
            ```vim
            vim.g.some_global_variable.key2 = 400
            
            vim.print(vim.g.some_global_variable)
            
            --> { key1 = "value", key2 = 300 }
            ```
            
    !!! abstract ""
        Instead, you need to create an intermediate Lua table and change this:
        
        !!!desc ""
            
            ```vim
            local temp_table = vim.g.some_global_variable
            
            temp_table.key2 = 400
            
            vim.g.some_global_variable = temp_table
            
            vim.print(vim.g.some_global_variable)
                
            --> { key1 = "value", key2 = 400 }
            ```
                
    !!! abstract ""
    
        To delete a variable, simply set it to `nil`:
            
        !!!desc ""
            
            ```vim
            vim.g.myvar = nil
            ```
                
    See also:
    
    • [lua-vim-variables](https://neovim.io/doc/user/lua/#lua-vim-variables)
    

#### Options:*`lua-guide-options`* {: data-toc-label="lua-guide-options" }

!!! desc "*`lua-guide-options`*"

    There are two complementary ways of setting [options](https://neovim.io/doc/user/options/#options) via Lua.
    
    !!! abstract "*`vim.opt`*"
    
        The most convenient way for setting global and local options, e.g., in `init.lua`, is through `vim.opt` and friends:
        
        !!!desc ""
        
            • [vim.opt](https://neovim.io/doc/user/lua/#vim.opt): behaves like [:set](https://neovim.io/doc/user/options/#%3Aset)
            • [vim.opt_global](https://neovim.io/doc/user/lua/#vim.opt_global): behaves like [:setglobal](https://neovim.io/doc/user/options/#%3Asetglobal)
            • [vim.opt_local](https://neovim.io/doc/user/lua/#vim.opt_local):  behaves like [:setlocal](https://neovim.io/doc/user/options/#%3Asetlocal)
            
    !!! abstract ""
    
        For example, the Vimscript commands:
        
        !!! desc ""
        
            ```vim
            set smarttab
            
            set nosmarttab
            ```
            
    !!! abstract ""
    
        Are equivalent to:
        
        !!! desc ""
            
            ```vim
            vim.opt.smarttab = true
            
            vim.opt.smarttab = false
            ```
        
    !!! abstract ""
        In particular, they allow an easy way to working with list-like, map-like, and set-like options through Lua tables: Instead of:
        
        !!! desc ""
        
            ```vim
            set wildignore=*.o,*.a,__pycache__
            
            set listchars=space:_,tab:>~
            
            set formatoptions=njt
            ```
            
    !!! abstract ""
    
        You can use:
        
        !!! desc ""
        
            ```vim
            vim.opt.wildignore = { '*.o', '*.a', '__pycache__' }
            
            vim.opt.listchars = { space = '_', tab = '>~' }
            
            vim.opt.formatoptions = { n = true, j = true, t = true }
            ```
            
    !!! abstract ""
    
        These wrappers also come with methods that work similarly to their [:set+=](https://neovim.io/doc/user/options/#%3Aset%2B%3D), [:set^=](https://neovim.io/doc/user/options/#%3Aset%5E%3D) and [:set-=](https://neovim.io/doc/user/options/#%3Aset-%3D) counterparts in Vimscript:
        
        !!! desc ""
        
            ```vim
            vim.opt.shortmess:append({ I = true })
            
            vim.opt.wildignore:prepend('*.o')
            
            vim.opt.whichwrap:remove({ 'b', 's' })
            ```
            
    !!! abstract ""
    
        The price to pay is that you cannot access the option values directly but must use [vim.opt:get()](https://neovim.io/doc/user/lua/#vim.opt%3Aget()):
        
        !!! desc ""
        
            ```vim
            print(vim.opt.smarttab)
            
            --> {...} (big table)
            
            print(vim.opt.smarttab:get())
            
            --> false
            
            vim.print(vim.opt.listchars:get())
            
            --> { space = '_', tab = '>~' }
            ```
            
!!! desc "*`vim.o`*"

    For this reason, there exists a more direct variable-like access using `vim.o` and friends, similarly to how you can get and set options via `:echo &number` and `:let &listchars='space:_,tab:>~'`:
    
    !!! abstract ""
        • [vim.o](https://neovim.io/doc/user/lua/#vim.o):  behaves like [:set](https://neovim.io/doc/user/options/#%3Aset)
        • [vim.go](https://neovim.io/doc/user/lua/#vim.go): behaves like [:setglobal](https://neovim.io/doc/user/options/#%3Asetglobal)
        • [vim.bo](https://neovim.io/doc/user/lua/#vim.bo): for buffer-scoped options
        • [vim.wo](https://neovim.io/doc/user/lua/#vim.wo): for window-scoped options (can be double indexed)
        
    !!! abstract ""
        For example:
        
        !!! desc ""
        
            ```vim
            vim.o.smarttab = false -- :set nosmarttab
            
            print(vim.o.smarttab)
            
            --> false
            
            vim.o.listchars = 'space:_,tab:>~' -- :set listchars='space:_,tab:>~'
            
            print(vim.o.listchars)
            
            --> 'space:_,tab:>~'
            
            vim.o.isfname = vim.o.isfname .. ',@-@' -- :set isfname+=@-@
            
            print(vim.o.isfname)
            
            --> '@,48-57,/,.,-,_,+,,,#,$,%,~,=,@-@'
            
            vim.bo.shiftwidth = 4 -- :setlocal shiftwidth=4
            
            print(vim.bo.shiftwidth)
            
            --> 4
            ```
            
    !!! abstract ""
    
        Just like variables, you can specify a buffer number or [window-ID](https://neovim.io/doc/user/windows/#window-ID) for buffer and window options, respectively. If no number is given, the current buffer or window is used:
        
        !!! desc ""
            
            ```vim
            vim.bo[4].expandtab = true  -- sets expandtab to true in buffer 4
                
            vim.wo.number = true        -- sets number to true in current window
                
            vim.wo[0].number = true     -- same as above
                
            vim.wo[0].number = true     -- sets number to true in current buffer
                
                                        -- in current window only
                
            print(vim.wo[].number)      --> true
            ```
    
    !!! abstract ""
        See also:
         
        !!! desc ""
        
            • [lua-options](https://neovim.io/doc/user/lua/#lua-options)
             

#### Mappings:*`lua-guide-mappings`* {: data-toc-label="lua-guide-mappings" }

!!! desc "Mappings:*`lua-guide-mappings`*"

    !!!abstract ""
        You can map either Vim commands or Lua functions to key sequences.
        
#### Creating Mappings: *`lua-guide-mappings-set`* {: data-toc-label="lua-guide-mappings-set" }

!!! desc "*`lua-guide-mappings-set`*"

    !!! abstract ""
        Mappings can be created using [vim.keymap.set()](https://neovim.io/doc/user/lua/#vim.keymap.set()). This function takes three mandatory arguments:
    
        • {mode} is a string or a table of strings containing the mode prefix for which the mapping will take effect. The prefixes are the ones listed in [:map-modes](https://neovim.io/doc/user/map/#%3Amap-modes), or "!" for [:map!](https://neovim.io/doc/user/map/#%3Amap%21), or empty string for [:map](https://neovim.io/doc/user/map/#%3Amap).
    
        • {lhs} is a string with the key sequences that should trigger the mapping.
    
        • {rhs} is either a string with a Vim command or a Lua function that should be executed when the {lhs} is entered.  An empty string is equivalent to [<Nop>](https://neovim.io/doc/user/intro/#%3CNop%3E), which disables a key.
    
        !!! desc ""
            
            Examples:
            
            ```vim
            -- Normal mode mapping for Vim command
            
            vim.keymap.set('n', '<Leader>ex1', '<cmd>echo "Example 1"<cr>')
            
            -- Normal and Command-line mode mapping for Vim command
            
            vim.keymap.set({'n', 'c'}, '<Leader>ex2', '<cmd>echo "Example 2"<cr>')
            
            -- Normal mode mapping for Lua function
            
            vim.keymap.set('n', '<Leader>ex3', vim.treesitter.start)
            
            -- Normal mode mapping for Lua function with arguments
            
            vim.keymap.set('n', '<Leader>ex4', function() print('Example 4') end)
            ```
            
    !!! abstract ""
        You can map functions from Lua modules via:
        
        !!! desc ""
        
            ```vim
            vim.keymap.set('n', '<Leader>pl1', require('plugin').action)
            ```
            
    !!! abstract ""
        Note that this loads the plugin at the time the mapping is defined. If you want to defer the loading to the time when the mapping is executed (as for [autoload](https://neovim.io/doc/user/userfunc/#autoload) functions), wrap it in `function() end`:
        
        !!! desc ""
        
            ```vim
            vim.keymap.set('n', '<Leader>pl2', function() require('plugin').action() end)
            ```
            
    !!! abstract ""
        The fourth, optional, argument is a table with keys that modify the behavior of the mapping such as those from [:map-arguments](https://neovim.io/doc/user/map/#%3Amap-arguments). The following are the most useful options:
        
        • `buf`: If given, only set the mapping for the buffer with the specified number; `0` or `true` means the current buffer.
        
        !!! desc ""
        
            ```vim
            -- set mapping for the current buffer
            
            vim.keymap.set('n', '<Leader>pl1', require('plugin').action, { buf = 0 })
            
            -- set mapping for the buffer number 4
            
            vim.keymap.set('n', '<Leader>pl1', require('plugin').action, { buf = 4 })
            ```
            
    !!! abstract ""
    
        • `silent`: If set to `true`, suppress output such as error messages.
        
        !!! desc ""
        
            ```vim
            vim.keymap.set('n', '<Leader>pl1', require('plugin').action, { silent = true })
            ```
            
    !!! abstract ""
    
        • `expr`: If set to `true`, do not execute the {rhs} but use the return value as input. Special [keycodes](https://neovim.io/doc/user/intro/#keycodes) are converted automatically. For example, the following mapping replaces <down> with <c-n> in the popupmenu only:
        
        !!! desc ""
        
            ```vim
            vim.keymap.set('c', '<down>', function()
            
              if vim.fn.pumvisible() == 1 then return '<c-n>' end
            
              return '<down>'
            
            end, { expr = true })
            ```
            
    !!! abstract ""
        `desc`: A string that is shown when listing mappings with, e.g., [:map](https://neovim.io/doc/user/map/#%3Amap). This is useful since Lua functions as {rhs} are otherwise only listed as `Lua: <number> <source file>:<line>`. Plugins should therefore always use this for mappings they create.
        
        !!! desc ""
        
            ```vim
            vim.keymap.set('n', '<Leader>pl1', require('plugin').action,
            
              { desc = 'Execute action from plugin' })
            ```
              
    !!! abstract ""
    
        • `remap`: By default, all mappings are nonrecursive (i.e., [vim.keymap.set()](https://neovim.io/doc/user/lua/#vim.keymap.set()) behaves like [:noremap](https://neovim.io/doc/user/map/#%3Anoremap)). If the {rhs} is itself a mapping that should be executed, set `remap = true`: 
        
        !!! desc ""
        
            ```vim
            vim.keymap.set('n', '<Leader>ex1', '<cmd>echo "Example 1"<cr>')
            
            -- add a shorter mapping
            
            vim.keymap.set('n', 'e', '<Leader>ex1', { remap = true })
            ```
            
    !!! abstract ""
    
        Note: [<Plug>](https://neovim.io/doc/user/map/#%3CPlug%3E) mappings are always expanded even with the default `remap = false`:
        
        !!! desc ""
            
            ```vim
            vim.keymap.set('n', '[%', '<Plug>(MatchitNormalMultiBackward)')
            ```
            
#### Removing mappings *`lua-guide-mappings-del`* {: data-toc-label="lua-guide-mappings-del" }

!!! desc " Removing mappings *`lua-guide-mappings-del`*"

    !!! abstract ""
    
        A specific mapping can be removed with |vim.keymap.del()|:
        
        !!! desc ""
         
            ```vim
            vim.keymap.del('n', '<Leader>ex1')
                 
            vim.keymap.del({'n', 'c'}, '<Leader>ex2', { buf = 0 })
            ```
                
    !!! abstract ""
    
        See also:
        • `vim.api.`[nvim_get_keymap()](https://neovim.io/doc/user/api/#nvim_get_keymap()): return all global mapping
        • `vim.api.`[nvim_buf_get_keymap()](https://neovim.io/doc/user/api/#nvim_buf_get_keymap()): return all mappings for buffer
        

#### Autocommands *`lua-guide-autocommands`*  {: data-toc-label="lua-guide-autocommands" }

!!! desc "*`lua-guide-autocommands`*"

    !!! abstract ""
        An [autocommand](https://neovim.io/doc/user/autocmd/#autocommand) is a Vim command or a Lua function that is automatically executed whenever one or more [events](https://neovim.io/doc/user/autocmd/#events) are triggered, e.g., when a file is read or written, or when a window is created. These are accessible from Lua through the Nvim API.
        
---

#### Creating autocommands *`lua-guide-autocommand-create`* {: data-toc-label="lua-guide-autocommand-create" }

!!! desc "*`lua-guide-autocommand-create`*"

    !!! abstract ""
        Autocommands are created using `vim.api.`[nvim_create_autocmd()](https://neovim.io/doc/user/api/#nvim_create_autocmd()), which takes two mandatory arguments:
        
        • {event}: a string or table of strings containing the event(s) which should trigger the command or function.
        
        • {opts}:  a table with keys that control what should happen when the event(s) are triggered.
        
        The most important options are:
        
        • `pattern`:  A string or table of strings containing the [autocmd-pattern](https://neovim.io/doc/user/autocmd/#autocmd-pattern).
        Note: Environment variable like `$HOME` and `~` are not automatically expanded; you need to explicitly use `vim.fn.`[expand()](https://neovim.io/doc/user/vimfn/#expand()) for this.
        
        • `command`:  A string containing a Vim command.
        
        • `callback`: A Lua function.
        
        You must specify one and only one of `command` and `callback`. If `pattern` is omitted, it defaults to `pattern = '*'`.
        
    !!! abstract ""
        Examples:
        
        !!! desc ""
        
            ```vim
            vim.api.nvim_create_autocmd({"BufEnter", "BufWinEnter"}, {
              pattern = {"*.c", "*.h"},
              command = "echo 'Entering a C or C++ file'",
            })
            ```
            
        ---
        
        !!! desc ""
        
            ```vim
            -- Same autocommand written with a Lua function instead
            
            vim.api.nvim_create_autocmd({"BufEnter", "BufWinEnter"}, {
              pattern = {"*.c", "*.h"},
              callback = function() print("Entering a C or C++ file") end,
            })
            ```
            
        ---
        
            
        !!! desc ""
        
            ```vim
            -- User event triggered by MyPlugin
            
            vim.api.nvim_create_autocmd("User", {
              pattern = "MyPlugin",
              callback = function() print("My Plugin Works!") end,
            })
            ```
             
    
    !!! abstract ""
    
        Nvim will always call a Lua function with a single table containing information about the triggered autocommand. The most useful keys are:
        
        • `match`: a string that matched the `pattern` (see [`<amatch>`](https://neovim.io/doc/user/cmdline/#%3Camatch%3E))
        
        • `buf`:   the number of the buffer the event was triggered in (see [`<abuf>`](https://neovim.io/doc/user/cmdline/#%3Cabuf%3E))
        
        • `file`:  the file name of the buffer the event was triggered in (see [`<afile>`](https://neovim.io/doc/user/cmdline/#%3Cafile%3E))
        
        • `data`:  a table with other relevant data that is passed for some events
        
        !!! desc ""
            For example, this allows you to set buffer-local mappings for some filetypes:
            
            ```vim
            vim.api.nvim_create_autocmd("FileType", {
              pattern = "lua",
              callback = function(ev)
            vim.keymap.set('n', 'K', vim.lsp.buf.hover, { buf = ev.buf })
            end
            })
            ```
            
    !!! abstract ""
    
        This means that if your callback itself takes an (even optional) argument, you must wrap it in `function() end` to avoid an error:
        
        !!! desc ""
            
            ```vim
            vim.api.nvim_create_autocmd('TextYankPost', {
             
              callback = function() vim.hl.hl_op() end
            })
            ```
            
    !!! abstract ""
    
        (Since unused arguments can be omitted in Lua function definitions, this is equivalent to `function(args) ... end`.)
        
        Instead of using a pattern, you can create a buffer-local autocommand (see [autocmd-buflocal](https://neovim.io/doc/user/autocmd/#autocmd-buflocal)) with `buffer`; in this case, `pattern` cannot be used:
        
        !!! desc ""
            
            ```vim
            -- set autocommand for current buffer
            
            vim.api.nvim_create_autocmd("CursorHold", {
              buffer = 0,
              callback = function() print("hold") end,
            })
            ```
            
        ---
        
        !!! desc ""
        
            ```vim
            -- set autocommand for buffer number 33
            
            vim.api.nvim_create_autocmd("CursorHold", {
              buffer = 33,
              callback = function() print("hold") end,
            })
            ```
            
    !!! abstract ""
    
        Similarly to mappings, you can (and should) add a description using `desc`:
        
        !!! desc ""
            
            ```vim
            vim.api.nvim_create_autocmd('TextYankPost', {
              callback = function() vim.hl.hl_op() end,
              desc = "Briefly highlight yanked text"
            })
            ```
            
    !!! abstract ""
        Finally, you can group autocommands using the `group` key; this will be covered in detail in the next section.
        
#### Grouping autocommands *`lua-guide-autocommands-group`* {: data-toc-label="lua-guide-autocommands-group" }

!!! desc "*`lua-guide-autocommands-group`*"

    !!! abstract ""
        Autocommand groups can be used to group related autocommands together; see [autocmd-groups](https://neovim.io/doc/user/autocmd/#autocmd-groups). This is useful for organizing autocommands and especially for preventing autocommands to be set multiple times.
    
        Groups can be created with `vim.api.`|nvim_create_augroup()|. This function takes two mandatory arguments: a string with the name of a group and a table determining whether the group should be cleared (i.e., all grouped autocommands removed) if it already exists. The function returns a number that is the internal identifier of the group. Groups can be specified either by this identifier or by the name (but only if the group has been created first).
        
        !!! desc ""
            
            For example, a common Vimscript pattern for autocommands defined in files that may be reloaded is:
            
            ```vim
            augroup vimrc
            
              " Remove all vimrc autocommands
              
              autocmd!
              
              au BufNewFile,BufRead *.html set shiftwidth=4
              
              au BufNewFile,BufRead *.html set expandtab
              
            augroup END
            ```
            
    !!! abstract ""
    
        This is equivalent to the following Lua code:
        
        !!! desc ""
        
            ```lua
            local mygroup = vim.api.nvim_create_augroup('vimrc', { clear = true })
            
            vim.api.nvim_create_autocmd({ 'BufNewFile', 'BufRead' }, {
            
              pattern = '*.html',
              group = mygroup,
              command = 'set shiftwidth=4',
              
            })
            
            vim.api.nvim_create_autocmd({ 'BufNewFile', 'BufRead' }, {
              
              pattern = '*.html',
            
              group = 'vimrc',  -- equivalent to group=mygroup
            
            command = 'set expandtab',
            
            })
            ```
            
    !!! abstract ""
    
        Autocommand groups are unique for a given name, so you can reuse them, e.g., in a different file:
        
        !!! desc ""
        
            ```lua
            local mygroup = vim.api.nvim_create_augroup('vimrc', { clear = false })
            
            vim.api.nvim_create_autocmd({ 'BufNewFile', 'BufRead' }, {
              
              pattern = '*.c',
              
              group = mygroup,
              
              command = 'set noexpandtab',
              
            })
            ```
    
#### Deleting autocommands *`lua-guide-autocommands-delete`* {: data-toc-label="lua-guide-autocommands-delete" }

!!! desc " *`lua-guide-autocommands-delete`*"

    !!! abstract ""
        You can use `vim.api.`|nvim_clear_autocmds()| to remove autocommands. This function takes a single mandatory argument that is a table of keys describing the autocommands that are to be removed:
    
    !!! desc ""
    
        ```lua
        -- Delete all BufEnter and InsertLeave autocommands
        
        vim.api.nvim_clear_autocmds({event = {"BufEnter", "InsertLeave"}})
        
        
        -- Delete all autocommands that uses "*.py" pattern
        
        vim.api.nvim_clear_autocmds({pattern = "*.py"})
        
        
        -- Delete all autocommands in group "scala"
         
        vim.api.nvim_clear_autocmds({group = "scala"})
        
        
        -- Delete all ColorScheme autocommands in current buffer
        
        vim.api.nvim_clear_autocmds({event = "ColorScheme", buffer = 0 })
        ```
        
    !!! abstract ""
    
        Note: Autocommands in groups will only be removed if the `group` key is specified, even if another option matches it.
        
        See also:
        
        • [nvim_get_autocmds()](https://neovim.io/doc/user/api/#nvim_get_autocmds()):  return all matching autocommands
        
        • [nvim_exec_autocmds()](https://neovim.io/doc/user/api/#nvim_exec_autocmds()): execute all matching autocommands
        

#### User commands *`lua-guide-commands`* {: data-toc-label="lua-guide-commands" }

!!! desc "*`lua-guide-commands`*"

    !!! abstract ""
    
        [user-commands](https://neovim.io/doc/user/map/#user-commands) are custom Vim commands that call a Vimscript or Lua function. Just like built-in commands, they can have arguments, act on ranges, or have custom completion of arguments. As these are most useful for plugins, we will cover only the basics of this advanced topic.
        
#### Creating user commands *`lua-guide-commands-create`* {: data-toc-label="lua-guide-commands-create" }

!!! desc "*`lua-guide-commands-create`*"

    !!! abstract ""
    
        User commands can be created via [nvim_create_user_command()](https://neovim.io/doc/user/api/#nvim_create_user_command()). This function takes three mandatory arguments:
        
        • a string that is the name of the command (which must start with an uppercase letter to distinguish it from builtin commands);
        
        • a string containing Vim commands or a Lua function that is executed when the command is invoked;
        
        • a table with [command-attributes](https://neovim.io/doc/user/map/#command-attributes); in addition, it can contain the keys `desc` (a string describing the command); `force` (set to `false` to avoid replacing an already existing command with the same name), and `preview` (a  Lua function that is used for [:command-preview](https://neovim.io/doc/user/map/#%3Acommand-preview)).
        
        !!! desc ""
        
            Example:
            
            ```lua
            vim.api.nvim_create_user_command('Test', 'echo "It works!"')
            
            vim.cmd.Test()
            
            --> It works!
            ```
                
    !!! abstract ""
    
        (Note that the third argument is mandatory even if no attributes are given.)
        
        Lua functions are called with a single table argument containing arguments and modifiers. The most important are:
        
        • `name`: a string with the command name
        • `fargs`: a table containing the command arguments split by whitespace (see [`<f-args>`](https://neovim.io/doc/user/map/#%3Cf-args%3E))
        • `bang`: `true` if the command was executed with a `!` modifier (see [`<bang>`](https://neovim.io/doc/user/map/#%3Cbang%3E))
        • `line1`: the starting line number of the command range (see [`<line1>`](https://neovim.io/doc/user/map/#%3Cline1%3E))
        • `line2`: the final line number of the command range (see [`<line2>`](https://neovim.io/doc/user/map/#%3Cline2%3E))
        • `range`: the number of items in the command range: 0, 1, or 2 (see [`<range>`](https://neovim.io/doc/user/map/#%3Crange%3E))
        • `count`: any count supplied (see [`<count>`]( https://neovim.io/doc/user/map/#%3Ccount%3E))
        • `smods`: a table containing the command modifiers (see [`<mods>`](https://neovim.io/doc/user/map/#%3Cmods%3E))
        
           
        !!! desc ""
        
            For example:
            
            ```lua
            vim.api.nvim_create_user_command('Upper',
              
              function(opts)
              
                print(string.upper(opts.fargs[1]))
                
              end,
              
              { nargs = 1 })
              
            vim.cmd.Upper('foo')
            
            --> FOO
            ```
            
    !!! abstract ""
    
        The `complete` attribute can take a Lua function in addition to the attributes listed in [:command-complete](https://neovim.io/doc/user/map/#%3Acommand-complete).
        
        !!! desc ""
        
            ```lua
            
            vim.api.nvim_create_user_command('Upper',
            
              function(opts)
                
                print(string.upper(opts.fargs[1]))
                
              end,
              
              { nargs = 1,
              
                complete = function(ArgLead, CmdLine, CursorPos)
                
                  -- return completion candidates as a list-like table
                  
                  return { "foo", "bar", "baz" }
                  
                end,
                
            })
            ```
            
    !!! abstract ""
    
        Buffer-local user commands are created with `vim.api.`[nvim_buf_create_user_command()](https://neovim.io/doc/user/api/#nvim_buf_create_user_command()). Here the first argument is the buffer number (`0` being the current buffer); the remaining arguments are the same as for [nvim_create_user_command()](https://neovim.io/doc/user/api/#nvim_create_user_command()):
        
        !!! desc ""
        
            ```lua
            vim.api.nvim_buf_create_user_command(, 'Upper',
            
              function(opts)
            
              print(string.upper(opts.fargs[1]))
              
            end,
              
            { nargs = 1 })
            ```
            
#### Deleting user commands *`lua-guide-commands-delete`* {: data-toc-label="lua-guide-commands-delete" }

!!! desc "*`lua-guide-commands-delete`*"

    !!! abstract ""
    
        User commands can be deleted with `vim.api.`[nvim_del_user_command()](https://neovim.io/doc/user/api/#nvim_del_user_command()). The only argument is the name of the command:
        
        !!! desc ""
        
        ```lua
        vim.api.nvim_del_user_command('Upper')
        ```
        
    !!! abstract ""
    
        To delete buffer-local user commands use `vim.api.`[nvim_buf_del_user_command()](https://neovim.io/doc/user/api/#nvim_buf_del_user_command()). Here the first argument is the buffer number (`0` being the current buffer), and second is command name:
        
        !!! desc ""
        
        ```lua
        vim.api.nvim_buf_del_user_command(4, 'Upper')
        ```
        
#### Credits *`lua-guide-credits`* {: data-toc-label="lua-guide-credits" }

!!! desc "*`lua-guide-credits`*"

    !!! abstract ""
    
        This guide is in large part taken from nanotee's Lua guide:
        
        [nanotee lua guide](https://github.com/nanotee/nvim-lua-guide)
        
        Thank you @nanotee!
        
        vim:tw=78:ts=8:sw=4:sts=4:et:ft=help:norl:
        

