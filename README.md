# FlumeControl

This repo is for the implementation of a software interface to a variable frequency drive (VFD) motor controller. The software interface will allow for control of the motor from a desktop computer. The main components of the software consist of: the VFD-PC interface, mapping VFD frequencies to fluid velocity achieved by the pump/motor, and a graphical user interface.

[links to remote collaboration]: #links-for-the-meeting-on-saturday-march-13--10am-pst
[first-time setup]: #first-time-setup
[Discussions]: https://github.com/blakeNaccarato/pybites/discussions
[this repo on GitHub]: https://github.com/blakeNaccarato/pybites

## Header 1

*Edit Later*.

## Header 2

Run [first-time setup], then you're ready to explore the repo. Overview:

- `List Item 1` – Configuration files for our "linters". Linters make sure we're writing clean code.
- `List Item 2` – Blank template challenges, code tests (to check if you did it correctly), and shared code goes here.
- `List Item 3` – The settings in here will automatically apply when viewing in VSCode. Also has extension recommendations.
- `List Item 4` – Find the subfolder with your name on it and you can start solving challenges.
- `List Item 5` – Lists patterns/files/folders that we don't want to push to GitHub, for example the `Thing` folder.

## Header 3

Paragraph. **Bolded** *Italisized* Sentence.

- <https://github.com/>
- <https://github.com/>

## First-time setup

Edit Later

- [FlumeControl](#flumecontrol)
  - [Header 1](#header-1)
  - [Header 2](#header-2)
  - [Header 3](#header-3)
  - [First-time setup](#first-time-setup)
    - [Install Python 3.8.8](#install-python-388)
    - [Install PowerShell 7.1.3](#install-powershell-713)
    - [Install Git](#install-git)
    - [Install VSCode and clone this repo](#install-vscode-and-clone-this-repo)
    - [Install recommended extensions and set up environment](#install-recommended-extensions-and-set-up-environment)

### Install Python 3.8.8

Install Python using the [Python 3.8.8 64-bit installer]. Make sure **not to add Python 3.8 to PATH** as seen below. If you need to see the image below in greater detail, try right-clicking on it and opening it in a new tab.

[Python 3.8.8 64-bit installer]: https://www.python.org/ftp/python/3.8.8/python-3.8.8-amd64.exe

![Python installation screenshots](https://i.imgur.com/5mUiTTU.png)

### Install PowerShell 7.1.3

Download [PowerShell v7.1.3] and install it. The link is an `*.msi` file. Double-click it to install.

[PowerShell v7.1.3]: https://github.com/PowerShell/PowerShell/releases/download/v7.1.3/PowerShell-7.1.3-win-x64.msi

![PowerShell installation screenshot](https://i.imgur.com/TgLRSNr.png)

### Install Git

Install [Git]. Use the following screenshots to guide your installation. Some options may appear slightly different than in these screenshots. That's okay. Just use your best judgement and don't worry about it too much. If you need to see the image below in greater detail, try right-clicking on it and opening it in a new tab.

[Git]: https://git-scm.com/downloads

![Git installation screenshots](https://i.imgur.com/pztSaet.png)

### Install VSCode and clone this repo

Install [VSCode]. I don't have screenshots for this installation process, but it should be pretty straight-forward.

Select the following text with your mouse and **Ctrl+C** to copy it: <https://github.com/blakeNaccarato/pybites.git>. You can also get this link on your clipboard by clicking the green "Code" button at [this repo on GitHub], and clicking the clipboard icon for the "HTTPS" option.

![GitHub dialog screenshot](https://i.imgur.com/vjr9P0L.png)

Open VSCode. Press **Ctrl+Shift+P** to bring up the *Command Palette*, and begin typing "Clone" until "Git: Clone" surfaces in the dialog box. Select that option (with the arrow keys, if needed) and press **Enter**. Press **Ctrl+V** to paste the link in the dialog box with the greyed-out text saying "Provide repository URL or pick a repository source." Press **Enter** to confirm the action. Choose anywhere on your local drive (*not in cloud storage like OneDrive or Google Drive*) to put the project. It will go into a subfolder named `pybites`. When prompted, click "Open" in the dialog box to open the folder in VSCode, as seen below.

If you are not automatically prompted to log in to GitHub on VSCode when you attempt this action, then follow [this guide] to log in.

![VSCode clone screenshot](https://i.imgur.com/v6cD3sW.png)

[VSCode]: https://code.visualstudio.com/
[this guide]: https://code.visualstudio.com/docs/editor/github

### Install recommended extensions and set up environment

The `.vscode/extensions.json` file recommends certain extensions for this workspace. To install them, click the "Extensions" sidebar button (step 1 below), type `@recommended` in the search bar (2), and then click the cloud icon (3) to install all recommended extensions. After all extensions are installed, you will probably need to reload the VSCode window by pressing **Ctrl+Shift+P** and typing "Developer: Reload window". You may also click the "Reload required" button that pops up on relevant extensions.

![test](https://i.imgur.com/BcLnV2v.png)

Finally, press **CTRL+\`** (that's a "backtick", near the top-left of your keyboard) to pull up the "Integrated Terminal". This gives you a PowerShell terminal in which to execute commands in the current environment. Enter `.\setup.ps1` to set up your Python environment. VSCode may prompt you to "activate" the environment. Click "Yes" if prompted.
