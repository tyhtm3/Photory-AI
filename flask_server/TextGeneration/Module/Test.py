
import StoryGenerator_photory as SGEN



def main():
    
    StoryGenerator = SGEN.StoryGeneration()
    #print(StoryGenerator.Generate_p_sampling())
    print(StoryGenerator.Generate_p_sampling('그가 날 바라봤을 때'))
if __name__ == "__main__" :
    main()