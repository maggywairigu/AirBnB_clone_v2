hanged in version 3.2: Added support for Windows.

os.getpriority(which, who)
Get program scheduling priority. The value which is one of PRIO_PROCESS, PRIO_PGRP, or PRIO_USER, and who is interpreted relative to which (a process identifier for PRIO_PROCESS, process group identifier for PRIO_PGRP, and a user ID for PRIO_USER). A zero value for who denotes (respectively) the calling process, the process group of the calling process, or the real user ID of the calling process.

Availability: Unix, not Emscripten, not WASI.

New in version 3.3.

os.PRIO_PROCESS
os.PRIO_PGRP
os.PRIO_USER
Parameters for the getpriority() and setpriority() functions.

Availability: Unix, not Emscripten, not WASI.

New in version 3.3.

os.PRIO_DARWIN_THREAD
os.PRIO_DARWIN_PROCESS
os.PRIO_DARWIN_BG
os.PRIO_DARWIN_NONUI
Parameters for the getpriority() and setpriority() functions.

Availability: macOS

New in version 3.12.

os.getresuid()
Return a tuple (ruid, euid, suid) denoting the current process’s real, effective, and saved user ids.

Availability: Unix, not Emscripten, not WASI.

New in version 3.2.

os.getresgid()
Return a tuple (rgid, egid, sgid) denoting the current process’s real, effective, and saved group ids.

Availability: Unix, not Emscripten, not WASI.

New in version 3.2.

os.getuid()
Return the current process’s real user id.

Availability: Unix.

The function is a stub on Emscripten and WASI, see WebAssembly platforms for more information.

os.initgroups(username, gid, /)
Call the system initgroups() to initialize the group access list with all of the groups of which the specified username is a member, plus the specified group id.

Availability: Unix, not Emscripten, not WASI.

New in version 3.2.

os.putenv(key, value, /)
Set the environment variable named key to the string value. Such changes to the environment affect subprocesses started with os.system(), popen() or fork() and execv().

Assignments to items in os.environ are automatically translated into corresponding calls to putenv(); however, calls to putenv() don’t update os.environ, so it is actually preferable to assign to items of os.environ. This also applies to getenv() and getenvb(), which respectively use os.environ and os.environb in their implementations.

Note On some platforms, including FreeBSD and macOS, setting environ may cause memory leaks. Refer to the system documentation for putenv().
Raises an auditing event os.putenv with arguments key, value.

Changed in version 3.9: The function is now always available.

os.setegid(egid, /)
Set the current process’s effective group id.

Availability: Unix, not Emscripten, not WASI.

os.seteuid(euid, /)
Set the current process’s effective user id.

Availability: Unix, not Emscripten, not WASI.

os.setgid(gid, /)
Set the current process’ group id.

Availability: Unix, not Emscripten, not WASI.

os.setgroups(groups, /)
Set the list of supplemental group ids associated with the current process to groups. groups must be a sequence, and each element must be an integer identifying a group. This operation is typically available only to the superuser.

Availability: Unix, not Emscripten, not WASI.

Note On macOS, the length of groups may not exceed the system-defined maximum number of effective group ids, typically 16. See the documentation for getgroups() for cases where it may not return the same group list set by calling setgroups().
os.setns(fd, nstype=0)
Reassociate the current thread with a Linux namespace. See the setns(2) and namespaces(7) man pages for more details.

If fd refers to a /proc/pid/ns/ link, setns() reassociates the calling thread with the namespace associated with that link, and nstype may be set to one of the CLONE_NEW* constants to impose constraints on the operation (0 means no constraints).

Since Linux 5.8, fd may refer to a PID file descriptor obtained from pidfd_open(). In this case, setns() reassociates the calling thread into one or more of the same namespaces as the thread referred to by fd. This is subject to any constraints imposed by nstype, which is a bit mask combining one or more of the CLONE_NEW* constants, e.g. setns(fd, os.CLONE_NEWUTS | os.CLONE_NEWPID). The caller’s memberships in unspecified namespaces are left unchanged.

fd can be any object with a fileno() method, or a raw file descriptor.

This example reassociates the thread with the init process’s network namespace:

fd = os.open("/proc/1/ns/net", os.O_RDONLY)
os.setns(fd, os.CLONE_NEWNET)
os.close(fd)
Availability: Linux >= 3.0 with glibc >= 2.14.

New in version 3.12.

See also The unshare() function.
os.setpgrp()
Call the system call setpgrp() or setpgrp(0, 0) depending on which version is implemented (if any). See the Unix manual for the semantics.

