import pickle
from Simulator.config_generator import SimGenerator
import argparse

def main():
    parser = argparse.ArgumentParser(description="MCHA Simulator")
    # parser.add_argument("input", help="Path to the input file")
    parser.add_argument("-m", "--mode", default="e", help="The processing mode of the simulator, \"e\" for simple example presentation, \"s\" for self-defined algorithm setup")
    args = parser.parse_args()
    if args.mode == 'e':
        # a packed example for small MARL implementation, constrcution process can be found in ./Example
        with open('Test.pkl', 'rb') as f:
            Generator:SimGenerator = pickle.load(f)
        Test = Generator.GenerateSim()
        Test.StepSim()
    return


if __name__ == '__main__':
    main()