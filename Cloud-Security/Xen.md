Hypervisor
----------
    + Hypervisor or a VMM is a piece of computer software,firmware or hardware that creates and
runs virtual machine.
    + Contains two types of Hypervisor
        * Type 1 or Bare metal or Native Hypervisor
            - Runs above the hardware. Eg. Xen
            - Manages the guests which are running over the hypervisor layer
        * Type 2 or Hosted hypervisor:
            - Runs above an OS. i.e above hardware and above the OS, hypervisor runs Eg. Virtualbox
            - Hypervisor runs as the 2nd layer above the OS and the guests are allowed to run
        as the 3rd layer.

Xen:
----
    + Categorized as Type 1.
    + It controls the underlying hardware + the guest OS running above it.
    + Allows the guest OSs to share the real physical hardware securely and in a resource managed way.
    + Supports Paravirtualization and Hardware Assisted Full virtualization
        * A technique which provides software interface to the virtual machines.
        * Full virtualization is a virtual env, one that is a complete simulation of the underlying hardwr
        * Hardware assisted - enables efficient full virtualization using hardware capabilities.

Paravirtualization:
-------------------
    +
