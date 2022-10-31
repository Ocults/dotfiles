<h2 align="center"> Tokyo Night and Dracula
</h2>

<!-- BADGES -->
<div align="center">
   <p></p>
   <a href="https://github.com/abissaldev/dotfiles/stargazers">
      <img src="https://img.shields.io/github/stars/abissaldev/dotfiles?color=C9CBFF&style=for-the-badge">
   </a>
   <a href="https://github.com/abissaldev/dotfiles/issues">
      <img src="https://img.shields.io/github/issues/abissaldev/dotfiles?color=f7768e&style=for-the-badge">
   </a>
   <a href="../LICENSE.md">
      <img src="https://img.shields.io/github/license/abissaldev/dotfiles?color=73daca&style=for-the-badge">
   </a>
   <br>
</div>
<p/>
<h2></h2>

<!-- INFORMATION -->
## :herb: <samp>INFORMATION</samp> <img alt="" align="right" src="https://badges.pufler.dev/visits/abissaldev/dotfiles?style=for-the-badge&color=A7D9B2&logoColor=white&labelColor=1C2325"/>

   <img src="./assets/showcase.png" alt="Rice Showcase" align="right" width="400px">

   Thanks for dropping by! This is my personal repository of my dotfiles.

   The [setup section](#-setup) will guide you through a step-by-step installation process.

   Here are more information about my setup:

   - **Window Manager:** [bspwm](https://github.com/baskerville/bspwm)
   - **Terminal:** [kitty](https://github.com/kitty/kitty)
   - **Shell:** [zsh](https://www.zsh.org/)
   - **Panel:** [polybar](https://github.com/polybar/polybar)
   - **Compositor:** [picom](https://github.com/yshui/picom)
   - **Editor:** [neovim](https://github.com/neovim/neovim)
   - **Browser:** [qutebrowser](https://github.com/qutebrowser/qutebrowser)
   - **Notification Daemon:** [dunst](https://github.com/dunst-project/dunst)
   - **File Manager:** [thunar](https://github.com/xfce-mirror/thunar)
   - **Application Launcher:** [rofi](https://github.com/davatorium/rofi)
   
   <!-- SETUP -->
   ## :wrench: <samp>SETUP</samp>
   
   This is step-by-step how to install these dotfiles. Just [R.T.F.M](https://en.wikipedia.org/wiki/RTFM).
   
   Clone Repository

   ```sh
    git clone https://github.com/abissaldev/dotfiles.git
    cd dotfiles
   ```
   ## 📦 Installation
   
   <strong>Arch Linux (and other Arch-based distributions)</strong>

   > Assuming your **AUR Helper** is [yay](https://github.com/Jguer/yay).
   ```sh
    yay -S bspwm sxhkd rofi polybar qutebrowser neovim-git kitty viewnior picom \
      hsetroot maim xclip imagemagick setxkbmap thunar dunst Pavucontrol \
      feh ctags zsh
   ```
  <details>
   <summary><strong>Fonts</strong></summary>

   |    Font List     |  Use  |
   | :--------------: | :---: |
   | [`Sarasa Mono CL`](https://github.com/be5invis/Sarasa-Gothic) | Main Font |
   | [`Victor Mono`](https://github.com/rubjo/victor-mono) | Main Italic Font |
   | [`DM Sans`](https://fonts.google.com/specimen/DM+Sans) | Main UI Font |
   | [`Material Icons`](https://github.com/google/material-design-icons/) | Main Icon Font |

   > **NOTE**: Only important fonts has been listed on the table above.

   ```sh
    $ cp -r ./etc/fonts/* $HOME/.local/share/fonts
   ```
   </details>

<strong>Configuration Files and Binaries</strong>

   - `rsync` method <kbd>**RECOMMENDED**</kbd>

      ```sh
       $ mkdir -p $HOME/.config/ && rsync -avxHAXP cfg/ $HOME/.config
       $ mkdir -p $HOME/.local/bin/ && rsync -avxHAXP --exclude 'bin/usr/' bin/ $HOME/.local/bin/
       # To make tabbed and chwb2 to work, you must move it to /usr/local/bin.
       $ sudo rsync -avxHAXP bin/usr/ /usr/local/bin/
      ```

      > **WARNING**: Ensure the `rsync` command must be correct as above.
      > 
      > |   Options   |                      Function                         |
      > | ----------- | ----------------------------------------------------- |
      > | `-a`        | Archive mode                                          |
      > | `-v`        | Verbose mode                                          |
      > | `-x`        | Don't cross filesystem boundaries                     |
      > | `-H`        | Preserve hard links                                   |
      > | `-A`        | Preserve ACLs/permissions                             |
      > | `-X`        | Preserve extended attributes                          |
      > | `-P`        | Show progress during transfer                         |
      > | `--exclude` | Exclude files matching `PATTERN`                      |
   - `cp` method

      ```sh
       $ mkdir -p $HOME/.config/ && cp -r ./cfg/* $HOME/.config/
       $ mkdir -p $HOME/.local/bin/ && cp -r ./bin/* $HOME/.local/bin/
       # To make tabbed and chwb2 to work, you must move it to /usr/local/bin.
       $ sudo mv $HOME/.local/bin/usr/* /usr/local/bin/
      ```

   > **DIFFERENCES**  
   > - `cp` is for duplicating stuff and by default only ensures files have unique full path names.
   > - `rsync` is for synchronizing stuff and uses size and timestamp of files to decide if they should be replaced.
   > I also recommend to not delete the **dotfiles** directory after cloning to make upgrades easier.

