---
layout: post
title: MKSTaskbarPlugin for VMware Workstation for Windows
tags:
- my-software
- software
- vmware
- windows
comments: true
---
[MKSTaskbarPlugin for VMware Workstation for
Windows](http://labs.vmware.com/flings/mkstaskbarplugin)

I wrote this a few years ago and published it a few months ago -- maybe
someone will find it useful.

mksTaskbarPlugin is a DLL which loads both in the vmware-vmx.exe process (to
get the screen image from the virtual machine) and the explorer.exe process
(to interact with the Windows taskbar).

The result is that you can use extra space on your Windows taskbar to show [a
scaled-down, live-updating thumbnail image of your choice of VMware virtual
machine](http://labs.vmware.com/flings/mkstaskbarplugin) running on the same
host. This is useful for keeping an eye on long-running background operations
like software installs in one VM while freeing up most of your screen to
interact with other VMs or the host OS.

