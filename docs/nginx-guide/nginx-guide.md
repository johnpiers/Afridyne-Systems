---
icon: simple/nginx
---

<div style="display: none;"><h1>nginx-guide</h1></div>

![](../imgs/nginx-guide.png){: style="display: block; margin: 0 auto"}

## NGINX on Arch Linux: A Plain-English Guide { .centered }

!!! desc "NGINX on Arch Linux"

    This guide shows you how to set up NGINX on Arch Linux for two jobs: **testing websites on your own computer**, and **acting as a reverse proxy** in front of an app you are running. Every step was tested on a real Arch machine, including the problems we ran into along the way.
    
### What is NGINX?

!!! education "What is NGINX?"

    NGINX (say "engine-x") is a web server. When your browser asks for a web page, a web server is the program that answers.
    
    It can do two jobs that matter here:
    
    - **Serve files.** You put a web page in a folder, and NGINX hands it to the browser.
    
    - **Reverse proxy.** NGINX sits in front of another program (for example a documentation site or a small app) and passes requests on to it. Visitors talk to NGINX, and NGINX talks to your app. This gives you clean addresses (`http://docs.test` instead of `http://127.0.0.1:8000`) and one central place for settings.
    
!!! info "Two words you will see a lot"
    - **Port:** a numbered door on your computer. Web pages normally use port 80. Only one program can use a given port at a time.
    - **Config file:** a plain text file of instructions that tells NGINX what to do.

### Before you start

!!! instruction "Before you start"

    You need:
    
    - Arch Linux with `sudo` access
    
    - A terminal
    
    Throughout this guide, lines starting with `sudo` need administrator rights, and you will be asked for your password.
    
## Step 1: Install NGINX

!!! assumption "Install NGINX"

    ```
    sudo pacman -S nginx
    ```
    
    Some optional extras exist (`nginx-mod-stream`, `nginx-mod-image-filter` and others). You do not need any of them for this guide.
    
## Step 2: Make sure nothing else is using port 80

