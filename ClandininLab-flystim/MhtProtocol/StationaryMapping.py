import numpy as np
from flystim.trajectory import Trajectory

class StationaryMapping():
    def getEpochParameters(protocolObject):
        stimulus_ID = 'MovingPatch'
        az_loc = protocolObject.protocol_parameters['azimuth_locations']
        el_loc = protocolObject.protocol_parameters['elevation_locations']
        
        if type(az_loc) is not list:
            az_loc = [az_loc]
        if type(el_loc) is not list:
            el_loc = [el_loc]
        

        stim_time = protocolObject.run_parameters['stim_time'] #sec
        flash_duration = protocolObject.protocol_parameters['flash_duration'] #sec
        
        time_steps = np.arange(0,stim_time,flash_duration)
        no_steps = len(time_steps)
        x_steps = np.random.choice(az_loc, size = no_steps, replace=True)
        y_steps = np.random.choice(el_loc, size = no_steps, replace=True)
 
        
        # time-modulated trajectories
        x = Trajectory(list(zip(time_steps,x_steps)), kind = 'previous') #note interp kind is previous
        y = Trajectory(list(zip(time_steps,y_steps)), kind = 'previous')
        # constant trajectories:
        w = Trajectory(protocolObject.protocol_parameters['square_width'])
        h = Trajectory(protocolObject.protocol_parameters['square_width'])
        angle = Trajectory(0)
        color = Trajectory(protocolObject.protocol_parameters['color'])
        trajectory = {'x': x.to_dict(), 'y': y.to_dict(), 'w': w.to_dict(), 'h': h.to_dict(),
            'angle': angle.to_dict(), 'color': color.to_dict()}

        epoch_parameters = {'name':stimulus_ID,
                            'background':protocolObject.run_parameters['idle_color'],
                            'trajectory':trajectory}
        convenience_parameters = {'square_width':protocolObject.protocol_parameters['square_width'],
                                  'angle':0,
                                  'color':protocolObject.protocol_parameters['color'],
                                  'elevation_locations':el_loc,
                                  'azimuth_locations':az_loc,
                                  'flash_duration':protocolObject.protocol_parameters['flash_duration'],
                                  'x_steps':x_steps,
                                  'y_steps':y_steps,
                                  'time_steps':time_steps}

        return epoch_parameters, convenience_parameters
        
        
    def getParameterDefaults():
        protocol_parameters = {'square_width':5.0,
                       'color':0.0,
                       'elevation_locations': [100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0], # 100...140
                       'azimuth_locations': [30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0], #30...80
                       'flash_duration':0.25}
        
        return protocol_parameters
    
    
    def getRunParameterDefaults():
        run_parameters = {'protocol_ID':'StationaryMapping',
              'num_epochs':6,
              'pre_time':2.0,
              'stim_time':100.0,
              'tail_time':2.0,
              'idle_color':0.5}
        return run_parameters