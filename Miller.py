import matplotlib.pyplot as plt
import numpy as np

def miller_encode(bits):
    """
    Encode binary bits into Miller code with transition points
    Returns:
        - time_points: Array of time values
        - amplitude_levels: Encoded signal levels
        - clock_signal: Reference clock signal
        - transitions: Array marking transition points (1=transition, 0=no transition)
    """
    amplitude = []
    clock = []
    time_points = []
    transitions = []
    
    current_level = 1
    prev_bit = None
    time = 0
    
    for bit in bits:
       
        if bit == 1:
           
            amplitude.extend([current_level, -current_level])
            transitions.extend([0, 1])  
            current_level = -current_level
        else:
            if prev_bit == 0:
                
                amplitude.extend([-current_level, current_level])
                transitions.extend([0, 1]) 
                current_level = -current_level
            else:
              
                amplitude.extend([current_level, current_level])
                transitions.extend([0, 0])
        
        
        clock.extend([1, 0])
        time_points.extend([time, time + 0.5])
        time += 1
        prev_bit = bit
    
    return (np.array(time_points), 
            np.array(amplitude), 
            np.array(clock),
            np.array(transitions))


d = [0,0,1,0,0,0,0,1,0,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0]


time, amplitude, clock, transitions = miller_encode(d)


plt.figure(figsize=(12, 6))


plt.subplot(3, 1, 1)
plt.stem(time, transitions, linefmt='g-', markerfmt='go', basefmt=' ')
plt.title('Transition Points (Green Dots = Transitions)')
plt.ylabel('Transition')
plt.ylim(-0.1, 1.1)
plt.yticks([0, 1], ['', 'Transition'])
plt.grid(True, linestyle=':', alpha=0.5)


plt.subplot(3, 1, 2)
plt.step(time, clock, where='post', color='purple', linewidth=1)
plt.title('Clock Signal')
plt.ylabel('Clock')
plt.ylim(-0.5, 1.5)
plt.yticks([0, 1], ['0', '1'])
plt.grid(True, linestyle=':', alpha=0.5)


plt.subplot(3, 1, 3)
plt.step(time, amplitude, where='post', color='black', linewidth=2)

transition_times = time[transitions == 1]
transition_levels = amplitude[transitions == 1]
plt.plot(transition_times, transition_levels, 'ro', markersize=8, label='Transitions')
plt.title('Miller Encoded Signal (Red Dots = Transitions)')
plt.ylabel('Amplitude')
plt.xlabel('Time (bit periods)')
plt.ylim(-1.5, 1.5)
plt.yticks([-1, 0, 1], ['-1', '0', '+1'])
plt.legend()
plt.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
plt.show()