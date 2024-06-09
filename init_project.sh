sudo apt-get update
sudo apt-get upgrade

# Install OpenFOAM v11
sudo sh -c "wget -O - https://dl.openfoam.org/gpg.key > /etc/apt/trusted.gpg.d/openfoam.asc"
sudo add-apt-repository http://dl.openfoam.org/ubuntu
sudo apt-get -y install openfoam11

# Paraview issues
sudo apt-get install gnome-panel gnome-flashback gnome-session-flashback indicator-applet-appmenu

# Update bash or OpenFOAM dependencies
source /opt/openfoam11/etc/bashrc

export PATH_TO_TEST='./test_cases/gpu_cooling'
$PATH_TO_TEST/Allmesh
$PATH_TO_TEST/Allrun

#Export data from simulation
pvpython export_date.py

#Make data convertion
python data_converter.py

