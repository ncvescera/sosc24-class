The FPGA for Friday came from two different vendors. The first is a Xilinx Artix7 on a Basys3 board. The second is a Lattice device.
If you want to install the tools on your own computer (linux only and completely optional) you have to install the following packages:

# AMD/Xilinx

Pre-requisites:

 `sudo apt-get install -y libncurses5 libtinfo5`

Download the installer from the Xilinx website and run it. The installer will install the Vivado IDE and the SDK. You need to install the cable drivers separately for the direcory `data/xicom/cable_drivers/lin64/install_script/install_drivers/`

**Warning**: The installer is huge and will take a long time to download and install, plus it requires to register on the Xilinx website.

# Lattice

We will use the open source tools for Lattice. The tools are called `yosys`, `nextpnr` and `icestorm`. You can install the OSS CAD SUITE for https://github.com/YosysHQ
