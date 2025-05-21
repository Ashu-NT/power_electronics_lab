
import matplotlib.pyplot as plt

import matplotlib.image as mpimg
from IPython.display import display,Markdown
from logger import logging

# Set plot style for professional reports
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12


  
def insert_circut_diagram(img_path,img_title) -> None:
    try:
        img = mpimg.imread(img_path)
        plt.imshow(img)
        plt.axis('off')
        plt.title(img_title, fontsize=16)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        display(Markdown(f"**The image location is wrong, or it is not uploaded at all."))
        logging.info(f"Error Inserting Circuit diagram {e}")
        

def plot_sim_data(sim_data=None,  x_label='', y_label='', title='', label ="LTSpice Simulation"):
    fig, ax = plt.subplots()
    try:
        if sim_data is not None:
             x_sim = sim_data.iloc[:, 0]  # Adjust column index as needed
             y_sim = sim_data.iloc[:, 1]  # Adjust column index as needed
             ax.plot(x_sim, y_sim, 'ro', label=label)    
    except Exception as e:
        print(f"Error Plotting: {e}")
        
    # Set labels and title
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.grid(True)
    ax.legend()
    
    plt.tight_layout()
    return fig, ax

def plot_single_oscillo_data(ch1_data=None,ch2_data=None,  x_label='', y_label='', title='', label ="LTSpice Simulation"):
    fig, ax = plt.subplots()
    try:
        if ch1_data and ch2_data is not None:
             x_ch1 = ch1_data.iloc[:, 1]  # Adjust column index as needed
             y_ch2 = ch2_data.iloc[:, 1]  # Adjust column index as needed
             ax.plot(x_ch1, y_ch2, 'b-', label=label)    
    except Exception as e:
        print(f"Error Plotting: {e}")
        
    # Set labels and title
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.grid(True)
    ax.legend()
    
    plt.tight_layout()
    return fig, ax


# Function to plot multiple data

def plot_multiple_data(processed_data:dict,values:list,x_label='', y_label='', title='', values_unit = 'μA'):
    
    cmap = plt.cm.viridis
    fig, ax = plt.subplots()
    
    for i, index in enumerate(values):
    # Calculate color based on position in the sequence
        color = cmap(i / (len(values) - 1) if len(values) > 1 else 0.5)
        
        if index in processed_data:
            data = processed_data[index]
            
            # Plot CH1 vs CH2 
            ax.plot(data['ch1_col_2'], data['ch2_col_2'], 
                    label=f'{index} {values_unit}', color=color)
            
        # Set labels and title
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.grid(True)
    ax.legend()
    
    plt.tight_layout()
    
    return fig,ax