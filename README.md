# winOpt

> A lightweight Windows optimization and maintenance utility built with Python.


![windows](https://img.shields.io/badge/OS-Windows-blue) ![release](https://img.shields.io/badge/Pre--release-v0.3.3--alpha1-yellow) ![license](https://img.shields.io/badge/License-winOpt_Personal_Use_License-red) ![version.py](https://img.shields.io/badge/python-3.14.0-blue)


winOpt is a Windows-focused command-line utility designed to provide
system maintenance, cleanup, optimization and software management
tools from a single interface.


## Screenshots

### Main Menu

![winOpt main menu](assets/screenshots/main-menu.png)


## Features

winOpt brings several useful Windows maintenance, configuration, and optimization tools together into a single command-line interface.

### ⚡ Windows Power Management

Manage Windows power plans directly from winOpt.

* View and select available power plans
* Quickly switch between different power configurations
* Useful for choosing between power efficiency and performance-oriented settings
* Designed to make power-plan management faster and easier

### 💾 Disk Maintenance

Access Windows disk maintenance tools from a simple menu.

* Run disk maintenance operations on selected drives
* Choose which drive you want to work with
* Supports different operations depending on the selected storage type
* Provides a convenient interface for Windows' built-in disk utilities

### 🧹 Cache & Temporary File Cleanup

Clean unnecessary temporary data from common Windows locations.

* Remove temporary files
* Clean cached data
* Help reclaim disk space
* Handle files that may be in use by Windows or other applications
* Designed as a quick maintenance option for regular system cleanup

> **Note:** Windows may prevent certain files from being deleted because they are currently being used by the system or another application.

### 🧩 Driver Management

winOpt provides access to driver-related functionality from the main interface.

* Centralized driver management options
* Designed to simplify common driver-related tasks
* Provides additional system-management functionality without requiring users to navigate through multiple Windows utilities

> ⚠️ Driver operations can affect system hardware functionality. Use this feature carefully and only install drivers from trusted sources.

### 📦 Software Installation

winOpt aims to make installing commonly used software more convenient.

* Access software installation options from the main menu
* Reduce the need to manually search for and download individual applications
* Designed to make setting up a Windows installation faster

Additional applications and installation options will be added as the project develops.

### 🖥️ Command-Line Interface

winOpt is built around a straightforward CLI experience.

* Simple numbered menus
* Easy navigation
* Lightweight interface
* Designed to be understandable for both beginners and experienced users
* No unnecessary graphical interface or background services

### 🔐 Administrator Privileges

Some Windows maintenance operations require elevated permissions.

winOpt can request Administrator privileges when necessary so that system-level operations can be performed correctly.

This allows the application to interact with parts of Windows that are normally restricted to standard users.

### 🛠️ Windows-Focused Utilities

Rather than attempting to become an all-purpose system utility, winOpt focuses specifically on Windows.

The project brings together several types of system-management functionality into one place, with the goal of making common maintenance tasks easier to access.

### 🚧 Continuously Expanding

winOpt is still in development, and the feature set will continue to grow.

Planned improvements include:

* Additional Windows optimization tools
* More cleanup options
* Expanded software installation support
* Additional system-management utilities
* Improved reliability and error handling
* More configuration options
* Further improvements to the CLI experience

> **winOpt is currently an alpha/pre-release project. Some features may still be experimental or under development.**



## Why winOpt?

Windows provides a huge number of tools for managing, maintaining, and configuring your system, but many of them are scattered across different parts of the operating system. Some settings are hidden behind multiple menus, while other maintenance tasks require using Windows utilities, command-line tools, or manually navigating through system folders.

**winOpt was created to bring some of these tasks together into one simple command-line utility.**

The goal of winOpt is not to replace every Windows system tool or promise unrealistic performance improvements. Instead, it aims to provide a convenient collection of useful Windows maintenance and optimization tools in one place, while keeping the experience simple enough for everyday users.

### ⚡ One place for common Windows tasks

Instead of searching through Windows Settings, Control Panel, system utilities, and individual tools, winOpt provides a central menu for several common maintenance operations.

Depending on the available version, winOpt can provide tools for tasks such as:

* Managing Windows power plans
* Performing disk maintenance
* Cleaning temporary and cached files
* Managing drivers
* Installing selected software
* Performing other system maintenance operations

The project is designed so that these operations can be accessed from a straightforward CLI interface rather than requiring users to remember individual commands or search through Windows menus.

### 🖥️ Designed for Windows

winOpt is built specifically around Windows system utilities and workflows.

Rather than trying to be a cross-platform tool with a large collection of unrelated features, the project focuses on providing useful functionality for Windows users and taking advantage of tools already available within the operating system.

This makes winOpt particularly suitable for users who want a lightweight Windows-focused utility without installing a large suite of third-party system-management software.

### 🧑‍💻 Simple for users, interesting for developers

winOpt is intended for two different types of users.

**For everyday users**, the goal is simplicity. You should be able to download the latest release, extract it, run the executable, and access the available tools from the main menu.

**For developers and technically curious users**, the source code is publicly available for inspection. You can see how the application interacts with Windows utilities, how its CLI is structured, and how the different maintenance features are organized.

The project is therefore not intended to be a mysterious "one-click optimizer" that asks users to trust a collection of unknown operations. The source is available so that technically minded users can inspect what the program does.

### 🔍 Transparency over magic

There are many Windows optimization tools that make large claims about dramatically increasing performance with a single click.

winOpt takes a different approach.

The project focuses on providing recognizable Windows maintenance and configuration operations rather than presenting optimization as magic. Each feature is intended to perform a specific task, and users should be able to understand what kind of operation they are running.

Performance improvements will naturally depend on the individual computer, Windows configuration, hardware, storage, and workload. **winOpt does not guarantee that every feature will make every computer faster.**

### 🪶 Lightweight and focused

winOpt is designed to remain relatively lightweight and focused on its purpose.

There is no intention to turn the project into a huge collection of unrelated utilities. The goal is to gradually build a useful set of Windows maintenance and optimization features while keeping the interface understandable and the project maintainable.

This also means that new features are added with the overall purpose of the project in mind rather than simply adding features for the sake of having a longer feature list.

### 🛠️ Built as an evolving project

winOpt is an actively developing project.

The early releases are intentionally published as **alpha and pre-release versions**. This allows the project to be tested, improved, and expanded before reaching a stable release.

Some planned functionality may not yet be available, and the behavior of certain features may continue to change during development.

Feedback, bug reports, and feature suggestions can help shape future versions of the project.

### 🎯 The long-term goal

The long-term goal of winOpt is to become a practical Windows maintenance and optimization utility that combines useful system tools into a single, understandable interface.

Rather than trying to be the "ultimate Windows optimizer," winOpt aims to be something more useful:

> **A simple, transparent, Windows-focused toolbox for everyday system maintenance.**

The project will continue to evolve through new features, improvements, testing, and user feedback.

**winOpt is still growing — and this is only the beginning.**


## Installation

### Download

Download the latest Windows release from the Releases page.

Extract the archive and run `winOpt.exe`.


### Run from source

Clone the repository:

git clone https://github.com/aniciccstefan/winOpt.git

cd winOpt

python winOpt.py


## License

winOpt is proprietary software.

The source code is publicly available for inspection, but it is **not open-source software**.

You may use and redistribute the original, unmodified version of winOpt according to the terms of the [winOpt Personal Use License](LICENSE.md).

Modification and redistribution of modified or derivative versions are not permitted without explicit written permission from the copyright holder.

**Copyright © 2026 Stefan Aničić. All rights reserved.**



## Author

Developed and maintained by [aniciccstefan].


© 2026 Stefan Aničić. All rights reserved.