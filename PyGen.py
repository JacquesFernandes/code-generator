import random;
import threading;

class GeneratorThread(threading.Thread):

    def __init__(self,num_samples,length=1,seed=None):
        threading.Thread.__init__(self);
        self.rgen = random.Random();
        self.rgen.seed(seed);
        self.num_samples = num_samples;
        self.output_list = list();
        self.sample_length = length;
        self.is_running = bool();

    def run(self):
        self.is_running = True;
        for i in range(self.num_samples):
            temp_string = str();
            for j in range(self.sample_length):
                temp_string += chr(self.rgen.randint(65,90));
            if temp_string not in self.output_list:
                self.output_list.append(temp_string);
            else:
                i -= 1;
        self.is_running = False;
        print(self.output_list);
        return;

    def get_output_list(self):
        return(self.output_list);

if __name__ == "__main__":
    gt = GeneratorThread(500,6);
    gt.start();
    gt.join();
    print("done!");