Availability: Unix, not Emscripten, not WASI.

os.setpgid(pid, pgrp, /)
Call the system call setpgid() to set the process group id of the process with id pid to the process group with id pgrp. See the Unix manual for the semantics.

Availability: Unix, not Emscripten, not WASI.

os.setpriority(which, who, priority)
Set program scheduling priority. The value which is one of PRIO_PROCESS, PRIO_PGRP, or PRIO_USER, and who is interpreted relative to which (a process identifier for PRIO_PROCESS, process group identifier for PRIO_PGRP, and a user ID for PRIO_USER). A zero value for who denotes (respectively) the calling process, the process group of the calling process, or the real user ID of the calling process. priority is a value in the range -20 to 19. The default priority is 0; lower priorities cause more favorable scheduling.

Availability: Unix, not Emscripten, not WASI.

New in version 3.3.

os.setregid(rgid, egid, /)
Set the current process’s real and effective group ids.

Availability: Unix, not Emscripten, not WASI.

os.setresgid(rgid, egid, sgid, /)
Set the current process’s real, effective, and saved group ids.

Availability: Unix, not Emscripten, not WASI.

New in version 3.2.

os.setresuid(ruid, euid, suid, /)
Set the current process’s real, effective, and saved user ids.

Availability: Unix, not Emscripten, not WASI.

New in version 3.2.

os.setreuid(ruid, euid, /)
Set the current process’s real and effective user ids.

Availability: Unix, not Emscripten, not WASI.

os.getsid(pid, /)
Call the system call getsid(). See the Unix manual for the semantics.

Availability: Unix, not Emscripten, not WASI.

os.setsid()
Call the system call setsid(). See the Unix manual for the semantics.

Availability: Unix, not Emscripten, not WASI.

os.setuid(uid, /)
Set the current process’s user id.

Availability: Unix, not Emscripten, not WASI.

os.strerror(code, /)
Return the error message corresponding to the error code in code. On platforms where strerror() returns NULL when given an unknown error number, ValueError is raised.

os.supports_bytes_environ
True if the native OS type of the environment is bytes (eg. False on Windows).

New in version 3.2.

os.umask(mask, /)
Set the current numeric umask and return the previous umask.

The function is a stub on Emscripten and WASI, see WebAssembly platforms for more information.

os.uname()
Returns information identifying the current operating system. The return value is an object with five attributes:

sysname - operating system name

nodename - name of machine on network (implementation-defined)

release - operating system release

version - operating system version

machine - hardware identifier

For backwards compatibility, this object is also iterable, behaving like a five-tuple containing sysname, nodename, release, version, and machine in that order.

Some systems truncate nodename to 8 characters or to the leading component; a better way to get the hostname is socket.gethostname() or even socket.gethostbyaddr(socket.gethostname()).

Availability: Unix.

Changed in version 3.3: Return type changed from a tuple to a tuple-like object with named attributes.

os.unsetenv(key, /)
Unset (delete) the environment variable named key. Such changes to the environment affect subprocesses started with os.system(), popen() or fork() and execv().

Deletion of items in os.environ is automatically translated into a corresponding call to unsetenv(); however, calls to unsetenv() don’t update os.environ, so it is actually preferable to delete items of os.environ.

Raises an auditing event os.unsetenv with argument key.

Changed in version 3.9: The function is now always available and is also available on Windows.

os.unshare(flags)
Disassociate parts of the process execution context, and move them into a newly created namespace. See the unshare(2) man page for more details. The flags argument is a bit mask, combining zero or more of the CLONE_* constants, that specifies which parts of the execution context should be unshared from their existing associations and moved to a new namespace. If the flags argument is 0, no changes are made to the calling process’s execution context.

Availability: Linux >= 2.6.16.

New in version 3.12.

See also The setns() function.
Flags to the unshare() function, if the implementation supports them. See unshare(2) in the Linux manual for their exact effect and availability.

os.CLONE_FILES
os.CLONE_FS
os.CLONE_NEWCGROUP
os.CLONE_NEWIPC
os.CLONE_NEWNET
os.CLONE_NEWNS
os.CLONE_NEWPID
os.CLONE_NEWTIME
os.CLONE_NEWUSER
os.CLONE_NEWUTS
os.CLONE_SIGHAND
os.CLONE_SYSVSEM
os.CLONE_THREAD
os.CLONE_VM
File Object Creation
These functions create new file objects. (See also open() for opening file descriptors.)

