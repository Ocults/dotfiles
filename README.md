<h2 align="center"> Tokyo Night and Dracula
</h2>

<!-- BADGES -->
<div align="center">
   <p></p>
   <a href="https://github.com/janleigh/dotfiles/stargazers">
      <img src="https://img.shields.io/github/stars/abissaldev/dotfiles?color=C9CBFF&labelColor=a9b1d6&style=for-the-badge">
   </a>
   <a href="https://github.com/janleigh/dotfiles/issues">
      <img src="https://img.shields.io/github/issues/abissaldev/dotfiles?color=f7768e&labelColor=1C2325&style=for-the-badge">
   </a>
   <a href="../LICENSE.md">
      <img src="https://img.shields.io/github/license/abissaldev/dotfiles?color=73daca&labelColor=1C2325&style=for-the-badge">
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
   - **Notification Daemon:** [dunst](https://github.com/dunst-project/dunst)
   - **File Manager:** [thunar](https://github.com/xfce-mirror/thunar)
   - **Application Launcher:** [rofi](https://github.com/davatorium/rofi)
   
   <!-- SETUP -->
   ## :wrench: <samp>SETUP</samp>
   
   This is step-by-step how to install these dotfiles. Just [R.T.F.M](https://en.wikipedia.org/wiki/RTFM).
   
   Clone Repository

   ```sh
    git clone --recurse-submodules https://github.com/janleigh/dotfiles.git
    cd dotfiles && git submodule update --remote --merge
   ```
   ## 📦 Installation
   
   <strong>Arch Linux (and other Arch-based distributions)</strong>

   > Assuming your **AUR Helper** is [yay](https://github.com/Jguer/yay).
   ```sh
    yay -S bspwm sxhkd rofi neovim-git kitty viewnior picom \
      playerctl hsetroot maim jq xclip imagemagick dunst
   ```
