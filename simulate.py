from Simulator import Simulator


simulation_done = False
sim_time = 1000
# trajectory = [[0,0], [5,5]]
trajectory = [[0, 0], [-3.5, 3.5], [-3.5, 7.5], [-4, 11.5], [-5, 10.5],
              [-7.5, 10.5], [-7.5, 14.5], [-11, 16], [-15, 18.5], [-18, 21.5],
              [-18, 24.5], [-14, 23.5], [-11, 22.5], [-7, 21.5], [-3.5, 21.5],
              [-3.5, 26.5], [-4.5, 30.5], [-4, 32.5], [-6, 32.5], [-8, 34.5],
              [-8, 38.5], [-4, 37.5], [0, 39], [4, 37.5], [8, 38.5], [8, 34.5],
              [6, 32.5], [4, 32.5], [4.5, 30.5], [3.5, 26.5], [3.5, 21.5],
              [7, 21.5], [11, 22.5], [14, 23.5], [18, 24.5], [18, 21.5],
              [15, 18.5], [11, 16], [7.5, 14.5], [7.5, 10.5], [5, 10.5],
              [4, 11.5], [3.5, 7.5], [3.5, 3.5], [0, 0]]

main_simulator = Simulator(sim_time, trajectory)

while not simulation_done:
    main_simulator.measure()
    main_simulator.calculate_target_data()
    main_simulator.calculate_control()
    main_simulator.move()
    main_simulator.check_target()
    main_simulator.accumulate_data()
    simulation_done = main_simulator.check_simulation_done()

main_simulator.plot_main_data()
