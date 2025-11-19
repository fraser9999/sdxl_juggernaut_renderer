# SDXL Inference Renderer
# with Batch Mode, 
# uses a SDXL Juggernaut Lightning 4s Model
# for Picture generation.
# Hermann Knopp
# 19.11.2025 (Early Alpha Version)
# uses Python 3.10+ amd64
 

# init
import os
import os.path
os.system("cls")

print("importing libs..please wait...")


# Library
from diffusers import AutoPipelineForText2Image, StableDiffusionXLPipeline, DPMSolverMultistepScheduler
import torch
torch.cuda.empty_cache()

# Window System Libs
from tkinter import *
from PIL import Image,ImageTk


import random
from random import randrange
from datetime import datetime


# Display Window
main=Tk()
main.title("Diffusers SDXL Preview")

# Set Preview window/picture size 512x512px
tex_size_x=512
tex_size_y=512
canvas = Canvas(main,width=tex_size_x,height=tex_size_y)
canvas.pack()
canvas.update()


#Make Custom Ideas Dir
dir_path = os.path.dirname(os.path.realpath(__file__))
path = "render"
filepath= dir_path + "\\" + path
# Check whether the specified path exists or not
isExist = os.path.exists(filepath)
if not isExist:
   # Create a new directory because it does not exist
   os.makedirs(filepath)
   print("The new directory 'render' is created!")

# get path
dir_path = os.path.dirname(os.path.realpath(__file__))


# set juggernaut model directory, please adjust!!!
model=  dir_path + "/" + "sdxl_juggernaut_4step.safetensors"

# init render pipeline
pipe = StableDiffusionXLPipeline.from_single_file(model, torch_dtype=torch.float16, variant="fp16", use_safetensors=True).to("cuda")

pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)



#Mem Savings
pipe.enable_attention_slicing()

#Mem Optimizations
#pipe.enable_xformers_memory_efficient_attention(attention_op=MemoryEfficientAttentionFlashAttentionOp)
#pipe.vae.enable_xformers_memory_efficient_attention(attention_op=None)

pipe.set_use_memory_efficient_attention_xformers(True)
pipe.enable_vae_slicing()


#Main Loop
while True:

    os.system("cls")
    
    # check batch mode yes/no
    print("Are you happy with your prompt? can i start batch...(J/N)")
    zufr=input("J/N")
    if zufr=="":
       #No 
       startflag=0
    if zufr==None:
       #No
       startflag=0
    if zufr=="J" or zufr=="j" or zufr=="y" or zufr=="Y":
       #Yes
       startflag=1
    if zufr=="N" or zufr=="n":
       #No
       startflag=0



    #One Image Render Loop
    if startflag==0:

        print("")
        prompt=input("Enter Positive Prompt: ")
        if prompt=="":
            prompt = "Professional Photografer Shot,Anne Hathaway,Jeans,Black Shirt"
        print(prompt)
        positive_prompt = prompt

        #Enter Negative Prompt once
        print("") 
        negative=input("Enter Negative Prompt: ")
        if negative=="":
           negative="mutated arm, mutated hand, mutated finger, mutated face, mutated eyes, mutated mouth, painting, black and white, blurred out, blurry,image noise, dof, depth of field,"
           print(negative)
        negative_prompt=negative


        # Set System Variable MAX Seed
        max=4294967295


        # generate random Seed Value
        seed=random.randint(1,max)


        # Status/Set Random Seed. always another Picture 
    
        print("")
        print("Set Seed to: " + str(seed))
        g_cuda = torch.Generator('cuda').manual_seed(seed)
        print("")

        print("")
        print("Positive: ",str(prompt))
        print("")
        print("Negative: ",str(negative))
        print("")

        # Inference Pipe
        image = pipe(prompt=prompt,negative_prompt=negative,height=1024, width=1024,num_inference_steps=4, guidance_scale=2.0, generator=g_cuda).images[0]


        # preview image
        image2=image

        image2=image2.resize((512,512))
        tk_image = ImageTk.PhotoImage(image2)
        canvas.create_image(1,1, anchor=NW, image=tk_image)
        canvas.update()


        # datetime object containing current date and time
        now = datetime.now()
        dt_string = now.strftime("%d%m%Y_%H%M%S")
        filename=filepath + "//" + "test_" + dt_string +".png"

        # save file image
        image.save(filename)

        # empty torch mem
        torch.cuda.empty_cache()






    # Enter invinite Batch Mode witrh Random Seed for your entered prompt
    if startflag==1:
       
        print("")
        print("Infinite Batch Mode, Stops with Crtl+C")

        print("Set Maximum Batch Mode Images (None=10)")
        maximum=int(input("Max:"))
        if maximum==None or maximum=="":
            maximum=10
        if maximum==0:
            maximum=1
        if maximum>2000:
            maximum=2000


        #Start Picture 1
        endflag=0
        i = 0
        maximum=int(maximum)
   
        # Running an Infinite Loop til crtl+c for Realtime Render
        while endflag==0:

            #print((str(i),str(maximum))) 
         
            if i>=maximum:
                print("You have finished all Images...Exit")
                #break
                a=input("Wait Key")
                endflag=1
                startflag=0
                continue

            # render counter
            i=i+1
            print("Will Render Image Nr: " +str(i) + " from " +str(maximum))        



            # Set System Variable MAX Seed
            max=4294967295


            # generate random Seed Value
            seed=random.randint(1,max)


            # Status/Set Random Seed. always another Picture 
    
            print("")
            print("Set Seed to: " + str(seed))
            g_cuda = torch.Generator('cuda').manual_seed(seed)
            print("")

            print("")
            print("Positive: ",str(prompt))
            print("")
            print("Negative: ",str(negative))
            print("")

            # Inference pipe batch mode
            image = pipe(prompt=prompt,negative_prompt=negative, height=1024, width=1024,num_inference_steps=4, guidance_scale=2.0, generator=g_cuda).images[0]


            # preview image
            image2=image

            image2=image2.resize((512,512))
            tk_image = ImageTk.PhotoImage(image2)
            canvas.create_image(1,1, anchor=NW, image=tk_image)
            canvas.update()



            # datetime object containing current date and time
            now = datetime.now()
            dt_string = now.strftime("%d%m%Y_%H%M%S")
            filename2=filepath + "//" + str(i) + "_test_" + dt_string +".png"

            # save file image
            image.save(filename2)

            # empty torch mem
            torch.cuda.empty_cache()            











    