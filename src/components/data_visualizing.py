
import matplotlib.pyplot as plt
import numpy as np
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
        
        
def plot_two_variable(x_data=None,  y_data=None, x_label='', y_label='', title='', label =" "):
    fig, ax = plt.subplots()
    try:
        if x_data is not None and y_data is not None:
             
             ax.plot(x_data, y_data, 'b-', label=label)    
    except Exception as e:
        logging.info(f"Error Plotting: {e}")
        
    # Set labels and title
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.grid(True)
    ax.legend()
    
    plt.tight_layout()
    return fig, ax

def plot_sim_data(sim_data=None,  x_label='', y_label='', title='', label ="LTSpice Simulation"):
    fig, ax = plt.subplots()
    try:
        if sim_data is not None:
             x_sim = sim_data.iloc[1:, 0]  # Adjust column index as needed
             y_sim = sim_data.iloc[1:, 1]  # Adjust column index as needed
             ax.plot(x_sim, y_sim, 'ro', label=label)    
    except Exception as e:
        logging.info(f"Error Plotting: {e}")
        
    # Set labels and title
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.grid(True)
    ax.legend()
    
    plt.tight_layout()
    return fig, ax

def plot_multiple_sim_data(sim_data=None,  x_label='',title='',
                            y1_label='', y2_label='', y3_label='',
                           label1 ="1st data",label2 ="2nd data",label3 ="3rd data"):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax3 = ax1.twinx()
    
 
    try:
        if sim_data is not None:
            # Time and signal columns
            t_sim = sim_data.iloc[1:, 0] * 1e6  # µs
            x_sim = sim_data.iloc[1:, 1]       # V
            y_sim = sim_data.iloc[1:, 2] * 1e3  # mA
            z_sim = sim_data.iloc[1:, 3] * 1e3  # mW

            # First Y-axis: 
            ax1.plot(t_sim, x_sim, color='#aabb05', linestyle="-.", label=label1)
            ax1.set_ylabel(y1_label, color='#aabb05')
            ax1.tick_params(axis='y', labelcolor='#aabb05')
            ax1.set_yticks(np.arange(0,3.9,0.3))

            # Second Y-axis: 
          
            ax2.plot(t_sim, y_sim, color='#aa0bcc', linestyle="-", label=label2)
            ax2.set_ylabel(y2_label, color='#aa0bcc')
            
            ax2.tick_params(axis='y', labelcolor='#aa0bcc')

            # Third Y-axis: 
            
            ax3.spines["right"].set_position(("axes", 1.15))  # shift third y-axis to the right
            ax3.plot(t_sim, z_sim, color='#FF5733', linestyle="--", label=label3)
            ax3.set_ylabel(y3_label, color='#FF5733')
            ax3.set_yticks(np.arange(0,150,15))
            ax3.tick_params(axis='y', labelcolor='#FF5733')

            # Add all legends to one box
            lines = ax1.get_lines() + ax2.get_lines() + ax3.get_lines()
            labels = [line.get_label() for line in lines]
            ax1.legend(lines, labels, loc='upper right')

    except Exception as e:
            logging.info(f"Error Plotting: {e}")

    ax1.set_xlabel(x_label)
    ax1.set_title(title)
    ax1.grid(False)
    ax2.grid(False)
    ax3.grid(False)

    plt.tight_layout()
    return fig

def plot_single_oscillo_data(ch1_data=None,ch2_data=None,  x_label='', y_label='', title='', label ="LTSpice Simulation"):
    fig, ax = plt.subplots()
    try:
        if ch1_data and ch2_data is not None:
             x_ch1 = ch1_data.iloc[:, 1]  # Adjust column index as needed
             y_ch2 = ch2_data.iloc[:, 1]  # Adjust column index as needed
             ax.plot(x_ch1, y_ch2, 'b-', label=label)    
    except Exception as e:
        logging.info(f"Error Plotting: {e}")
        
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