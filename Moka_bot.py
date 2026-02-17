while True:
    user_input = input("You: ")
    user_input = user_input.lower()

    if "how are you" in user_input:
        print("Bot: I'm just a moka bot, but I'm here to help!\n")

    elif "what is your name" in user_input:
        print("Bot: My name is wolf.\n")

    elif "hello" in user_input:
        print("Bot: Hello there!\n")
        
    elif "bye" in user_input:
        print("Bot: Bye! Bye!\n")
    elif "stars" in user_input:
        print("  *  ")
        print(" *** ")
        print("*****")
        
    elif "hi" in user_input:
        print("Bot: Hi there!\n")
        
    elif "what language do you speak" in user_input:
        print("Bot: I currently speak English, but as soon as I'm trained, I can speak any language as well.\n")
        
    elif "who are you" in user_input:
        print("Bot: I am Moka bot, I am here to help you!\n")

    elif "thank you" in user_input:
        print("Bot: You're welcome!")

    elif "date" in user_input or "what date is today" in user_input:
        import datetime
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        print(f"Bot: Today's date is {current_date}.\n")

    elif "day" in user_input or "what day is today" in user_input:
        import datetime
        current_day = datetime.datetime.now().strftime("%A")
        print(f"Bot: Today is {current_day}.\n")
        
    elif "what is ai" in user_input or "ai" in user_input:
        print("Bot: AI, or Artificial Intelligence, refers to the simulation of human intelligence processes by machines. It aims to enable machines to perform tasks that typically require human intelligence, such as recognizing patterns, making decisions, and understanding natural language.\n")
    
    elif "father of computer" in user_input:
        print("Bot: The title 'Father of Computer' is often attributed to Charles Babbage, who designed the Analytical Engine, an early mechanical general-purpose computer.\n")
        
    elif "what is computer" in user_input:
        print("Bot: A computer is an electronic device that can perform various tasks by executing instructions. It consists of hardware components such as a CPU, memory, storage, input/output devices, and plays a crucial role in modern life.\n")
        
    elif "my school name" in user_input:
        print("Bot: Kongu School\n")
        
    elif "my project name" in user_input:
        print("Bot: My project\n")
        
    elif "chandrayaan 3" in user_input:
        print("Bot: Chandrayaan-3 is the third Indian lunar exploration mission by ISRO, consisting of a lander and rover similar to Chandrayaan-2.\n")
        
    elif "science project idea" in user_input:
        print("Bot: Here are some general science project ideas:\n"
              "- Renewable Energy Innovations\n"
              "- Volcano Eruption Simulation\n"
              "- Exploring Simple Machines\n"
              "- Ecosystem Diorama: Life Interactions\n"
              "- Clean Water Filtration System\n"
              "- Journey Through Human Body Systems\n"
              "- Robotics and Automation Showcase\n"
              "- Unveiling Electrical Circuits\n"
              "- Wonders of Space Exploration\n"
              "- Chemical Reactions Unveiled\n"
              "- Mini Weather Station Insights\n"
              "- Biodegradable Plastics Experiment\n"
              "- Microscopic World Revealed\n"
              "- Hydroponic Plant Growth Insights\n"
              "- Geological Wonders: Rocks and Minerals\n")

    elif "chemistry project idea" in user_input:
        print("Bot: Here are some chemistry project ideas:\n"
              "- Acid-Base Reaction Showcase\n"
              "- Crystal Growing Demonstrations\n"
              "- Chemical Reaction Clock Display\n"
              "- Elephant Toothpaste Experiment\n"
              "- Dye-Sensitized Solar Cells Demo\n"
              "- Density Tower Exploration\n"
              "- Electrolysis of Water Exhibit\n"
              "- Chemical Garden Formation\n"
              "- Molecular Models and Isomerism\n"
              "- Food Chemistry Insights\n"
              "- Oxidation and Reduction Reactions\n"
              "- Chemiluminescence Display\n"
              "- Chromatography Experiments\n"
              "- Chemical Equilibrium Showcase\n"
              "- Fireworks Chemistry Unveiled\n")

    elif "biology project idea" in user_input:
        print("Bot: Here are some biology project ideas:\n"
              "- Plant Growth and Light Exposure\n"
              "- Investigating Microorganisms\n"
              "- Effects of Different Nutrients on Plant Growth\n"
              "- Animal Behavior Studies\n"
              "- Human Digestive System Simulation\n"
              "- Genetics and Heredity Experiments\n"
              "- Biodiversity Assessment\n"
              "- Environmental Impact Analysis\n"
              "- Cell Structure and Function Exploration\n"
              "- Photosynthesis and Respiration Demonstrations\n"
              "- Dissections and Anatomy Studies\n"
              "- Microscopic Life Observation\n"
              "- Ecosystem Health Assessment\n"
              "- Ethology: Animal Communication\n"
              "- Microbiology Cultivation\n"
              "- Marine Life Diversity Exploration\n")

    elif "physics project idea" in user_input:
        print("Bot: Here are some physics project ideas:\n"
              "- Projectile Motion Simulations\n"
              "- Constructing Simple Machines\n"
              "- Optics and Light Experiments\n"
              "- Waves and Sound Demonstrations\n"
              "- Renewable Energy Projects\n"
              "- Magnetism and Electromagnetism\n"
              "- Building a Electric Circuit\n"
              "- Friction and Motion Studies\n"
              "- Solar Oven Construction\n"
              "- Thermodynamics Demonstrations\n"
              "- Reflection and Refraction Studies\n"
              "- Exploring Forces and Newton's Laws\n"
              "- Electrical Energy Efficiency Tests\n"
              "- Pendulum Experiments\n"
              "- Investigating Fluid Dynamics\n"
              "- Balloon-Powered Car Design\n")

    elif "computer science project idea" in user_input:
        print("Bot: Here are some computer science project ideas:\n"
              "- Creating a Simple Website\n"
              "- Developing a Mobile App\n"
              "- Programming a Chatbot\n"
              "- Data Visualization Projects\n"
              "- Game Development and Design\n"
              "- Building a Database System\n"
              "- Cybersecurity and Encryption\n"
              "- AI and Machine Learning Applications\n"
              "- Internet of Things (IoT) Projects\n"
              "- Algorithm Design and Analysis\n"
              "- Social Media Analytics Tool\n"
              "- Virtual Reality or Augmented Reality\n"
              "- Natural Language Processing Tools\n"
              "- Cloud Computing Projects\n"
              "- Automation and Scripting\n"
              "- E-commerce Platform Development\n")

    else:
        print("Bot: Sorry, I didn't understand that.\n")