!!! important "Nothing else is allowed on port 80"

    If another web server is already running, NGINX cannot start. A common culprit is Apache (`httpd`). Check what is listening on port 80:
    
    ```
    sudo ss -tlnp | grep ':80 '
    ```
    
    - **No output** means port 80 is free. Go to Step 3.
    
    - **Output mentioning `httpd`** means Apache is running. If you do not use it, stop it and stop it starting at boot:
    
    ```
    sudo systemctl disable --now httpd
    ```
    
    !!! tip "Stop it, don't uninstall it!"
    
        Other packages (such as GNOME's file sharing) can depend on Apache. Stopping and disabling it is safe and easy to undo. Removing it can pull out other things you want.
        
        - **Output mentioning something else** means that program is holding the port. Work out whether you need it before changing anything.
        
## Step 3: Start NGINX with systemd

!!! recommendation "Start NGINX with systemd"

    On Arch you control NGINX through `systemctl`, not by typing `nginx` yourself.
    
    ```
    sudo systemctl start nginx
    systemctl is-active nginx
    curl -I http://localhost
    ```
    
    You want to see `active`, then `HTTP/1.1 200 OK` with a `Server: nginx` line. You can also open `http://localhost` in a browser to see the NGINX welcome page.
    
    To make NGINX start every time you boot:
    
    ```
    sudo systemctl enable nginx
    ```
    
    To undo that later: `sudo systemctl disable nginx`.
    
    ```
    sudo systemctl disable nginx
    ```
    
### The golden habit: edit, test, reload

!!! desc "Edit, Test, Reload"

    Whenever you change a config file, do these three things in this order:
        
    **1. Edit** the file.
        
    **2. Test** it with `sudo nginx -t`. This checks for mistakes without touching the running server.
        
    ```
    sudo nginx -t
    ```
        
    **3. Reload** with `sudo systemctl reload nginx`. This applies the change without dropping connections.
        
    ```
    sudo systemctl reload nginx
    ```
    
!!! warning "Never skip the test"
    If the test reports an error, the running server is not affected. NGINX keeps using the old, working settings until you fix the file and reload.

## Step 4: Tidy up the main config

!!! deep-dive "Tidy up the main config"

    The main config file is `/etc/nginx/nginx.conf`. Back it up first:
    
    ```
    sudo cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak
    ```
    
### Fix the "types_hash" warning

!!! deep-dive "Fix the "types_hash" warning"

    On a fresh Arch install, `sudo nginx -t` prints a harmless warning about `types_hash`. To remove it, add one line inside the `http { ... }` block, right after the `default_type` line:
    
    
    ```
    types_hash_max_size 4096;
    ```
    
### Let NGINX read small per-site files

!!! decision "Let NGINX read small per-site files"

    It is much tidier to keep each site in its own small file than to pile everything into `nginx.conf`. Create a folder for them and add one more line, directly under the line you just added:
    
    ```
    sudo mkdir -p /etc/nginx/conf.d
    ```
    
    ```
    include /etc/nginx/conf.d/*.conf;
    ```
    
    !!! tip "Making these edits"
        Use any editor with `sudo`, for example `sudo nano /etc/nginx/nginx.conf`. The surrounding lines should look like this when you are done:
        
        ```
        http {
            include       mime.types;
            default_type  application/octet-stream;
            types_hash_max_size 4096;
            include /etc/nginx/conf.d/*.conf;
        ```
        
### Choose what answers unknown names

!!! assumption "Choose what answers unknown names"

    When a request arrives for a name that matches none of your sites, NGINX has to pick one to answer it. Rather than leave that to chance, tell it which. In the `server { ... }` block for `localhost`, change:
        
    ```
            listen       80;
    ```
    
    to:
    
    ```
            listen       80 default_server;
    ```
    
    Now test and reload:
    
    ```
    sudo nginx -t
    sudo systemctl reload nginx
    ```
    
    You should see `syntax is ok` and `test is successful`, with no warnings.
    
## Step 5: A local test site

!!! desc "A local test site"

    Goal: open `http://mysite.test` in your browser and see your own page.
    
    **1. Make a folder and a page.** We use `/srv/www` rather than your home folder, because NGINX often cannot read inside home folders and shows a confusing "403 Forbidden" error.
    
    ```
    sudo mkdir -p /srv/www/mysite
    sudo chown $USER: /srv/www/mysite
    echo '<h1>mysite.test is working</h1>' > /srv/www/mysite/index.html
    ```
    
    **2. Create the site's config file:**
    
    ```
    sudo tee /etc/nginx/conf.d/mysite.conf > /dev/null <<'EOF'
    server {
        listen 80;
        server_name mysite.test;
        root /srv/www/mysite;
        index index.html;
    }
    EOF
    ```
    
    This says: when someone asks for `mysite.test`, serve the files from that folder.
    
    **3. Point the name at your own computer.** The file `/etc/hosts` is your computer's private address book:
    
    ```
    echo '127.0.0.1 mysite.test' | sudo tee -a /etc/hosts
    ```
    
    !!! info "Why `.test` ?"
        The ending `.test` is reserved for testing and can never clash with a real website. Avoid endings like `.com` for fake local names.
        
        **4. Test, reload, and check:**
        
        ```
        sudo nginx -t
        sudo systemctl reload nginx
        curl http://mysite.test
        ```
        
        You should see your heading. Open `http://mysite.test` in a browser too. The "Not secure" label is normal because this is plain HTTP on your own machine.
        
## Step 6: A reverse proxy

!!! desc "A reverse proxy"

    Goal: open `http://docs.test` and have NGINX pass the request to an app running on your computer. The example uses a documentation site served by `mkdocs serve` on port 8000, but any app on any port works the same way.
    
    **1. Start your app** and note its port. Check that it answers directly:
    
    ```
    curl -I http://127.0.0.1:8000
    ```
    
    **2. Create the proxy config.** Change `8000` to your app's port:
    
    ```
    sudo tee /etc/nginx/conf.d/docs.conf > /dev/null <<'EOF'
    server {
        listen 80;
        server_name docs.test;
    
        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
    
            # keeps live-reload style connections from being cut off
            proxy_http_version 1.1;
            proxy_buffering off;
            proxy_read_timeout 1h;
        }
    }
    EOF
    ```
    
    What the main lines do:
    
    | Line | Meaning |
    |------|---------|
    | `proxy_pass` | Hand every request to the app on this address |
    | `proxy_set_header ...` | Pass along the original name and visitor details, which most apps want |
    | Last three lines | Allow long-lived connections, such as a page that refreshes itself when you edit a file |
    
    **3. Add the name to your address book, then test and reload:**
    
    ```
    echo '127.0.0.1 docs.test' | sudo tee -a /etc/hosts
    sudo nginx -t
    sudo systemctl reload nginx
    curl -I http://docs.test
    ```
    
    You should get a normal response, with `Server: nginx` in it, showing that NGINX is relaying your app's answer. Open `http://docs.test` in a browser.
    
    !!! tip "Redirects are normal"
        Some apps redirect `/` to another path. If you see `302 Found`, the proxy is working. The app is simply sending you to its real home page.
        
### Where things live

!!! desc "Where things live"

    | What | Where |
    |------|---------|
    | Main config | ``` \
    |  | /etc/nginx/nginx.conf \
    |  | ``` |
    | Your per-site configs | ``` \
    |  | /etc/nginx/conf.d/*.conf \
    |  | ``` |
    | Test site files | ``` \
    |  | /srv/www/ \
    |  | ``` |
    | Name-to-address book | ``` \
    |  | /etc/hosts \
    |  | ``` |
    | Error log | ``` \
    |  | sudo journalctl -u nginx \
    |  | ``` |
    
### Everyday commands

!!! desc "Everyday commands"

    <div class="no-sort" markdown>
    
    | Task | Command |
    |------|---------|
    | Check config for mistakes | ``` \
    |  | sudo nginx -t \
    |  | ``` |
    | Apply config changes | ``` \
    |  | sudo systemctl reload nginx \
    |  | ``` |
    | Start nginx | ``` \
    |  | sudo systemctl start nginx \
    |  | ``` |
    | Stop nginx | ``` \
    |  | sudo systemctl stop nginx \
    |  | ``` |
    | Restart nginx | ``` \
    |  | sudo systemctl restart nginx \
    |  | ``` |
    | Is it running? | ``` \
    |  | systemctl status nginx --no-pager \
    |  | ``` |
    | Start at boot | ``` \
    |  | sudo systemctl enable nginx \
    |  | ``` |
    | Don't start at boot | ``` \
    |  | sudo systemctl disable nginx \
    |  | ``` |
    | See what is using a port | ``` \
    |  | sudo ss -tlnp 'sport = :80' \
    |  | ``` |
    | Show the full merged config | ``` \
    |  | sudo nginx -T \
    |  | ``` |
    
    </div>
    
### Troubleshooting

!!! ex "Troubleshooting"

    **"bind() to 0.0.0.0:80 failed (98: Address already in use)"**
    Another program is using port 80. Find it with `sudo ss -tlnp | grep ':80 '`. If it is Apache and you do not need it, see [Step 2](nginx-guide.md#step-2-make-sure-nothing-else-is-using-port-80). 
    
    ---
    
    **"mkdir() /var/lib/nginx/client-body failed (13: Permission denied)"**
    You ran `nginx` as a normal user. Do not start it by hand. Use `sudo systemctl start nginx`.
    
    ---
    
    **"could not build optimal types_hash"**
    A harmless warning. The fix is in [Step 4](nginx-guide.md#step-4-tidy-up-the-main-config).
    
    ---
    
    **"invalid number of arguments in proxy_pass directive"**
    A typo in the config file, often a stray character such as a backslash before the semicolon. Run `grep proxy_pass /etc/nginx/conf.d/*.conf` and look at the line.
    
    ---
    
    **Python or another app says "Address already in use" on port 8000**
    Something is already using that port. In our testing it was a `mkdocs serve` that was already running. Check with `sudo ss -tlnp | grep ':8000 '`.
    
    ---
    
    **"403 Forbidden" when serving files**
    NGINX cannot read the folder. Keep site files under `/srv/www`, not in your home folder, and make sure the files are readable by everyone.
    
    ---
    
    **The browser shows the wrong site, or a search page**
    Check that the name is in `/etc/hosts`, that you used a `.test` ending, and that you typed `http://` at the start.
    
    ---
    
    **You edited a file and nothing changed**
    Run `sudo nginx -t`, then `sudo systemctl reload nginx`. Editing alone does nothing until you reload.
    
    ---
    
    **Something broke and you want to go back**
    Restore your backup, then test and reload:
    
    ```
    sudo cp /etc/nginx/nginx.conf.bak /etc/nginx/nginx.conf
    sudo nginx -t
    sudo systemctl reload nginx
    ```
    
### Where to go next

!!! info "Where to go next"

    - Add more test sites by repeating [Step 5](nginx-guide.md#step-5-a-local-test-site) with a new name and folder.
    - Proxy more apps by repeating [Step 6](nginx-guide.md#step-6-a-reverse-proxy) with a new name and port.
    
    - Read the official documentation at [nginx.org](https://nginx.org/en/docs/).
    
