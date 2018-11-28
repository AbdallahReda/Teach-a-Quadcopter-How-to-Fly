# Teach-a-Quadcopter-How-to-Fly
Design an agent that can fly a quadcopter, and then train it using a reinforcement learning algorithm.



Clone the repository and navigate to the downloaded folder.
```
git clone https://github.com/sharifovrus/Teach-a-Quadcopter-How-to-Fly-2.git
cd Teach-a-Quadcopter-How-to-Fly
```

Create and activate a new environment.
```
conda create -n quadcop python=3.6 matplotlib numpy pandas
source activate quadcop
```

Create an [IPython kernel](http://ipython.readthedocs.io/en/stable/install/kernel_install.html) for the `quadcop` environment.
```
python -m ipykernel install --user --name quadcop --display-name "quadcop"
```
    
Open the notebook.
```
jupyter notebook Quadcopter_Project.ipynb
```
    
    
 Before running code, change the kernel to match the `quadcop` environment by using the drop-down menu (**Kernel > Change kernel > quadcop**). Then, follow the instructions in the notebook.


 Requirements:
   - matplotlib==2.0.0
   - numpy==1.14.1
   - pandas==0.19.2