os.fdopen(fd, *args, **kwargs)
Return an open file object connected to the file descriptor fd. This is an alias of the open() built-in function and accepts the same arguments. The only difference is that the first argument of fdopen() must always be an integer.

File Descriptor Operations
These functions operate on I/O streams referenced using file descriptors.

File descriptors are small integers corresponding to a file that has been opened by the current process. For example, standard input is usually file descriptor 0, standard output is 1, and standard error is 2. Further files opened by a process will then be assigned 3, 4, 5, and so forth. The name “file descriptor” is slightly deceptive; on Unix platforms, sockets and pipes are also referenced by file descriptors.

The fileno() method can be used to obtain the file descriptor associated with a file object when required. Note that using the file descriptor directly will bypass the file object methods, ignoring aspects such as internal buffering of data.

os.close(fd)
Close file descriptor fd.

Note This function is intended for low-level I/O and must be applied to a file descriptor as returned by os.open() or pipe(). To close a “file object” returned by the built-in function open() or by popen() or fdopen(), use its close() method.
os.closerange(fd_low, fd_high, /)
Close all file descriptors from fd_low (inclusive) to fd_high (exclusive), ignoring errors. Equivalent to (but much faster than):

for fd in range(fd_low, fd_high):
    try:
        os.close(fd)
    except OSError:
        pass
os.copy_file_range(src, dst, count, offset_src=None, offset_dst=None)
Copy count bytes from file descriptor src, starting from offset offset_src, to file descriptor dst, starting from offset offset_dst. If offset_src is None, then src is read from the current position; respectively for offset_dst.

In Linux kernel older than 5.3, the files pointed by src and dst must reside in the same filesystem, otherwise an OSError is raised with errno set to errno.EXDEV.

This copy is done without the additional cost of transferring data from the kernel to user space and then back into the kernel. Additionally, some filesystems could implement extra optimizations, such as the use of reflinks (i.e., two or more inodes that share pointers to the same copy-on-write disk blocks; supported file systems include btrfs and XFS) and server-side copy (in the case of NFS).

The function copies bytes between two file descriptors. Text options, like the encoding and the line ending, are ignored.

The return value is the amount of bytes copied. This could be less than the amount requested.

Note On Linux, os.copy_file_range() should not be used for copying a range of a pseudo file from a special filesystem like procfs and sysfs. It will always copy no bytes and return 0 as if the file was empty because of a known Linux kernel issue.
Availability: Linux >= 4.5 with glibc >= 2.27.

New in version 3.8.

os.device_encoding(fd)
Return a string describing the encoding of the device associated with fd if it is connected to a terminal; else return None.

On Unix, if the Python UTF-8 Mode is enabled, return 'UTF-8' rather than the device encoding.

Changed in version 3.10: On Unix, the function now implements the Python UTF-8 Mode.

os.dup(fd, /)
Return a duplicate of file descriptor fd. The new file descriptor is non-inheritable.

On Windows, when duplicating a standard stream (0: stdin, 1: stdout, 2: stderr), the new file descriptor is inheritable.

Availability: not WASI.

Changed in version 3.4: The new file descriptor is now non-inheritable.

os.dup2(fd, fd2, inheritable=True)
Duplicate file descriptor fd to fd2, closing the latter first if necessary. Return fd2. The new file descriptor is inheritable by default or non-inheritable if inheritable is False.

Availability: not WASI.

Changed in version 3.4: Add the optional inheritable parameter.

Changed in version 3.7: Return fd2 on success. Previously, None was always returned.

os.fchmod(fd, mode)
Change the mode of the file given by fd to the numeric mode. See the docs for chmod() for possible values of mode. As of Python 3.3, this is equivalent to os.chmod(fd, mode).

Raises an auditing event os.chmod with arguments path, mode, dir_fd.

Availability: Unix.

The function is limited on Emscripten and WASI, see WebAssembly platforms for more information.

os.fchown(fd, uid, gid)
Change the owner and group id of the file given by fd to the numeric uid and gid. To leave one of the ids unchanged, set it to -1. See chown(). As of Python 3.3, this is equivalent to os.chown(fd, uid, gid).

Raises an auditing event os.chown with arguments path, uid, gid, dir_fd.

Availability: Unix.

The function is limited on Emscripten and WASI, see WebAssembly platforms for more information.

os.fdatasync(fd)
Force write of file with filedescriptor fd to disk. Does not force update of metadata.

Availability: Unix.
