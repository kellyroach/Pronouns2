# Git Bash for Windows Users
- **Apple macOS**: If you are using Apple macOS, you don't need
  to read nor do any of the following.
- **Microsoft Windows**: If you are using Microsoft Windows,
  there is a good chance you don't have a `make` command already
  installed on your PC.  The gist is we have you: install
  [MSYS2](https://www.msys2.org), install `make` in
  [MSYS2](https://www.msys2.org), add paths to `Environment
  Variables`, install [Git Bash](https://gitforwindows.org/),
  then use [Git Bash](https://gitforwindows.org/) as a more
  empowered POSIX-like substitute for CMD.EXE and you can enjoy
  every aspect of Pronouns2.

## Understanding the Terminology
- **Git for Windows**: The complete software package that
  includes both Git and Unix tools for Windows
- **Git Bash**: A terminal emulator (git-bash.exe) included with
  Git for Windows that provides a Unix-like command interface
- **git-cmd.exe**: A Windows command prompt that adds Git to the
  PATH but uses Windows commands
- **GNU Bash**: The actual shell program running inside
  [Git Bash](https://gitforwindows.org/) (current version
  5.2.37)

## Why Git Bash?
We recommend [Git Bash](https://gitforwindows.org/) because it:
- Provides a Unix-like environment that works well with Windows
- Includes Git and essential Unix tools in one installation
- Can be enhanced with additional tools through [MSYS2](https://www.msys2.org)
- Maintains compatibility with Windows commands and paths

Other options like [MinGW](https://www.mingw-w64.org),
[Cygwin](https://cygwin.com), or
[WSL](https://learn.microsoft.com/en-us/windows/wsl/) require
more complex setup or provide more functionality than Pronouns2
needs.

## Step-by-Step Setup Guide

### 1. Requirements
- [MSYS2](https://www.msys2.org) requires 64 bit Windows 10 or
  newer.
- [Git for Windows](https://gitforwindows.org/) requires Windows 8.1
  or later on i686 and x86_64 CPU architectures.
- [Git for Windows](https://gitforwindows.org/) requires Windows 11
  on ARM64 CPU architecture.

### 2. Install MSYS2:
- Visit [https://www.msys2.org](https://www.msys2.org)
- Download the installer (e.g., `msys2-x86_64-20241208.exe`).
- Run the installer.
- You may need to click through a Windows SmartScreen:
    - A popup says "Windows protected your PC / Microsoft
      Defender SmartScreen".
    - Click "More info" beneath the message.
    - Click "Run anyway" button.
- Use default installation options.
- Let it launch [MSYS2](https://www.msys2.org) when finished

### 3. Install `make` in MSYS2:
- In the [MSYS2](https://www.msys2.org) console (UCRT64) that
  opens, run these commands:
  ```bash
  pacman -Syu
  pacman -S mingw-w64-x86_64-make
  ```
- Type `Y` when prompted to proceed with installation.

### 4. Add MSYS2 to Windows PATH:
- Quick path: Windows key + Start typing `environment variables`.
- Either:
  - Windows 10-11: Settings → System → About → Advanced system settings
  - Windows 10: Control Panel → System and Security → System → Advanced system settings
- Click `Environment Variables`.
- Under `System variables`, find and edit `Path`.
- Add these two new paths:
  ```
  C:\msys64\mingw64\bin
  C:\msys64\usr\bin
  ```

### 5. Install Git Bash:
- Visit [https://gitforwindows.org/](https://gitforwindows.org/).
- Download the installer (e.g., `Git-2.47.1-64-bit.exe`).
- Close and reopen [Git Bash](https://gitforwindows.org/) if it
  was already open.
- Navigate to `Pronouns2` using `cd` commands.
  (e.g., `cd /c/Pronouns2`)
- Run `Pronouns2` project `make` commands in
  [Git Bash](https://gitforwindows.org/) as needed.
